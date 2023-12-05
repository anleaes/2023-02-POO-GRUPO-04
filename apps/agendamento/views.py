from django.shortcuts import render

# Create your views here.

from .models import Agendamento
from rest_framework import viewsets
from .serializer import AgendamentoSerializer

# Após o comentario "# Create your views here." e crie as views "Agendamento".

class AgendamentoViewSet(viewsets.ModelViewSet):
    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer  