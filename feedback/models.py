from django.db import models
from institute.models import Designation
from courses.models import Course
from users.models import CustomUser


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


class CourseFeedback(models.Model):
    is_active = models.BooleanField(default=True)
    course = models.ForeignKey(Course, on_delete=models.PROTECT)

class UserFeedback(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    course_feedback = models.ForeignKey(CourseFeedback, on_delete=models.CASCADE)
    score = models.IntegerField()

