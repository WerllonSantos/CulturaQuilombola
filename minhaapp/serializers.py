from .models import Voluntario, Doacao,Contato
from rest_framework import serializers

class VoluntarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voluntario
        fields = ['nome','rg','orgExp','cpf','cep',
        'estado','bairro','endereco','email','telefone',
                  'celular']


class DoacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doacao
        fields = ['nome','mensagemopcional', 'email','valor_doacao', 'data','contador_doacoes', ]

class ContatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contato
        fields = ['nome', 'celular', 'email','mensagemopcional']