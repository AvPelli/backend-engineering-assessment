from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from ..models import Quiz, Participant
from ..views import QuizViewSet, ParticipantViewSet

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.quiz = Quiz.objects.create(title='Sample Quiz',creator_id=1)
        self.participant = Participant.objects.create(user_id=self.user.id, quiz_id=self.quiz.id,score=0)

    def test_quiz_view(self):
        response = self.client.get(reverse('quiz', args=[self.quiz.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_quiz_questions_view(self):
        response = self.client.get(reverse('quiz-questions', args=[self.quiz.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_participant_quizzes_view(self):
        response = self.client.get(reverse('quizzes', args=[self.participant.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_redirect_to_participant_quizzes(self):
        response = self.client.get(reverse('redirect-quizzes', args=[self.participant.id]))
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
