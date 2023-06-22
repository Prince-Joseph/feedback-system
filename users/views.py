from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import CustomUserForm

def profile(request):
    context = {
        "form" : CustomUserForm()
    }
    
    return render(request, "profile.html", context)


def profile_update(request):
    if request.method == "POST":
        form = CustomUserForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
        messages.add_message(request, messages.INFO, "Profile Updated")
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
