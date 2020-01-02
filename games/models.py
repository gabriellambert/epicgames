from django.db import models


class Jogo(models.Model):
    mandatario = models.CharField(max_length=20)
    visitante = models.CharField(max_length=20)
    torneio = models.CharField(max_length=30)
    ano = models.IntegerField()
    imagem = models.ImageField(upload_to='fotos/%d/%m/%Y', blank=True, default='')

    def __str__(self):
        return self.mandatario + ' x ' + self.visitante
