from rest_framework import serializers
from .models import Quiz, Category, Question, Answer







class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = "__all__"


class QuestionSerializer(serializers.ModelSerializer):
    answer = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ('updated', 'title', 'difficulty', 'date_created', 'quiz', 'answer')




class QuizSerializer(serializers.ModelSerializer):
    question = QuestionSerializer(many=True, read_only=True)
    class Meta:
        model = Quiz
        fields = ('name', 'created_date', 'category', 'question')

class CategorySerializer(serializers.ModelSerializer):
    quiz_set = QuizSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ("name", "quiz_set")
