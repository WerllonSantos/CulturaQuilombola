from django import forms
from django.forms.widgets import DateInput
from django.core.exceptions import ValidationError
from .models import Voluntario, Doacao, Contato

class VoluntarioForm(forms.ModelForm):
    class Meta:
        model = Voluntario
        fields = ['nome', 'sobrenome', 'cpf','rg','orgExp','genero', 'telefone',
                  'celular', 'endereco', 'estado', 'cep',
                  'email', 'senha', 'concordou_termos_voluntariado',
                  'concordou_termos_imagem']

class VoluntarioForm(forms.ModelForm):
    class Meta:
        model = Voluntario
        fields = ['nome', 'sobrenome', 'cpf','rg','orgExp','genero', 'telefone',
                  'celular', 'endereco',  'estado', 'cep',
                  'email', 'senha', 'concordou_termos_voluntariado',
                  'concordou_termos_imagem']
        widgets = {
            'data_nascimento': DateInput(attrs={'type': 'date'})
        }

class VoluntarioForm(forms.ModelForm):
    def clean_cpf(self):
        cpf = self.cleaned_data['cpf']
        if Voluntario.objects.filter(cpf=cpf).exists():
            raise ValidationError('CPF já cadastrado.')
        return cpf

    class Meta:
        model = Voluntario
        fields = ['nome', 'sobrenome', 'cpf', 'rg','orgExp','genero', 'telefone',
                  'celular', 'endereco',  'estado', 'cep',
                  'email', 'senha', 'concordou_termos_voluntariado',
                  'concordou_termos_imagem']

class DoacaoForm(forms.ModelForm):
    class Meta:
        model = Doacao
        fields = ['nome', 'mensagemopcional', 'email', 'valor_doacao', 'data']
        widgets = {
            'mensagemopcional': forms.Textarea(attrs={'rows': 3}),
            'data': forms.DateInput(attrs={'type': 'date'}),
        }


class DoacaoForm(forms.ModelForm):
    def clean_valor_doacao(self):
        valor_doacao = self.cleaned_data['valor_doacao']
        if valor_doacao <= 0:
            raise ValidationError('O valor da doação deve ser maior que zero.')
        return valor_doacao

    class Meta:
        model = Doacao
        fields = ['nome', 'mensagemopcional', 'email', 'valor_doacao', 'data']

class DoacaoForm(forms.ModelForm):
    def clean_nome(self):
        nome = self.cleaned_data['nome']
        return nome.upper()

    class Meta:
        model = Doacao
        fields = ['nome', 'mensagemopcional', 'email', 'valor_doacao', 'data']


class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'email', 'mensagemopcional', 'celular']

    def clean_celular(self):
        celular = self.cleaned_data['celular']

        return celular
