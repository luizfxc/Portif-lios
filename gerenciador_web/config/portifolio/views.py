from django.shortcuts import render, get_object_or_404, redirect

from .models import Projeto, Tecnologia, ImagemProjeto


# ===============================
# LISTAGEM DE PROJETOS
# ===============================

def listar_projetos(request):
    projetos_salvos = Projeto.objects.all()

    contexto = {
        'meus_projetos': projetos_salvos
    }

    return render(request, 'portfolio/lista_projetos.html', contexto)


# ===============================
# DETALHE DO PROJETO
# ===============================

def detalhe_projeto(request, projeto_id):
    projeto = get_object_or_404(Projeto, pk=projeto_id)
    imagens = ImagemProjeto.objects.filter(projeto=projeto)

    return render(
        request,
        'portfolio/detalhe_projeto.html',
        {'projeto': projeto, 'imagens': imagens}
    )


# ===============================
# ADICIONAR PROJETO
# ===============================

def adicionar_projeto(request):
    tecnologias = Tecnologia.objects.all()

    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        link = request.POST.get('link')
        tecnologia_id = request.POST.get('tecnologia')

        tecnologia_selecionada = Tecnologia.objects.get(pk=tecnologia_id)

        Projeto.objects.create(
            titulo=titulo,
            descricao=descricao,
            link=link,
            tecnologia=tecnologia_selecionada
        )

        return redirect('listar_projetos')

    return render(request, 'portfolio/form_projeto.html', {'tecnologias': tecnologias})


# ===============================
# ALTERAR PROJETO
# ===============================

def alterar_projeto(request, projeto_id):
    projeto = get_object_or_404(Projeto, pk=projeto_id)
    tecnologias = Tecnologia.objects.all()

    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        link = request.POST.get('link')
        tecnologia_id = request.POST.get('tecnologia')

        tecnologia_selecionada = get_object_or_404(Tecnologia, pk=tecnologia_id)

        projeto.titulo = titulo
        projeto.descricao = descricao
        projeto.link = link
        projeto.tecnologia = tecnologia_selecionada

        projeto.save()

        return redirect('listar_projetos')

    contexto = {
        'projeto': projeto,
        'tecnologias': tecnologias,
    }

    return render(request, 'portfolio/form_projeto.html', contexto)


# ===============================
# EXCLUIR PROJETO
# ===============================

def excluir_projeto(request, projeto_id):
    projeto = get_object_or_404(Projeto, pk=projeto_id)

    if request.method == 'POST':
        projeto.delete()
        return redirect('listar_projetos')

    return render(
        request,
        'portfolio/confirmar_exclusao.html',
        {'projeto': projeto}
    )
