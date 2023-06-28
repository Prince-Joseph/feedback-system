import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "feedback_evaluation_system.settings")
django.setup()

from users.models import CustomUser

import random
import string

# Users
for x in range(26,10000):
    user = CustomUser()
    user.username = f"A{str(x).rjust(3, '0')}"
    user.fullname = f"A{str(x).rjust(3, '0')}"
    user.set_password("admin")
    # print(user.username)
    user.save()