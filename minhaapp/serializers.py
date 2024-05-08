from .models import voluntario
from rest_framework import serializers

class voluntarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = voluntario
        fields = ['nome','rg','orgExp','cpf','cep',
        'estado','bairro','endereco','email','telefone',
                  'celular']


