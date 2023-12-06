from .models import LocalVacinacao
from rest_framework import serializers

class LocalVacinacao(serializers.ModelSerializer):
    class Meta:
        model = LocalVacinacao
        fields = '__all__'