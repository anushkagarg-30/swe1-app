from polls.models import Question, Choice
from django.utils import timezone


def ensure_question_with_choices(question_text, choices):
    question, _ = Question.objects.get_or_create(
        question_text=question_text,
        defaults={"pub_date": timezone.now()},
    )
    for choice_text in choices:
        Choice.objects.get_or_create(
            question=question, choice_text=choice_text, defaults={"votes": 0}
        )
    return question


ensure_question_with_choices(
    "What's your favorite programming language?",
    ["Python", "JavaScript", "Java"],
)

ensure_question_with_choices(
    "What's your favorite fruit?",
    ["Apple", "Banana", "Mango", "Orange"],
)

print("Sample polls ensured successfully (idempotent seeding).")
