from django.urls import path

from . import views  

urlpatterns = [
    
    path('', views.listar_projetos, name='listar_projetos'),
    path('<int:projeto_id>/', views.detalhe_projeto, name='detalhe_projeto'),

    path('adicionar/', views.adicionar_projeto, name='adicionar_projeto'),
    path('<int:projeto_id>/alterar/', views.alterar_projeto, name='alterar_projeto'),
    path('<int:projeto_id>/excluir/', views.excluir_projeto, name='excluir_projeto'),

    
    path('tecnologias/', views.tecnologia_listar, name='tecnologia_listar'),
    path('tecnologias/adicionar/', views.tecnologia_criar, name='tecnologia_criar'),
    path('tecnologias/<int:tecnologia_id>/alterar/', views.tecnologia_editar, name='tecnologia_editar'),
    path('tecnologias/<int:tecnologia_id>/excluir/', views.tecnologia_excluir, name='tecnologia_excluir'),

    
    path('<int:projeto_id>/imagens/', views.imagem_listar, name='imagem_listar'),
    path('<int:projeto_id>/imagens/adicionar/', views.imagem_criar, name='imagem_criar'),
    path('imagens/<int:imagem_id>/excluir/', views.imagem_excluir, name='imagem_excluir'),

]
