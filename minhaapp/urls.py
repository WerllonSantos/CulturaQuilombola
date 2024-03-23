from django.urls import path
from .views import pagina, sobre,equipe, noticias, eventos, voluntario,doar, contato

urlpatterns = [
    path('', pagina, name="pagina"),
    path('sobre/', sobre, name="sobre"),
    path('equipe/', equipe, name="equipe"),
    path('noticias/', noticias, name="noticias"),
    path('eventos/', eventos, name="eventos"),
    path('voluntario/', voluntario, name="voluntario"),
    path('doar/', doar, name="doar"),
    path('contato/', contato, name="contato"),

]
