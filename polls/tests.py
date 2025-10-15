from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone
from .models import Question, Choice


class QuestionModelTests(TestCase):
    def test_question_creation(self):
        """Test that a question can be created"""
        question = Question.objects.create(
            question_text="What's up?", pub_date=timezone.now()
        )
        self.assertEqual(question.question_text, "What's up?")
        self.assertIsNotNone(question.pub_date)

    def test_question_str_representation(self):
        """Test the string representation of Question"""
        question = Question.objects.create(
            question_text="Test question", pub_date=timezone.now()
        )
        self.assertEqual(str(question), "Test question")


class ChoiceModelTests(TestCase):
    def test_choice_creation(self):
        """Test that a choice can be created"""
        question = Question.objects.create(
            question_text="Test question", pub_date=timezone.now()
        )
        choice = Choice.objects.create(
            question=question, choice_text="Test choice", votes=0
        )
        self.assertEqual(choice.choice_text, "Test choice")
        self.assertEqual(choice.votes, 0)
        self.assertEqual(choice.question, question)


class PollsViewTests(TestCase):
    def setUp(self):
        """Set up test data"""
        self.client = Client()
        self.question = Question.objects.create(
            question_text="Test question", pub_date=timezone.now()
        )
        self.choice = Choice.objects.create(
            question=self.question, choice_text="Test choice", votes=0
        )

    def test_index_view(self):
        """Test the polls index view"""
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test question")

    def test_detail_view(self):
        """Test the polls detail view"""
        response = self.client.get(reverse("polls:detail", args=(self.question.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test question")
        self.assertContains(response, "Test choice")

    def test_results_view(self):
        """Test the polls results view"""
        response = self.client.get(reverse("polls:results", args=(self.question.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test question")
