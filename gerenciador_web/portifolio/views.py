from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse 
from .models import Projeto, Tecnologia, ImagemProjeto 
from .forms import ProjetoForm, TecnologiaForm, ImagemProjetoForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

def listar_projetos(request):
    """
    View para listar todos os projetos.
    Busca os projetos no banco de dados e renderiza o template.
    """
    projetos = Projeto.objects.all()
    contexto = {
        'projetos': projetos
    }
    
    return render(request, 'portifolio/lista_projetos.html', contexto)


def detalhe_projeto(request, projeto_id):
    """
    Exibe os detalhes de um projeto específico.
    Se o projeto não for encontrado, retorna um erro 404.
    """
    # 1. Busca o objeto Projeto pelo ID. Se não encontrar, lança um erro 404.
    projeto = get_object_or_404(Projeto, id=projeto_id)
    
    # 2. Prepara o contexto. O objeto 'projeto' contém todas as informações, 
    #    incluindo as relações com tecnologias e imagens (graças ao related_name).
    contexto = {
        'projeto': projeto
    }
    
    # 3. Renderiza o template 'portifolio/detalhe_projeto.html' com o contexto.
    return render(request, 'portifolio/detalhe_projeto.html', contexto)

@staff_member_required
def adicionar_projeto(request):
    """Adiciona um novo projeto usando ModelForm (APENAS STAFF)."""
    if request.method == "POST":
        form = ProjetoForm(request.POST) 
        if form.is_valid():
            projeto = form.save() 
            return redirect('portifolio:detalhe_projeto', projeto.id)
    else:
        form = ProjetoForm() 
    return render(request, 'portifolio/projeto_form.html', {'form': form})


@staff_member_required
def alterar_projeto(request, projeto_id):
    """Altera um projeto existente usando ModelForm (APENAS STAFF)."""
    projeto = get_object_or_404(Projeto, id=projeto_id)
    
    if request.method == "POST":
        form = ProjetoForm(request.POST, instance=projeto) 
        if form.is_valid():
            form.save()
            return redirect('portifolio:detalhe_projeto', projeto.id)
    else:
        form = ProjetoForm(instance=projeto)
        
    return render(request, 'portifolio/projeto_form.html', {'form': form, 'projeto': projeto})


@staff_member_required
def excluir_projeto(request, projeto_id):
    """Remove um projeto existente (APENAS STAFF)."""
    projeto = get_object_or_404(Projeto, id=projeto_id)
    
    if request.method == 'POST':
        projeto.delete()
        return redirect('portifolio:listar_projetos')
    
    return render(request, 'portifolio/projeto_confirm_delete.html', {'projeto': projeto})

# ==========================================================
# VIEWS DE TECNOLOGIAS
# ==========================================================

@staff_member_required
def tecnologia_listar(request):
    """Lista todas as tecnologias (APENAS STAFF)."""
    tecnologias = Tecnologia.objects.all().order_by('nome')
    contexto = {
        'tecnologias': tecnologias
    }
    return render(request, 'portifolio/tecnologia_lista.html', contexto)


@staff_member_required
def tecnologia_criar(request):
    """Cria uma nova tecnologia usando ModelForm (APENAS STAFF)."""
    if request.method == "POST":
        form = TecnologiaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('portifolio:tecnologia_listar')
    else:
        form = TecnologiaForm()
        
    return render(request, 'portifolio/tecnologia_form.html', {'form': form})


@staff_member_required
def tecnologia_editar(request, tecnologia_id):
    """Edita uma tecnologia existente (APENAS STAFF)."""
    tecnologia = get_object_or_404(Tecnologia, id=tecnologia_id)
    
    if request.method == "POST":
        form = TecnologiaForm(request.POST, instance=tecnologia)
        if form.is_valid():
            form.save()
            return redirect('portifolio:tecnologia_listar')
    else:
        form = TecnologiaForm(instance=tecnologia)

    return render(request, 'portifolio/tecnologia_form.html', {'form': form, 'tecnologia': tecnologia})


@staff_member_required
def tecnologia_excluir(request, tecnologia_id):
    """Remove uma tecnologia existente (APENAS STAFF)."""
    tecnologia = get_object_or_404(Tecnologia, id=tecnologia_id)
    
    if request.method == 'POST':
        tecnologia.delete()
        return redirect('portifolio:tecnologia_listar')
    
    return render(request, 'portifolio/tecnologia_confirm_delete.html', {'tecnologia': tecnologia})


# ==========================================================
# VIEWS DE IMAGENS
# ==========================================================

@staff_member_required
def imagem_listar(request, projeto_id):
    """Lista as imagens de um projeto específico para gestão (APENAS STAFF)."""
    projeto = get_object_or_404(Projeto, id=projeto_id)
    imagens = projeto.imagens.all() 
    contexto = {
        'projeto': projeto,
        'imagens': imagens
    }
    return render(request, 'portifolio/imagem_lista.html', contexto)


@staff_member_required
def imagem_criar(request, projeto_id): 
    """Adiciona uma nova imagem a um projeto, processando o upload (APENAS STAFF)."""
    projeto = get_object_or_404(Projeto, id=projeto_id)
    
    if request.method == 'POST':
        form = ImagemProjetoForm(request.POST, request.FILES) 
        
        if form.is_valid():
            imagem = form.save(commit=False)
            imagem.projeto = projeto 
            imagem.save()
            return redirect('portifolio:detalhe_projeto', projeto_id=projeto.id)
    
    else:
        form = ImagemProjetoForm()
        
    contexto = {
        'form': form,
        'projeto': projeto,
    }
    return render(request, 'portifolio/imagem_form.html', contexto)


@staff_member_required
def imagem_excluir(request, imagem_id):
    """Remove uma imagem específica (APENAS STAFF)."""
    imagem = get_object_or_404(ImagemProjeto, id=imagem_id)
    projeto_id = imagem.projeto.id 
    
    if request.method == 'POST':
        imagem.delete()
        return redirect('portifolio:detalhe_projeto', projeto_id=projeto_id)
    
    return render(request, 'portifolio/imagem_confirm_delete.html', {'imagem': imagem})