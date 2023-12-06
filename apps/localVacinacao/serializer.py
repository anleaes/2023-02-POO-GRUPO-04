from .models import LocalVacinacao
from rest_framework import serializers

class LocalVacinacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocalVacinacao
        fields = '__all__'