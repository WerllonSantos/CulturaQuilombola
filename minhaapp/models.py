from django.db import models

# Create your models here.


class Voluntario(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14)
    data_nascimento = models.DateField()
    genero = models.CharField(max_length=10)
    telefone = models.CharField(max_length=20)
    celular = models.CharField(max_length=20)
    endereco = models.CharField(max_length=255)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    cep = models.CharField(max_length=9)
    email = models.EmailField()
    senha = models.CharField(max_length=100)
    concordou_termos_voluntariado = models.BooleanField()
    concordou_termos_imagem = models.BooleanField()

    def __str__(self):
        return self.nome

class Doacao(models.Model):
    nome = models.CharField(max_length=100)
    mensagemopcional = models.TextField()
    email = models.EmailField()
    valor_doacao = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()
    contador_doacoes = models.IntegerField(default=0)

    def __str__(self):
        return self.nome

class Contato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    mensagemopcional = models.TextField()
    celular = models.CharField(max_length=20)
    data_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

