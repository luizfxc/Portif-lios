# portifolio/forms.py

from django import forms
from .models import Projeto, Tecnologia, ImagemProjeto

# ===============================================
# Formulário para o Modelo Projeto
# ===============================================

class ProjetoForm(forms.ModelForm):
    """
    Formulário para criar e editar projetos.
    Usa ModelForm para campos automáticos e adiciona widgets para estilização.
    """
    class Meta:
        model = Projeto
        # Inclui todos os campos de texto e o ManyToManyField 'tecnologias'
        fields = ['titulo', 'descricao', 'link', 'tecnologias'] 
        
        # Adiciona widgets para controle de aparência (usando classes Bootstrap)
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'link': forms.URLInput(attrs={'class': 'form-control'}),
            # O campo ManyToMany (tecnologias) geralmente é renderizado como CheckboxSelectMultiple
            # Você pode usar SelectMultiple se preferir uma caixa de seleção.
            'tecnologias': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

# -----------------------------------------------

# ===============================================
# Formulário para o Modelo Tecnologia (CRUD de Tecnologias)
# ===============================================

class TecnologiaForm(forms.ModelForm):
    """
    Formulário simples para criar e editar objetos Tecnologia.
    """
    class Meta:
        model = Tecnologia
        fields = ['nome']
        
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
        }

# -----------------------------------------------

# ===============================================
# Formulário para o Modelo ImagemProjeto (Upload de Imagens)
# 🛑 ESSENCIAL para a view imagem_criar
# ===============================================

class ImagemProjetoForm(forms.ModelForm):
    """
    Formulário para o upload de uma nova imagem e sua legenda.
    """
    class Meta:
        model = ImagemProjeto
        # Não inclui 'projeto' aqui, pois é definido na view.
        fields = ['imagem', 'legenda']
        
        widgets = {
            # É importante usar FileInput para campos de upload
            'imagem': forms.FileInput(attrs={'class': 'form-control'}),
            'legenda': forms.TextInput(attrs={'class': 'form-control'}),
        }