from django.contrib import admin
from .models import voluntario, doar, contato

# Register your models here.
admin.site.register(voluntario)
admin.site.register(doar)
admin.site.register(contato)