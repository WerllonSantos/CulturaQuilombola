from rest_framework import viewsets
from .serializers import voluntarioSerializer
from .models import voluntario

class voluntarioViewSet(viewsets.ModelViewSet):
    model = voluntario
    serializer_class = voluntarioSerializer
    queryset = voluntario.objects.all()
    filter_fields = ('nome','rg','orgExp','cpf','cep',
                     'estado','bairro','endereco','email','telefone',
                     'celular')