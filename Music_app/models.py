from django.db import models

# Create your models here.

class Music(models.Model):
    nome = models.CharField(max_length=150)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class Partitura(models.Model):
    music = models.ForeignKey(Music, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)