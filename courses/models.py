from django.db import models
from institute.models import Department
from users.models import CustomUser

class Course(models.Model):
    couse_code = models.CharField(max_length=15, unique=True)
    name = models.CharField(max_length=256)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.couse_code


class CourseParticipant(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

class CourseTeacher(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)