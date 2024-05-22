from django.shortcuts import render, redirect, get_object_or_404
from minhaapp.forms import VoluntarioForm, DoacaoForm, ContatoForm, InscricaoNewsletterForm
from minhaapp.models import Voluntario, Doacao, Contato, InscricaoNewsletter


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
        nome = request.POST.get('name', '')
        sobrenome = request.POST.get('sobrenome', '')
        cpf = request.POST.get('cpf','')
        genero = request.POST.get('genero', '')
        telefone = request.POST.get('telefone', '')
        celular = request.POST.get('celular', '')
        endereco = request.POST.get('address', '')
        estado = request.POST.get('state', '')
        cep = request.POST.get('zip', '')
        email = request.POST.get('email', '')
        senha = request.POST.get('password', '')
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

def pagina_sucesso(request):
    return render(request, 'pagina_sucesso.html')

def cadastrar_voluntario(request):
    if request.method == 'POST':
        form = VoluntarioForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('pagina_sucesso')
    else:
        form = VoluntarioForm()

    return render(request, 'cadastrar_voluntario.html', {'form': form})

def mostrar_voluntario(request, voluntario_id):
    voluntario = Voluntario.objects.get(pk=voluntario_id)
    return render(request, 'mostrar_voluntario.html', {'voluntario': voluntario})

def lista_contatos(request):
    contatos = Contato.objects.all()
    return render(request, 'lista_contatos.html', {'contatos': contatos})

def pagina_inscricao(request):
    form = InscricaoNewsletterForm()
    return render(request, 'pagina_inscricao.html', {'form': form})

def InscricaoNewsletter(request):
    if request.method == 'POST':
        form = InscricaoNewsletterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            NewsletterInscricao.objects.create(email=email)  # Certifique-se de que `NewsletterInscricao` é o modelo
            return redirect('pagina_sucesso_inscricao')
    else:
        form = InscricaoNewsletterForm()
    return render(request, 'pagina_inscricao.html', {'form': form})

def pagina_sucesso_inscricao(request):
    return render(request, 'pagina_sucesso_inscricao.html')