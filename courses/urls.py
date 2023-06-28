# urls.py
from django.urls import path
from .views import courses, create_course, create_form_handler, course_detail
urlpatterns = [
    path("courses/", courses, name="courses"),
    path("course/<int:course_id>/", course_detail, name="course"),
    path("course/create/", create_course),
    path("course/create/post/", create_form_handler, name="create_form_handler"),
]
