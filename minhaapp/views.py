from django.shortcuts import render, redirect, get_object_or_404
from .forms import voluntarioForm, doarForm
from . models import voluntario, doar


# Create your views here.
def pagina (request):
    return render(request, 'pagina.html')
def sobre (request):
    return render(request, 'sobre.html')

def equipe(request):
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

def createvoluntario(request):
    voluntarioForm = voluntarioForm(request.POST or None)
    if(voluntarioForm.is_valid()):
        voluntario = voluntarioForm.save(commit=False)
        voluntario.save()
        return redirect("readvoluntario")
    return render(request, 'createvoluntario.html', {'voluntarioForm':voluntarioForm})


def readvoluntario(request):
    voluntario = voluntario.objects.all()
    return render(request, 'readvoluntario.html',
                  {'voluntario':voluntario})


def updatevoluntario(request, id):
    voluntario = get_object_or_404(voluntario, pk=id)
    voluntarioForm = voluntarioForm(request.POST or None,
                            instance=voluntario)
    if(voluntarioForm.is_valid()):
        voluntario = voluntarioForm.save(commit=False)
        voluntario.save()
        return redirect("readvoluntario")
    return render(request, 'createvoluntario.html', {'voluntarioForm':voluntarioForm})



def deletevoluntario(request, id):
    voluntario = get_object_or_404(voluntario, pk=id)
    voluntario.delete()
    return redirect("readvoluntario")


