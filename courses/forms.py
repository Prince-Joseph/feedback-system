from django.forms import DateInput, ModelForm
from .models import Course


class CourseCreateForm(ModelForm):
    class Meta:
        model = Course
        fields = "__all__"
        widgets = {
            "start_date": DateInput(attrs={"type": "date"}),
            "end_date": DateInput(attrs={"type": "date"}),
        }
