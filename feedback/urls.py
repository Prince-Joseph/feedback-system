from django.urls import path
from .views import feedback_view, feedback_handler

urlpatterns = [
    path("feedback", feedback_view),
    path("feedback/post/", feedback_handler, name="feedback_handler")
]
