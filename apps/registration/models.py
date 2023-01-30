from django.db import models
from course.models import Course
from studant.models import Studant

class Registration(models.Model):
    studant = models.ForeignKey(Studant, on_delete=models.CASCADE, blank=False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, blank=False)
    initial_date = models.DateField(blank=False)
    deadline = models.DateField(blank=False)

    def __str__(self):
        return f'{self.studant} - {self.course}'
