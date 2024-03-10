from django.urls import path
from .views import pagina, sobre,equipe, atividades,voluntario, contato

urlpatterns = [
    path('', pagina, name="pagina"),
    path('sobre/',sobre, name="sobre"),
    path('equipe/', equipe, name="equipe"),
    path('atividades/', atividades, name="atividades"),
    path('voluntario/', voluntario, name="voluntario"),
    path('contato/', contato, name="contato"),

]
