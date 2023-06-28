from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import QuestionPermit, Question
import re

def active_feedbacks(request):
    context = {}
    return render(request, "feedback/active_feedbacks.html", context)


def feedback_view(request):
    permitted_questions_list = QuestionPermit.objects.filter(
        designation__id=request.user.designation.id
    ).values_list("id")
    questions = Question.objects.filter(id__in=permitted_questions_list)
    context = {"questions": questions}
    return render(request, "feedback/feedback_form.html", context)


def feedback_handler(request):
    if request.method == "POST":
        sum_score = 0
        max_score = 0

        # extract question id
        for l in request.POST:
            if l != "csrfmiddlewaretoken":
                question_number = int(re.findall(r"\d+", l)[0])
                value = int(request.POST[l])
                question = Question.objects.get(id=question_number)
                score = question.priority * value
                max_score = max_score + (question.priority)
                sum_score = sum_score + score

        print(sum_score / max_score)
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
