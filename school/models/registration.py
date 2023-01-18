from django.db import models
from school.models import Studant, Course

class Registration(models.Model):
    studant = models.ForeignKey(Studant, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    initial_date = models.DateField()
    deadline = models.DateField()

    def __str__(self):
        return f'{self.studant} - {self.course}'
