from django.db import models
# from users.models import CustomUser

class Department(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Designation(models.Model):
    name = models.CharField(max_length=50)
    is_student = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Course(models.Model):
    couse_code = models.CharField(max_length=15, unique=True)
    name = models.CharField(max_length=256)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.couse_code
