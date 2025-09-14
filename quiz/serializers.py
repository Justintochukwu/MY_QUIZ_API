from rest_framework import serializers
from .models import Quizzes, Question

class QuizSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Quizzes 
        fields = [
            'title',
        ]
        
class RandomQuestionSerializer(serializers.ModelSerializer):
    
    answer = serializers.StringRelatedField(many=True)
    
    class Meta:
        
        model = Question
        field = [
            'title','answer'
        ]