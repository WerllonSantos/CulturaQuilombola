from django.urls import path, include
from rest_framework import routers
from .viewsets import voluntarioViewSet
from minhaapp.views import pagina, sobre, equipe, noticias, eventos, voluntario, doar, contato, createvoluntario, \
    readvoluntario, updatevoluntario, deletevoluntario, createdoar, readdoar, updatedoar, deletedoar, readcontato, \
    createcontato, updatecontato, deletecontato



router = routers.DefaultRouter()
router.register(r'voluntario', voluntarioViewSet, basename="voluntario")


urlpatterns = [
    path('', pagina, name='pagina'),
    path('sobre/', sobre, name='sobre'),
    path('equipe/', equipe, name='equipe'),
    path('noticias/', noticias, name='noticias'),
    path('eventos/', eventos, name='eventos'),
    path('voluntario/', voluntario, name='voluntario'),
    path('doar/', doar, name='doar'),
    path('contato/', contato, name='contato'),
    path('createvoluntario', createvoluntario, name='createvoluntario'),
    path('createdoar', createdoar, name='createdoar'),
    path('createcontato', createcontato, name='createcontato'),
    path('readvoluntario', readvoluntario, name='readvoluntario'),
    path('readdoar', readdoar, name='readdoar'),
    path('readcontato', readcontato, name='readcontato'),
    path('updatevoluntario/<int:id>', updatevoluntario, name='updatevoluntario'),
    path('updatedoar/<int:id>', updatedoar, name='updatedoar'),
    path('updatecontato/<int:id>', updatecontato, name='updatecontato'),
    path('deletevoluntario/<int:id>', deletevoluntario, name='deletevoluntario'),
    path('deletecontato/<int:id>', deletecontato, name='deletecontato'),
    path('deletedoar/<int:id>', deletedoar, name='deletedoar'),
    path('api/', include(router.urls)),

]