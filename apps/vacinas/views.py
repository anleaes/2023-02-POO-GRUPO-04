from django.shortcuts import render

# Create your views here.

from .models import Vacina
from rest_framework import viewsets
from .serializer import VacinaSerializer

# Após o comentario "# Create your views here." e crie as views "Vacina".

class VacinaViewSet(viewsets.ModelViewSet):
    queryset = Vacina.objects.all()
    serializer_class = VacinaSerializer  
