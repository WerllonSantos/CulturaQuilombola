from django.contrib import admin
from .models import Voluntario, Doacao, Contato, InscricaoNewsletter

admin.site.register(Voluntario)
admin.site.register(Doacao)
admin.site.register(Contato)
admin.site.register(InscricaoNewsletter)