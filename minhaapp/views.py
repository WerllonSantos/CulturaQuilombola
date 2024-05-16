from django.shortcuts import render, redirect, get_object_or_404
from .forms import VoluntarioForm, DoacaoForm, ContatoForm
from .models import Voluntario, Doacao, Contato


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
    if request.method == 'POST':
        voluntarioForm = VoluntarioForm(request.POST)
        if voluntarioForm.is_valid():
            voluntario = voluntarioForm.save()
            return redirect('Voluntario')
    else:
        voluntarioForm = VoluntarioForm()

    return render(request, 'voluntario.html', {'VoluntarioForm': voluntarioForm})


def Doacao(request):
    return render(request, 'Doacao.html')


def Contato(request):
    if request.method == 'POST':
        contatoForm = ContatoForm(request.POST)
        if contatoForm.is_valid():
            contato = contatoForm.save()
            return redirect('Contato')
    else:
        contatoForm = ContatoForm()

    return render(request, 'contato.html', {'ContatoForm': contatoForm})


def createVoluntario(request):
    voluntarioForm = VoluntarioForm(request.POST or None)
    if voluntarioForm.is_valid():
        voluntario = voluntarioForm.save(commit=False)
        voluntario.save()
        return redirect('Voluntario')
    return render(request, 'voluntario.html', {'VoluntarioForm': voluntarioForm})

def createDoacao(request):
    DoacaoForm = DoacaoForm(request.POST or None)
    if(DoacaoForm.is_valid()):
        Doacao = DoacaoForm.save(commit=False)
        Doacao.save()
        return redirect("Doacao")
    return render(request, 'Doacao.html', {'DoacaoForm':DoacaoForm})

def createContato(request):
    contatoForm = ContatoForm(request.POST or None)
    if contatoForm.is_valid():
        contato = ContatoForm.save(commit=False)
        contato.save()
        return redirect("Contato")
    return render(request, 'contato.html', {'ContatoForm': ContatoForm})

def readVoluntario(request, Voluntario=None):
    Voluntario = Voluntario.objects.all()
    return render(request, 'voluntario.html',
                  {'Voluntario':Voluntario})


def readDoacao(request):
    Doacao = Doacao.objects.all()
    return render(request, 'Doacao.html',
                  {'Doacao':Doacao})


def readContato(request, Contato=None):
    Contato = Contato.objects.all()
    return render(request, 'contato.html',
                  {'Contato':Contato})

def updateVoluntario(request, id):
    Voluntario = get_object_or_404(Voluntario, pk=id)
    VoluntarioForm = VoluntarioForm(request.POST or None,
                            instance=Voluntario)
    if(voluntarioForm.is_valid()):
        Voluntario = VoluntarioForm.save(commit=False)
        Voluntario.save()
        return redirect("Voluntario")
    return render(request, 'voluntario.html', {'VoluntarioForm':VoluntarioForm})


def updateDoacao(request, id):
    Doacao = get_object_or_404(Doacao, pk=id)
    DoacaoForm = DoacaoForm(request.POST or None,
                                instance=Doacao)
    if(DoacaoForm.is_valid()):
        Doacao = DoacaoForm.save(commit=False)
        Doacao.save()
        return redirect("Doacao")
    return render(request, 'Doacao.html', {'DoacaoForm':DoacaoForm})

def updateContato(request, id):
    Contato = get_object_or_404(contato, pk=id)
    ContatoForm = ContatoForm(request.POST or None,
                                instance=Contato)
    if(contatoForm.is_valid()):
        Contato = ContatoForm.save(commit=False)
        Contato.save()
        return redirect("Contato")
    return render(request, 'contato.html', {'ContatoForm':ContatoForm})

def deleteVoluntario(request, id):
    Voluntario = get_object_or_404(Voluntario, pk=id)
    Voluntario.delete()
    return redirect("Voluntario")

def deleteDoacao(request, id):
    Doacao = get_object_or_404(Doacao, pk=id)
    Doacao.delete()
    return redirect("Doacao")

def deleteContato(request, id):
    Contato = get_object_or_404(Contato, pk=id)
    Contato.delete()
    return redirect("Contato")
def cadastrar_Voluntario(request):
    if request.method == 'POST':
        # Extrair dados do formulário
        nome = request.POST['name']
        sobrenome = request.POST['sobrenome']
        cpf = request.POST['cpf']
        genero = request.POST['genero']
        telefone = request.POST['telefone']
        celular = request.POST['celular']
        endereco = request.POST['address']
        estado = request.POST['state']
        cep = request.POST['zip']
        email = request.POST['email']
        senha = request.POST['password']
        concordou_termos_voluntariado = 'termosVoluntariado' in request.POST
        concordou_termos_imagem = 'termosImagem' in request.POST

        # Salvar no banco de dados
        voluntario = Voluntario(nome=nome, sobrenome=sobrenome, cpf=cpf, genero=genero, telefone=telefone,
                                celular=celular, endereco=endereco,
                                estado=estado, cep=cep, email=email, senha=senha,
                                concordou_termos_voluntariado=concordou_termos_voluntariado,
                                concordou_termos_imagem=concordou_termos_imagem)
        voluntario.save()

        # Redirecionar após salvar
        return redirect('pagina_sucesso')

    return render(request, 'voluntario.html')
