from django import forms
from .models import voluntario, doar

class voluntarioForm(forms.ModelForm):
    class Meta:
        model = voluntario
        fields = ['nome','sobrenome','Comogostaiadeserchamado',
        'cpf','datadenascimento', 'genero', 'cep',
        'estado', 'bairro', 'endereco','telefone','celular',
                  'email']

class doarForm(forms.ModelForm):
    class Meta:
        model = doar
        fields = ['nome','mensagemopcional', 'email','valor_doacao', ]

