from django.db import models
from vacinas import Vacina
from Pessoa import Pessoa

# Create your models here.
class RegistroVacinação(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    vacina = models.ForeignKey(Vacina, on_delete=models.CASCADE)
    data = models.DateField()
    profissional_saude = models.CharField(max_length=100)