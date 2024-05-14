from django.shortcuts import render, redirect, get_object_or_404

from .forms import voluntarioForm, contatoForm


def pagina(request):
    return render(request, 'pagina.html')

def sobre(request):
    return render(request, 'sobre.html')
def equipe(request):
    return render(request, 'equipe.html')

def noticias(request):
    return render(request, 'noticias.html')

def eventos(request):
    return render(request, 'eventos.html')

def voluntario(request):
    return render(request, 'voluntario.html')

def doar(request):
    return render(request, 'doar.html')

def contato(request):
    return render(request, 'contato.html')


def createvoluntario(request):
    voluntarioForm = voluntarioForm(request.POST or None)
    if(voluntarioForm.is_valid()):
        voluntario = voluntarioForm.save(commit=False)
        voluntario.save()
        return redirect("voluntario")
    return render(request, 'voluntario.html', {'voluntarioForm':voluntarioForm})

def createdoar(request):
    doarForm = doarForm(request.POST or None)
    if(doarForm.is_valid()):
        doar = doarForm.save(commit=False)
        doar.save()
        return redirect("doar")
    return render(request, 'doar.html', {'doarForm':doarForm})

def createcontato(request):
    form_contato = contatoForm(request.POST or None)
    if form_contato.is_valid():
        contato_instance = form_contato.save(commit=False)
        contato_instance.save()
        return redirect("contato")
    return render(request, 'contato.html', {'contatoForm': form_contato})

def readvoluntario(request, voluntario=None):
    voluntario = voluntario.objects.all()
    return render(request, 'voluntario.html',
                  {'voluntario':voluntario})


def readdoar(request):
    doar = doar.objects.all()
    return render(request, 'doar.html',
                  {'doar':doar})


def readcontato(request, contato=None):
    contato = contato.objects.all()
    return render(request, 'contato.html',
                  {'contato':contato})

def updatevoluntario(request, id):
    voluntario = get_object_or_404(voluntario, pk=id)
    voluntarioForm = voluntarioForm(request.POST or None,
                            instance=voluntario)
    if(voluntarioForm.is_valid()):
        voluntario = voluntarioForm.save(commit=False)
        voluntario.save()
        return redirect("voluntario")
    return render(request, 'voluntario.html', {'voluntarioForm':voluntarioForm})


def updatedoar(request, id):
    doar = get_object_or_404(doar, pk=id)
    doarForm = doarForm(request.POST or None,
                                instance=doar)
    if(doarForm.is_valid()):
        doar = doarForm.save(commit=False)
        doar.save()
        return redirect("doar")
    return render(request, 'doar.html', {'doarForm':doarForm})

def updatecontato(request, id):
    contato = get_object_or_404(contato, pk=id)
    contatoForm = contatoForm(request.POST or None,
                                instance=contato)
    if(contatoForm.is_valid()):
        contato = contatoForm.save(commit=False)
        contato.save()
        return redirect("contato")
    return render(request, 'contato.html', {'contatoForm':contatoForm})

def deletevoluntario(request, id):
    voluntario = get_object_or_404(voluntario, pk=id)
    voluntario.delete()
    return redirect("voluntario")

def deletedoar(request, id):
    doar = get_object_or_404(doar, pk=id)
    doar.delete()
    return redirect("doar")

def deletecontato(request, id):
    contato = get_object_or_404(contato, pk=id)
    contato.delete()
    return redirect("contato")

