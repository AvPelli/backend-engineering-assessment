from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QuizViewSet, QuestionViewSet, AnswerViewSet, ParticipantViewSet, quiz_view, redirect_to_participant_quizzes

router = DefaultRouter()
router.register(r'quiz', QuizViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'answers', AnswerViewSet)
router.register(r'participants', ParticipantViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('quiz/<int:id>/',quiz_view, name='quiz'),
    path('api/quiz/<int:pk>/questions/', QuizViewSet.as_view({'get': 'questions'}), name='quiz-questions'),
    path('api/participants/<int:user_id>/quizzes/',ParticipantViewSet.as_view({'get':'quizzes'}), name='quizzes'),
    path('quizzes/<int:user_id>/', redirect_to_participant_quizzes, name='redirect-quizzes'),
]
