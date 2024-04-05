from django.db import models

class Voluntario(models.Model):
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)
    apelido = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14)
    data_nascimento = models.DateField()
    genero = models.CharField(max_length=20)
    telefone = models.CharField(max_length=20)
    celular = models.CharField(max_length=20)
    endereco = models.CharField(max_length=255)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    cep = models.CharField(max_length=9)

    def __str__(self):
        return self.nome
