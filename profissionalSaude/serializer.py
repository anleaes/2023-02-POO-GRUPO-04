from .models import ProfissionalSaude
from rest_framework import serializers

class ProfissionalSaudeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfissionalSaude
        fields = '__all__'
        