from django.urls import path
from .views import QuestionList, QuizDetail, QuizList, CategoryList

urlpatterns = [   
    
    path("quiz/", QuizList.as_view()),
    path("question/", QuestionList.as_view()),
    path("category/", CategoryList.as_view()),
    path("quiz-detail/<int:id>", QuizDetail.as_view()),
]