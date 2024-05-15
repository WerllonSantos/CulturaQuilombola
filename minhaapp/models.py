from django.db import models

# Create your models here.


class Voluntario(models.Model):
    nome = models.CharField(max_length=40)
    rg = models.IntegerField(max_length=10)
    orgExp = models.CharField(max_length=10)
    cpf = models.CharField(max_length=11)
    cep = models.CharField(max_length=8)
    estado = models.CharField(max_length=20)
    bairro = models.CharField(max_length=20)
    endereco = models.CharField(max_length=80)
    email = models.CharField(max_length=40)
    telefone = models.CharField(max_length=15)
    celular = models.CharField(max_length=15)
    sobrenome = models.CharField(max_length=100)
    genero = models.CharField(max_length=10)
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

