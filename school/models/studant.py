from django.db import models

class Studant(models.Model):
    first_name = models.CharField(max_length=20, blank=False)
    last_name = models.CharField(max_length=60, blank=False)
    rg = models.CharField(max_length=11, blank=False)
    cpf = models.CharField(max_length=9, blank=False)
    cep = models.CharField(max_length=8, blank=False)
    date_birth = models.DateField()
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.first_name
