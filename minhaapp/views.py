from django.shortcuts import render

# Create your views here.

def pagina (request):
    return render(request, 'pagina.html')
def sobre (request):
    return render(request, 'sobre.html')

def equipe (request):
    return render(request, 'equipe.html')

def atividades (request):
    return render(request, 'atividades.html')

def voluntario (request):
    return render(request, 'voluntario.html')

def contato (request):
    return render(request, 'contato.html')
