from django.db import models

class criar(models.Model):
    titulo = models.CharField(max_length = 100)
    descricao = models.TextField()
    autor = models.CharField(max_length = 100)
    preco = models.DecimalField(max_digits = 10, decimal_places = 2)
    genero = models.CharField(max_length = 100)
    
    class Meta:
        verbose_name_plural = 'criar'

    def __str__(self):
        return self.titulo
