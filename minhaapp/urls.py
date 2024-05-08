from django.urls import path, include
from rest_framework import routers
from .viewsets import voluntarioViewSet
from .views import pagina, sobre, equipe, noticias, eventos, voluntario, doar, contato, createvoluntario, readvoluntario, updatevoluntario, deletevoluntario, sobre, equipe

router = routers.DefaultRouter()
router.register(r'voluntario', voluntarioViewSet, basename="voluntario")



urlpatterns = [
    path('', pagina, name='pagina'),
    path('sobre/', sobre, name="sobre"),
    path('equipe/', equipe, name="equipe"),
    path('noticias/', noticias, name="noticias"),
    path('eventos/', eventos, name="eventos"),
    path('voluntario/', voluntario, name="voluntario"),
    path('doar/', doar, name="doar"),
    path('contato/', contato, name="contato"),
    path('createvoluntario', createvoluntario, name='createvoluntario'),
    path('readvoluntario', readvoluntario, name='readvoluntario'),
    path('updatevoluntario/<int:id>', updatevoluntario, name='updatevoluntario'),
    path('deletevoluntario/<int:id>', deletevoluntario, name='deletevoluntario'),
    path('api/', include(router.urls)),

  ]