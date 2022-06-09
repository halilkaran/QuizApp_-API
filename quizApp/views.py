from django.shortcuts import HttpResponse, get_object_or_404
from rest_framework import generics
from quizApp.models import Category, Question, Quiz
from .serializer import CategorySerializer, QuestionSerializer, QuizSerializer



# Create your views here.

def home(request):
    return HttpResponse('<h1>API Page</h1>')

class QuizList(generics.ListAPIView):
    # permission_classes = [IsAdminOrReadOnly]
    serializer_class = QuizSerializer
    queryset = Quiz.objects.all()

class QuestionList(generics.ListAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    
class CategoryList(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    

class QuizDetail(generics.RetrieveAPIView):
    serializer_class = QuizSerializer
    queryset = Quiz.objects.all()
    lookup_field='id'
