from django.db import models

class Course(models.Model):
    LEVEL = (
        ('B', 'Basic'),
        ('I', 'Intermediary'),
        ('A', 'Advenced'),
        ('S', 'Specialist'),
    )
    CATEGORY = (
        ('M', 'Medicine'),
        ('T', 'Tech'),
        ('E', 'Engineering'),
        ('S', 'Sale'),
    )
    summary = models.CharField(max_length=10, blank=False)
    description = models.CharField(max_length=100, blank=False)
    level = models.CharField(max_length=1, choices=LEVEL, blank=False, default='B')
    duration = models.CharField(max_length=10, default='10 hours', blank=False)
    category = models.CharField(max_length=1, default='T', blank=False)

    def __str__(self):
        return self.summary
