from django.db import models

class Voluntario(models.Model):
    nome = models.CharField(max_length=40)
    cpf = models.CharField(max_length=11)
    rg = models.CharField(max_length=8)
    orgExp = models.CharField(max_length=10)
    cep = models.CharField(max_length=8)
    estado = models.CharField(max_length=20)
    bairro = models.CharField(max_length=20)
    endereco = models.CharField(max_length=80)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    celular = models.CharField(max_length=15)
    sobrenome = models.CharField(max_length=100)
    genero = models.CharField(max_length=10)
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
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Contato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    mensagemopcional = models.TextField()
    celular = models.CharField(max_length=20)
    data_envio = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

