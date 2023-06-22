from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    fullname = models.CharField(max_length=256, null=True, blank=True)
    contact_number = models.CharField(max_length=10,null=True, blank=True)
