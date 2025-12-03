from django.contrib import admin
from .models import Tecnologia, Projeto, ImagemProjeto



class ImagemProjetoInline(admin.TabularInline):
    model = ImagemProjeto
    extra = 1 
    fields = ('imagem', 'legenda')



@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):

    list_display = ('titulo', 'data_criacao', 'link')

    search_fields = ('titulo', 'descricao')

    inlines = [ImagemProjetoInline]

    filter_horizontal = ('tecnologias',)



@admin.register(Tecnologia)
class TecnologiaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
