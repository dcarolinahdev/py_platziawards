# Python
import datetime
# Django
from django.test import TestCase
from django.urls.base import reverse
from django.utils import timezone
# Models
from .models import Question

# Test Set for Model
class QuestionModelTest(TestCase):

    def test_was_published_recently_with_future_questions(self):
        """was_published_recently returns False for questions
        whose pub_date is in the future."""
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(question_text='Who is the best CD in Platzi?', pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_past_questions(self):
        """was_published_recently returns False for questions
        whose pub_date is in the past."""
        time = timezone.now() - datetime.timedelta(days=30)
        past_question = Question(question_text='Who is the best CD in Platzi?', pub_date=time)
        self.assertFalse(past_question.was_published_recently())

    def test_was_published_recently_with_present_questions(self):
        """was_published_recently returns False for questions
        whose pub_date is in the present."""
        time = timezone.now()
        present_question = Question(question_text='Who is the best CD in Platzi?', pub_date=time)
        self.assertTrue(present_question.was_published_recently())

# Test Set for View
class QuestionIndexViewTest(TestCase):

    def test_no_questions(self):
        """If no question exist, an appropiate message is displayed."""
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context["latest_question_list"], [])
