from django.contrib import admin
from .models import Voluntario, Doacao, Contato

# Register your models here.
admin.site.register(Voluntario)
admin.site.register(Doacao)
admin.site.register(Contato)