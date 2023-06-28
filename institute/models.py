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
