from django.urls import path
from .views import pagina, sobre,equipe, atividades, contato

urlpatterns = [
    path('', pagina, name="pagina"),
    path('sobre/',sobre, name="sobre"),
    path('equipe/', equipe, name="equipe"),
    path('atividades/', atividades, name="atividades"),
    path('contato/', contato, name="contato"),
]
