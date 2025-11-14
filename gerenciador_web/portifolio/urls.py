# portifolio/urls.py (Versão Completa)

from django.urls import path
from .views import (
    listar_projetos, detalhe_projeto, adicionar_projeto, alterar_projeto, excluir_projeto,
    tecnologia_listar, tecnologia_criar, tecnologia_editar, tecnologia_excluir,
    imagem_listar, imagem_criar, imagem_excluir
)

# Definir o namespace da aplicação (boa prática)
app_name = 'portifolio' 


urlpatterns = [
    
    # Views de Projetos
    path('', listar_projetos, name='listar_projetos'),
    path('<int:projeto_id>/', detalhe_projeto, name='detalhe_projeto'),
    path('adicionar/', adicionar_projeto, name='adicionar_projeto'),
    path('<int:projeto_id>/alterar/', alterar_projeto, name='alterar_projeto'),
    path('<int:projeto_id>/excluir/', excluir_projeto, name='excluir_projeto'),

    # Views de Tecnologias
    path('tecnologias/', tecnologia_listar, name='tecnologia_listar'),
    path('tecnologias/adicionar/', tecnologia_criar, name='tecnologia_criar'),
    path('tecnologias/<int:tecnologia_id>/alterar/', tecnologia_editar, name='tecnologia_editar'),
    path('tecnologias/<int:tecnologia_id>/excluir/', tecnologia_excluir, name='tecnologia_excluir'),

    # Views de Imagens
    path('<int:projeto_id>/imagens/', imagem_listar, name='imagem_listar'),
    path('<int:projeto_id>/imagens/adicionar/', imagem_criar, name='imagem_criar'),
    path('imagens/<int:imagem_id>/excluir/', imagem_excluir, name='imagem_excluir'),

]