from polls.models import Question, Choice
from django.utils import timezone

q = Question.objects.create(question_text="What's your favorite programming language?", pub_date=timezone.now())
q.choice_set.create(choice_text="Python", votes=0)
q.choice_set.create(choice_text="JavaScript", votes=0)
q.choice_set.create(choice_text="Java", votes=0)

print("Sample poll and choices created successfully.")
