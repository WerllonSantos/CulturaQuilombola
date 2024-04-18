from django.db import models

# Create your models here.

class voluntario(models.Model):
    nome = models.CharField(max_length=40)
    sobrenome = models.IntegerField()
    Comogostaiadeserchamado = models.CharField(max_length=10)
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
    nome = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    valordadoação = models.CharField(max_length=40)
    mensagemopcional = models.CharField(max_length=500)

    def __str__(self):
        return self.nome

