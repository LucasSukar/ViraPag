from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

class Categoria(models.Model):
    genero = models.CharField(max_length=100, unique=True)

    def _str_(self):
        return self.genero

class Livro(models.Model):
    STATUS_LEITURA_CHOICES = [
        ('NL', 'Não Lido'),
        ('EL', 'Em Leitura'),
        ('L', 'Lido'),
    ]
    AVALIACAO_CHOICES = [
        (0, '0 Estrelas'),
        (1, '1 Estrela'),
        (2, '2 Estrelas'),
        (3, '3 Estrelas'),
        (4, '4 Estrelas'),
        (5, '5 Estrelas'),
    ]
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    anopublicado = models.IntegerField()
    genero=models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    status_leitura=models.CharField(max_length=2, choices=STATUS_LEITURA_CHOICES, default='NL')
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='livros')
    isbn = models.CharField(max_length=13, null=True)
    in_wishlist = models.BooleanField(default=False)
    in_collection = models.BooleanField(default=True)
    avaliacao = models.IntegerField(choices=AVALIACAO_CHOICES, null=True, blank=True)
    is_favorite = models.BooleanField(default=False)
    
    def _str_(self):
        return self.titulo
    
    def comentarios(self):
        return Comentario.objects.filter(livro=self)
    
class ListaDesejos(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='lista_desejos',null=True)
    livros = models.ManyToManyField('Livro', related_name='desejado_por')

    def _str_(self):
        return f" Lista de desejos de {self.usuario}"


class BookHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book_title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    date_started = models.DateField(default=timezone.now)
    date_finished = models.DateField(blank=True, null=True)

    def _str_(self):
        return f"{self.book_title} ({self.author})"

class Comentario(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()
    data_publicacao = models.DateTimeField(default=timezone.now)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE, related_name='comentarios') 

    def _str_(self):
        return f"Comentário de {self.autor} em {self.livro}: {self.texto}"