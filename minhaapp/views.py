from django.shortcuts import render

# Create your views here.

def pagina (request):
    return render(request, 'pagina.html')
def sobre (request):
    return render(request, 'sobre.html')

def equipe (request):
    return render(request, 'equipe.html')

def noticias (request):
    return render(request, 'noticias.html')

def eventos (request):
    return render(request, 'eventos.html')

def voluntario (request):
    return render(request, 'voluntario.html')

def doar (request):
    return render(request, 'doar.html')

def contato (request):
    return render(request, 'contato.html')
