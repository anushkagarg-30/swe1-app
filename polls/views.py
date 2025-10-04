from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Question, Choice

# Static vote storage for testing AWS deployment
# This is a temporary solution - votes will reset when server restarts
STATIC_VOTES = {}

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        # Show all questions on the index page, newest first
        return Question.objects.order_by("-pub_date")

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        question = self.get_object()
        
        # Add static vote counts to context
        static_votes = {}
        for choice in question.choice_set.all():
            choice_key = f"{question.id}_{choice.id}"
            static_votes[choice.id] = STATIC_VOTES.get(choice_key, 0)
        
        context['static_votes'] = static_votes
        return context

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # Only allow POST submissions to cast a vote. Redirect GETs back to detail.
    if request.method != "POST":
        return HttpResponseRedirect(reverse("polls:detail", args=(question.id,)))
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(request, "polls/detail.html", {
            "question": question,
            "error_message": "You didn't select a choice.",
        })
    else:
        # Use static storage instead of database for testing AWS deployment
        choice_key = f"{question_id}_{selected_choice.id}"
        if choice_key not in STATIC_VOTES:
            STATIC_VOTES[choice_key] = 0
        STATIC_VOTES[choice_key] += 1
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
