from .models import RegistroVacinação
from rest_framework import serializers

class RegistroVacinaçãoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroVacinação
        fields = '__all__'