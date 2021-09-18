#Django
from .models import Answer, Question
from rest_framework import serializers


class QuestionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Question
        fields = ['profile','title', 'detail_question']


class AnswerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Answer
        fields = ['profile', 'detail_answer', 'question']
