from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Livro, Categoria

def mainapp(request):
    return render(request, 'mainapp/mainapp.html')

class Biblioteca(View):
    def get(self, request):
        livros = Livro.objects.all()
        return render(request, 'mainapp/livro_list.html', {'livros': livros})


class LivroEmDetalhe(View):
    def get(self, request, pk):
        livro = get_object_or_404(Livro, pk=pk)
        return render(request, 'mainapp/livro_detail.html', {'livro': livro})


class LivroCreateView(View):
    def get(self, request):
        categorias = Categoria.objects.all()
        return render(request, 'mainapp/livro_form.html', {'categorias':categorias})

    def post(self, request):
        titulo = request.POST.get('titulo')
        autor = request.POST.get('autor')
        anopublicado = request.POST.get('anopublicado')
        genero_id = request.POST.get('genero')
        genero = get_object_or_404(Categoria, id=genero_id)
        livro = Livro.objects.create(titulo=titulo, autor=autor, anopublicado=anopublicado, genero=genero)
        return redirect('livro_list')


class LivroUpdateView(View):
    def get(self, request, pk):
        livro = get_object_or_404(Livro, pk=pk)
        return render(request, 'mainapp/livro_form.html', {'livro': livro})

    def post(self, request, pk):
        livro = get_object_or_404(Livro, pk=pk)
        livro.titulo = request.POST.get('titulo')
        livro.autor = request.POST.get('autor')
        livro.anopublicado = request.POST.get('anopublicado')
        livro.genero=request.POST.get('genero')
        livro.save()
        return redirect('livro_list')


class LivroDeleteView(View):
    def get(self, request, pk):
        livro = get_object_or_404(Livro, pk=pk)
        return render(request, 'mainapp/livro_confirm_delete.html', {'livro': livro})

    def post(self, request, pk):
        livro = get_object_or_404(Livro, pk=pk)
        livro.delete()
        return redirect('livro_list')