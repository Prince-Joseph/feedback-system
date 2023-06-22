from django.shortcuts import render
from .models import QuestionPermit, Question


def feedback_view(request):
    permitted_questions_list = QuestionPermit.objects.filter(
        designation__id=request.user.designation.id
    ).values_list('id')
    questions = Question.objects.filter(id__in = permitted_questions_list)
    context = {"questions": questions}
    return render(request, "feedback_form.html", context)
