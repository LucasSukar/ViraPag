from django.db import models
class Categoria(models.Model):
    genero = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.genero

class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    anopublicado = models.IntegerField()
    genero=models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.titulo
    

