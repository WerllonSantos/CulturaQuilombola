from django.urls import path, include
from rest_framework import routers
from .viewsets import VoluntarioViewSet, DoacaoViewSet, ContatoViewSet
from minhaapp.views import pagina, sobre, equipe, noticias, eventos, voluntario, Doacao, contato, createvoluntario, \
    readvoluntario, updatevoluntario, deletevoluntario, createDoacao, readDoacao, updateDoacao, deleteDoacao, readcontato, \
    createcontato, updatecontato, deletecontato, cadastrar_voluntario



router = routers.DefaultRouter()
router.register(r'voluntario', VoluntarioViewSet, basename="voluntario")
router.register(r'Doacao', DoacaoViewSet, basename="Doacao")
router.register(r'contato', ContatoViewSet, basename="Contato")


urlpatterns = [
    path('', pagina, name='pagina'),
    path('sobre/', sobre, name='sobre'),
    path('equipe/', equipe, name='equipe'),
    path('noticias/', noticias, name='noticias'),
    path('eventos/', eventos, name='eventos'),
    path('voluntario/', voluntario, name='voluntario'),
    path('Doacao/', Doacao, name='Doacao'),
    path('contato/', contato, name='contato'),
    path('createvoluntario', createvoluntario, name='createvoluntario'),
    path('createDoacao', createDoacao, name='createDoacao'),
    path('createcontato', createcontato, name='createcontato'),
    path('readvoluntario', readvoluntario, name='readvoluntario'),
    path('readDoacao', readDoacao, name='readDoacao'),
    path('readcontato', readcontato, name='readcontato'),
    path('updatevoluntario/<int:id>', updatevoluntario, name='updatevoluntario'),
    path('updateDoacao/<int:id>', updateDoacao, name='updateDoacao'),
    path('updatecontato/<int:id>', updatecontato, name='updatecontato'),
    path('deletevoluntario/<int:id>', deletevoluntario, name='deletevoluntario'),
    path('deletecontato/<int:id>', deletecontato, name='deletecontato'),
    path('deleteDoacao/<int:id>', deleteDoacao, name='deleteDoacao'),
    path('cadastrar_voluntario/', cadastrar_voluntario, name='voluntario'),
    path('api/', include(router.urls)),

]