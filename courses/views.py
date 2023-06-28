from django.http import HttpResponseRedirect
from django.shortcuts import render
from courses.models import Course, CourseParticipant
from courses.forms import CourseCreateForm
from django.contrib import messages


# decorator staff
def courses(request):
    context = {
        "courses": Course.get_relevant_courses(request.user),
    }
    return render(request, "courses/courses.html", context)


def create_course(request):
    logged_in_user = request.user

    context={}
    context['form'] = CourseCreateForm()
    if logged_in_user.designation.name == "CCO":
        return render(request, "courses/course_creation_form.html", context)
    
    elif logged_in_user.designation.name == "Basic DS":
        return render(request, "courses/course_creation_form.html", context)

    else:
        return HttpResponseRedirect("/")

def create_form_handler(request):
    if request.method == "POST":
             # extract question id
        form = CourseCreateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, "Course Created")

    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

def course_detail(request, course_id):
    context = {}
    context['course'] = Course.objects.get(id= course_id)
    context['course_particpants'] = CourseParticipant.objects.filter(course__id= course_id)
    return render(request, "courses/course_detail.html", context)   
