from django.db import models
from vacinas.models import Vacina
from Pessoa.models import Pessoa

#Create your models here.
class Agendamento(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    vacina = models.ForeignKey(Vacina, on_delete=models.CASCADE)
    data = models.DateField()
