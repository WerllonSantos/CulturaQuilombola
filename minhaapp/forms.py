from django.forms import ModelForm
from .models import voluntario,doar

class voluntarioForm(ModelForm):
    class Meta:
        model = voluntario
        fields = ['nome','sobrenome','Comogostaiadeserchamado',
        'cpf','datadenascimento', 'genero', 'cep',
        'estado', 'bairro', 'endereco','telefone','celular',
                  'email']


class doarForm(ModelForm):
    class Meta:
        model = doar
        fields = ['nome','valordadoação','mensagemopcional', 'email', ]

