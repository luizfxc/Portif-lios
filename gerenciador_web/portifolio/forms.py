# portifolio/forms.py

from django import forms
from .models import Projeto, Tecnologia, ImagemProjeto

# ===============================================
# Formulário para o Modelo Projeto
# ===============================================

class ProjetoForm(forms.ModelForm):
    """
    Cria um formulário automaticamente a partir do modelo Projeto.
    Isto facilita a gestão dos campos (CRUD).
    """
    class Meta:
        model = Projeto
        # 🛑 Usamos 'tecnologias' no ManyToManyField se tiver aceitado a sugestão. 
        # Caso contrário, use 'tecnologia' (singular)
        fields = ['titulo', 'descricao', 'link', 'tecnologias'] 
        
        # Opcional: Adicionar classes CSS ou ajuda extra aos campos
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 4}),
        }

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