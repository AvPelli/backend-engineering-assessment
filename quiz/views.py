from django.shortcuts import render, redirect
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Quiz, Question, Answer, Participant
from .serializers import QuizSerializer, QuestionSerializer, AnswerSerializer, ParticipantSerializer


def quiz_view(request, id):
    return render(request, 'quiz.html', {'quiz_id': id})

def redirect_to_participant_quizzes(request, user_id):
    return redirect('quizzes', user_id=user_id)


#Return data in JSON format by serializing objects -> these can be answers to API calls
class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

    @action(detail=True, methods=['get'])
    def questions(self, request, pk=None):
        quiz = self.get_object()
        questions = Question.objects.filter(quiz=quiz)
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

class ParticipantViewSet(viewsets.ModelViewSet):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer

    @action(detail=False, methods=['get'], url_path=r'(?P<user_id>\d+)/quizzes')
    def get_user_quizzes(self, request, user_id=None):
        user_quizzes = Participant.objects.filter(user_id=user_id)
        serializer = self.get_serializer(user_quizzes, many=True)
        return Response(serializer.data)
