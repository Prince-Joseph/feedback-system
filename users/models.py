from django.contrib.auth.models import AbstractUser
from django.db import models
from institute.models import Designation, Department


class CustomUser(AbstractUser):
    fullname = models.CharField(max_length=256, null=True, blank=True)
    contact_number = models.CharField(max_length=10, null=True, blank=True)
    designation = models.ForeignKey(Designation, on_delete=models.PROTECT)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
