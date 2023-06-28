from django.urls import path
from .views import feedback_view, feedback_handler

urlpatterns = [
    path("feedbacks/active/", feedback_view),
    path("feedback/", feedback_view),
    path("feedback/post/", feedback_handler, name="feedback_handler")
]
