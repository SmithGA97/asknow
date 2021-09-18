#Django
from .models import Question
from rest_framework import serializers


class QuestionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Question
        fields = ['profile','title', 'detail_question']
     
