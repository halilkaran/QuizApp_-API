from django.contrib import admin
from .models import Answer, Category, Question, Quiz
import nested_admin
#answer başka tablonun içinde olacak şekile inlien olarak hazırla
class Answerinline(nested_admin.NestedTabularInline):
  model = Answer
  extra = 4
  max_num = 4
class Questioninline(nested_admin.NestedTabularInline):
  model = Question
  inlines = [Answerinline]
  extra = 1
  max_num = 10
class QuizAdmin(nested_admin.NestedModelAdmin):
  model = Quiz
  inlines = [Questioninline]
class QuestionAdmin(nested_admin.NestedModelAdmin):
  model = Question
  inlines = [Answerinline]
admin.site.register(Category)
admin.site.register(Quiz,QuizAdmin)
# admin.site.register(Question, QuestionAdmin)
# admin.site.register(Answer)