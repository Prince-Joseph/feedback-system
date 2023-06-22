from django.urls import path
from .views import profile, profile_update
urlpatterns = [
    path("profile/", profile),
    path("profile/update/", profile_update, name="profile_update")
]