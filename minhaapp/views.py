from django.shortcuts import render, redirect, get_object_or_404
from .forms import VoluntarioForm, DoacaoForm, ContatoForm


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

def Doacao(request):
    return render(request, 'Doacao.html')

def contato(request):
    return render(request, 'contato.html')


def createvoluntario(request):
    voluntarioForm = voluntarioForm(request.POST or None)
    if(voluntarioForm.is_valid()):
        voluntario = voluntarioForm.save(commit=False)
        voluntario.save()
        return redirect("voluntario")
    return render(request, 'voluntario.html', {'voluntarioForm':voluntarioForm})

def createDoacao(request):
    DoacaoForm = DoacaoForm(request.POST or None)
    if(DoacaoForm.is_valid()):
        Doacao = DoacaoForm.save(commit=False)
        Doacao.save()
        return redirect("Doacao")
    return render(request, 'Doacao.html', {'DoacaoForm':DoacaoForm})

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


def readDoacao(request):
    Doacao = Doacao.objects.all()
    return render(request, 'Doacao.html',
                  {'Doacao':Doacao})


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


def updateDoacao(request, id):
    Doacao = get_object_or_404(Doacao, pk=id)
    DoacaoForm = DoacaoForm(request.POST or None,
                                instance=Doacao)
    if(DoacaoForm.is_valid()):
        Doacao = doarForm.save(commit=False)
        Doacao.save()
        return redirect("Doacao")
    return render(request, 'Doacao.html', {'DoacaoForm':DoacaoForm})

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

def deleteDoacao(request, id):
    Doacao = get_object_or_404(Doacao, pk=id)
    Doacao.delete()
    return redirect("Doacao")

def deletecontato(request, id):
    contato = get_object_or_404(contato, pk=id)
    contato.delete()
    return redirect("contato")

def cadastrar_voluntario(request):
    if request.method == 'POST':
        # Extrair dados do formulário
        nome = request.POST['name']
        sobrenome = request.POST['sobrenome']
        cpf = request.POST['cpf']
        data_nascimento = request.POST['dataNascimento']
        genero = request.POST['genero']
        telefone = request.POST['telefone']
        celular = request.POST['celular']
        endereco = request.POST['address']
        cidade = request.POST['city']
        estado = request.POST['state']
        cep = request.POST['zip']
        email = request.POST['email']
        senha = request.POST['password']
        concordou_termos_voluntariado = 'termosVoluntariado' in request.POST
        concordou_termos_imagem = 'termosImagem' in request.POST

        # Salvar no banco de dados
        voluntario = Voluntario(nome=nome, sobrenome=sobrenome, cpf=cpf, data_nascimento=data_nascimento,
                                genero=genero, telefone=telefone, celular=celular, endereco=endereco, cidade=cidade,
                                estado=estado, cep=cep, email=email, senha=senha,
                                concordou_termos_voluntariado=concordou_termos_voluntariado,
                                concordou_termos_imagem=concordou_termos_imagem)
        voluntario.save()

        # Redirecionar após salvar
        return redirect('pagina_sucesso')

    return render(request, 'voluntario.html')