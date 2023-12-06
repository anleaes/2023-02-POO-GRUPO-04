from django.db import models

# Create your models here.
class EstoqueVacinas(models.Model):
    vacina = models.ForeignKey(Vacina, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    data_validade = models.DateField()