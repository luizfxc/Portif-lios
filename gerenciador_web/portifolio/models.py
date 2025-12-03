from django.db import models
from django.urls import reverse 


class Tecnologia(models.Model):
    """Modelo para as tecnologias/habilidades usadas."""
    nome = models.CharField(max_length=100, unique=True) 

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name_plural = "Tecnologia"


class Projeto(models.Model):
    """Modelo principal para o Projeto de Portfólio."""
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
   
    link = models.URLField(max_length=300, blank=True, null=True)

   
    tecnologias = models.ManyToManyField(
        Tecnologia,
        blank=True, 
        related_name='projetos'
    )
    
    class Meta:
        ordering = ['-data_criacao'] 
    def __str__(self):
        return self.titulo
    
   
    def get_absolute_url(self):
        return reverse('portifolio:detalhe_projeto', args=[str(self.id)])


class ImagemProjeto(models.Model):
    """Modelo para as imagens associadas a um projeto."""
    projeto = models.ForeignKey(
        Projeto, 
        on_delete=models.CASCADE,
        related_name='imagens' 
    )
   
    imagem = models.ImageField(upload_to='projetos/galeria/')
    legenda = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"Imagem de {self.projeto.titulo}" if self.projeto else "Imagem sem Projeto"
    
    