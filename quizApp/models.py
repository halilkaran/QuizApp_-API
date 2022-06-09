from django.db import models

class Category(models.Model):
    Category_name = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural ="Categories"
    def __str__(self):
        return self.Category_name

class Quiz(models.Model):   
    Quiz_name = models.CharField(max_length=40)
    created_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT) 
    def __str__(self):
        return self.Quiz_name

class Question(models.Model):
    OPTIONS = (
        ("d", "Difficult"),
        ("n", "Normal"),("e", "Easy")
    )
    updated = models.DateTimeField(auto_now=True)
    Question_text = models.CharField(max_length=40)
    difficulty = models.CharField(max_length=10, choices=OPTIONS, default="d")
    date_created = models.DateTimeField(auto_now_add=True)
    quiz = models.ForeignKey(Quiz, on_delete=models.PROTECT, related_name='question')
    def __str__(self):
        return self.Question_text

class Answer(models.Model) :
    updated = models.DateTimeField(auto_now=True)
    answer_text = models.CharField(max_length=100)
    is_right = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.PROTECT, related_name='answer')
    def __str__(self):
        return self.answer_text