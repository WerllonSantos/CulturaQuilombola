from rest_framework import viewsets
from .serializers import VoluntarioSerializer, DoacaoSerializer, ContatoSerializer
from .models import Voluntario, Doacao, Contato

class VoluntarioViewSet(viewsets.ModelViewSet):
    model = Voluntario
    serializer_class = VoluntarioSerializer
    queryset = Voluntario.objects.all()
    filter_fields = ('nome', 'sobrenome',
        'cpf','rg','orgExp' 'data_nascimento', 'genero', 'telefone',
        'celular', 'endereco', 'cidade','estado', 'cep',
        'email', 'senha', 'concordou_termos_voluntariado',
         'concordou_termos_imagem',)

class DoacaoViewSet(viewsets.ModelViewSet):
    model = Doacao
    serializer_class = DoacaoSerializer
    queryset = Doacao.objects.all()
    filter_fields = ('nome','mensagemopcional', 'email','valor_doacao',
                     'data','contador_doacoes',)

class ContatoViewSet(viewsets.ModelViewSet):
    model = Contato
    serializer_class = ContatoSerializer
    queryset = Contato.objects.all()
    filter_fields = ('nome', 'celular', 'email','mensagemopcional',)