from django.db import models
from vacinas.models import Vacina

# Create your models here.
class EstoqueVacinas(models.Model):
    vacina = models.ForeignKey(Vacina, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    data_validade = models.DateField()

def __str__(self):
    return self.vacina
