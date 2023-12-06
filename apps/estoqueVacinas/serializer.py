from .models import EstoqueVacinas
from rest_framework import serializers

class EstoqueVacinasSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstoqueVacinas
        fields = '__all__'