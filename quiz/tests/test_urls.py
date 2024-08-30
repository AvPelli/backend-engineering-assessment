from django.test import TestCase
from django.urls import reverse, resolve
from ..views import QuizViewSet,ParticipantViewSet,quiz_view,redirect_to_participant_quizzes

class TestUrls(TestCase):

    def test_quiz_url_resolves(self):
        url = reverse('quiz', args=[1])
        self.assertEqual(resolve(url).func, quiz_view)

    def test_quiz_questions_url_resolves(self):
        url = reverse('quiz-questions', args=[1])
        self.assertEqual(resolve(url).func.cls, QuizViewSet)

    def test_participant_quizzes_url_resolves(self):
        url = reverse('quizzes', args=[1])
        self.assertEqual(resolve(url).func.cls, ParticipantViewSet)

    def test_redirect_quizzes_url_resolves(self):
        url = reverse('redirect-quizzes', args=[1])
        self.assertEqual(resolve(url).func, redirect_to_participant_quizzes)
