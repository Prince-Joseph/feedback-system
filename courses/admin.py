from django.contrib import admin
from .models import Course, CourseParticipant

admin.site.register(Course)
admin.site.register(CourseParticipant)
