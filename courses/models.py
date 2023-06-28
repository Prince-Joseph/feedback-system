from django.db import models
from institute.models import Department
from users.models import CustomUser

class Course(models.Model):
    course_code = models.CharField(max_length=15, unique=True)
    name = models.CharField(max_length=256)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    course_incharge = models.ForeignKey(CustomUser, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.course_code

    def get_relevant_courses(user):
        courses = None
        print(user.isDesignation("CCO"))
        if user.isDesignation("CCO"):
            courses = Course.objects.filter(department = user.department)
        elif user.isDesignation("Basic DS"):
            courses = Course.objects.filter(course_incharge = user)
        return courses

    @property
    def t_score(self):
        students = self.courseparticipant_set.all()
        t = 0
        """
        T SCORE CALCULATIONS
        """
        if students:
            for student in students:
                diff = student.final_marks - student.initial_marks
                t = t+diff

            t= t/len(students)
        return t



class CourseParticipant(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    initial_marks = models.IntegerField(null=True, blank=True)
    final_marks = models.IntegerField(null=True, blank=True)

class CourseTeacher(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)