from django.shortcuts import render

# Create your views here.

from .models import RegistroVacinação
from rest_framework import viewsets
from .serializer import RegistroVacinaçãoSerializer

# Após o comentario "# Create your views here." e crie as views "RegistroVacinação".

class RegistroVacinaçãoViewSet(viewsets.ModelViewSet):
    queryset = RegistroVacinação.objects.all()
    serializer_class = RegistroVacinaçãoSerializer  