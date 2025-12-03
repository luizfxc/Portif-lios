from django.shortcuts import render, get_object_or_404, redirect
from .models import Projeto, Tecnologia, ImagemProjeto
from .forms import ProjetoForm, TecnologiaForm 



def adicionar_projeto(request):
    """Adiciona um novo projeto usando ModelForm."""
    if request.method == "POST":

        form = ProjetoForm(request.POST) 
        if form.is_valid():

            projeto = form.save() 
            return redirect('portifolio:detalhe_projeto', projeto.id)
    else:

        form = ProjetoForm() 
        
    return render(request, 'portifolio/projeto_form.html', {'form': form})


def alterar_projeto(request, projeto_id):
    """Altera um projeto existente usando ModelForm."""
    projeto = get_object_or_404(Projeto, id=projeto_id)
    
    if request.method == "POST":

        form = ProjetoForm(request.POST, instance=projeto) 
        if form.is_valid():
            form.save()
            return redirect('portifolio:detalhe_projeto', projeto.id)
    else:

        form = ProjetoForm(instance=projeto)
        
    return render(request, 'portifolio/projeto_form.html', {'form': form, 'projeto': projeto})



def tecnologia_criar(request):
    """Cria uma nova tecnologia usando ModelForm."""
    if request.method == "POST":
        form = TecnologiaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('portifolio:tecnologia_listar')
    else:
        form = TecnologiaForm()
        
    return render(request, 'portifolio/tecnologia_form.html', {'form': form})


def tecnologia_editar(request, tecnologia_id):
    """Edita uma tecnologia existente usando ModelForm."""
    tecnologia = get_object_or_404(Tecnologia, id=tecnologia_id)
    
    if request.method == "POST":
        form = TecnologiaForm(request.POST, instance=tecnologia)
        if form.is_valid():
            form.save()
            return redirect('portifolio:tecnologia_listar')
    else:
        form = TecnologiaForm(instance=tecnologia)

    return render(request, 'portifolio/tecnologia_form.html', {'form': form, 'tecnologia': tecnologia})

