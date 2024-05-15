from django import forms
from .models import Voluntario, Doacao, Contato

class VoluntarioForm(forms.ModelForm):
    class Meta:
        model = Voluntario
        fields = ['nome', 'sobrenome', 'cpf', 'data_nascimento', 'genero', 'telefone',
        'celular', 'endereco', 'cidade','estado', 'cep',
        'email', 'senha', 'concordou_termos_voluntariado',
         'concordou_termos_imagem',]

class DoacaoForm(forms.ModelForm):
    class Meta:
        db_table = 'minhaapp_Doacao'
        model = Doacao
        fields = ['nome','mensagemopcional', 'email','valor_doacao', 'data','contador_doacoes', ]


class ContatoForm(forms.ModelForm):
    class Meta:
        db_table = 'minhaapp_Contato'
        model = Contato
        fields = ['nome', 'celular', 'email', 'mensagem']

    mensagem = forms.CharField(widget=forms.Textarea, required=False, label='Mensagem Opcional')
