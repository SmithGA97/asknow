from django_filters import filterset
from apps.posts.models import Answer, Question
from django.shortcuts import render
from .serializers import QuestionSerializer, AnswerSerializer
from rest_framework import viewsets
import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class QuestionFilter(django_filters.FilterSet):
    class Meta:
        model = Question
        fields = {
            'title': ['exact'],
            'detail_question': ['contains']
        }


# Create your views here.
class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    filterset_class = QuestionFilter
    filter_backends = [DjangoFilterBackend]
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]


class AnswerViewSet(viewsets.ModelViewSet):
    queryset= Answer.objects.all()
    serializer_class= AnswerSerializer

    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = self.queryset
        profile = self.request.GET.get('profile')
        if profile:
            queryset = queryset.filter(profile=profile)
        return queryset
