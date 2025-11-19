from django.db import models


class Tecnologia(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome



class Projeto(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    link = models.CharField(max_length=300, blank=True, null=True)

    tecnologia = models.ForeignKey(
        Tecnologia,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.titulo



class ImagemProjeto(models.Model):
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)
    imagem = models.CharField(max_length=300)   # mantendo simples como no modelo original
    legenda = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.legenda if self.legenda else "Imagem"
