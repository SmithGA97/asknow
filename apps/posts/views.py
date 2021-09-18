from apps.posts.models import Question
from django.shortcuts import render
from .serializers import QuestionSerializer
from rest_framework import viewsets

# Create your views here.
class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
