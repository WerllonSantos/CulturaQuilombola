from django.urls import path, include
from rest_framework import routers
from .viewsets import VoluntarioViewSet, DoacaoViewSet, ContatoViewSet
from minhaapp.views import pagina, sobre, equipe, noticias, eventos, Voluntario, Doacao, Contato, createVoluntario, \
    readVoluntario, updateVoluntario, deleteVoluntario, createDoacao, readDoacao, updateDoacao, deleteDoacao, \
    readContato, createContato, updateContato, deleteContato, cadastrar_Voluntario, pagina_sucesso, mostrar_voluntario, \
    lista_contatos, pagina_inscricao, InscricaoNewsletter, pagina_sucesso_inscricao


router = routers.DefaultRouter()
router.register(r'Voluntario', VoluntarioViewSet, basename="Voluntario")
router.register(r'Doacao', DoacaoViewSet, basename="Doacao")
router.register(r'Contato', ContatoViewSet, basename="Contato")


urlpatterns = [
    path('', pagina, name='pagina'),
    path('sobre/', sobre, name='sobre'),
    path('equipe/', equipe, name='equipe'),
    path('noticias/', noticias, name='noticias'),
    path('eventos/', eventos, name='eventos'),
    path('Voluntario/', Voluntario, name='Voluntario'),
    path('Doacao/', Doacao, name='Doacao'),
    path('Contato/', Contato, name='Contato'),
    path('createVoluntario', createVoluntario, name='createVoluntario'),
    path('createDoacao', createDoacao, name='createDoacao'),
    path('createContato', createContato, name='createContato'),
    path('readVoluntario', readVoluntario, name='readVoluntario'),
    path('readDoacao', readDoacao, name='readDoacao'),
    path('readContato', readContato, name='readContato'),
    path('updateVoluntario/<int:id>', updateVoluntario, name='updateVoluntario'),
    path('updateDoacao/<int:id>', updateDoacao, name='updateDoacao'),
    path('updateContato/<int:id>', updateContato, name='updateContato'),
    path('deleteVoluntario/<int:id>', deleteVoluntario, name='deleteVoluntario'),
    path('deleteContato/<int:id>', deleteContato, name='deleteContato'),
    path('deleteDoacao/<int:id>', deleteDoacao, name='deleteDoacao'),
    path('cadastrar_Voluntario/', cadastrar_Voluntario, name='Voluntario'),
    path('pagina_sucesso/', pagina_sucesso, name='pagina_sucesso'),
    path('mostrar_voluntario/<int:voluntario_id>/', mostrar_voluntario, name='mostrar_voluntario'),
    path('lista_contatos/', lista_contatos, name='lista_contatos'),
    path('', pagina_inscricao, name='pagina_inscricao'),
    path('inscrever/', InscricaoNewsletter, name='inscrever_newsletter'),
    path('sucesso-inscricao/', pagina_sucesso_inscricao, name='pagina_sucesso_inscricao'),
    path('api/', include(router.urls)),

]