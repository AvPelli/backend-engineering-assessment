#from django.shortcuts import render

from rest_framework import viewsets
from .models import Quiz, Question, Answer, Participant
from .serializers import QuizSerializer, QuestionSerializer, AnswerSerializer, ParticipantSerializer

#Return data in JSON format by serializing objects -> these can be answers to API calls
class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

class ParticipantViewSet(viewsets.ModelViewSet):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer
