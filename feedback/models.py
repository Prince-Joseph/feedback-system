from django.db import models
from institute.models import Designation

class Question(models.Model):
    text = models.TextField()
    max_value = models.IntegerField()
    priority = models.IntegerField()
    def __str__(self):
        return f'q# {self.id}'


class QuestionPermit(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    designation = models.ForeignKey(Designation, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'q# {self.id} {self.designation}'