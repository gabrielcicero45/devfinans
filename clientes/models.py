from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email =models.EmailField(max_length=100)
    senha =models.CharField(max_length=10, default=' ')
    def __str__(self):
        return self.nome


        