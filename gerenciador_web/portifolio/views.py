from django.shortcuts import render, get_object_or_404, redirect

from .models import Projeto, Tecnologia, ImagemProjeto




def listar_projetos(request):
    projetos = Projeto.objects.all()
    return render(request, 'portifolio/listar_projetos.html', {'projetos': projetos})


def detalhe_projeto(request, projeto_id):
    projeto = get_object_or_404(Projeto, id=projeto_id)
    imagens = ImagemProjeto.objects.filter(projeto=projeto)
    return render(request, 'portifolio/detalhe_projeto.html', {
        'projeto': projeto,
        'imagens': imagens
    })


def adicionar_projeto(request):
    if request.method == "POST":
        titulo = request.POST['titulo']
        descricao = request.POST['descricao']
        link = request.POST.get('link', '')

        projeto = Projeto.objects.create(
            titulo=titulo,
            descricao=descricao,
            link=link
        )
        return redirect('portifolio:projeto_detalhe', projeto.id)

    return render(request, 'portifolio/projeto_form.html')


def alterar_projeto(request, projeto_id):
    projeto = get_object_or_404(Projeto, id=projeto_id)

    if request.method == "POST":
        projeto.titulo = request.POST['titulo']
        projeto.descricao = request.POST['descricao']
        projeto.link = request.POST.get('link', '')
        projeto.save()

        return redirect('portifolio:projeto_detalhe', projeto.id)

    return render(request, 'portifolio/projeto_form.html', {'projeto': projeto})


def excluir_projeto(request, projeto_id):
    projeto = get_object_or_404(Projeto, id=projeto_id)
    projeto.delete()
    return redirect('portifolio:projeto_listar')



def tecnologia_listar(request):
    tecnologias = Tecnologia.objects.all()
    return render(request, 'portifolio/tecnologia_listar.html', {'tecnologias': tecnologias})


def tecnologia_criar(request):
    if request.method == "POST":
        nome = request.POST['nome']
        Tecnologia.objects.create(nome=nome)
        return redirect('portifolio:tecnologia_listar')

    return render(request, 'portifolio/tecnologia_form.html')


def tecnologia_editar(request, tecnologia_id):
    tecnologia = get_object_or_404(Tecnologia, id=tecnologia_id)

    if request.method == "POST":
        tecnologia.nome = request.POST['nome']
        tecnologia.save()
        return redirect('portifolio:tecnologia_listar')

    return render(request, 'portifolio/tecnologia_form.html', {'tecnologia': tecnologia})


def tecnologia_excluir(request, tecnologia_id):
    tecnologia = get_object_or_404(Tecnologia, id=tecnologia_id)
    tecnologia.delete()
    return redirect('portifolio:tecnologia_listar')



def imagem_listar(request, projeto_id):
    projeto = get_object_or_404(Projeto, id=projeto_id)
    imagens = ImagemProjeto.objects.filter(projeto=projeto)
    return render(request, 'portifolio/imagem_listar.html', {
        'projeto': projeto,
        'imagens': imagens
    })


def imagem_criar(request, projeto_id):
    projeto = get_object_or_404(Projeto, id=projeto_id)

    if request.method == "POST":
        imagem = request.FILES.get('imagem')
        ImagemProjeto.objects.create(projeto=projeto, imagem=imagem)
        return redirect('portifolio:imagem_listar', projeto.id)

    return render(request, 'portifolio/imagem_form.html', {'projeto': projeto})


def imagem_excluir(request, imagem_id):
    img = get_object_or_404(ImagemProjeto, id=imagem_id)
    projeto_id = img.projeto.id
    img.delete()
    return redirect('portifolio:imagem_listar', projeto_id)
