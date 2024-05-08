from django.db import models

# Create your models here.


class voluntario(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    Comogostaiadeserchamado = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    datadenascimento = models.CharField(max_length=8)
    genero = models.CharField(max_length=20)
    cep = models.CharField(max_length=8)
    estado = models.CharField(max_length=20)
    bairro = models.CharField(max_length=20)
    endereco = models.CharField(max_length=80)
    email = models.CharField(max_length=40)
    telefone = models.CharField(max_length=15)
    celular = models.CharField(max_length=15)

    def __str__(self):
        return self.nome

class doar(models.Model):
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    valor_doacao = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()
    contador_doacoes = models.IntegerField(default=0)
    mensagemopcional = models.CharField(max_length=500)

    def __str__(self):
        return self.nome

