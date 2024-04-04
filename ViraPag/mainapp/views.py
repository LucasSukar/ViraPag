from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Livro, Categoria
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.models import User

class HomeView(View):
    def get(self, request):
        return render(request, 'mainapp/home.html')
    
class CadastroView():
    def get(self, request):
        return render(request, 'mainapp/cadastro.html')
    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')  
        password = request.POST.get('password')

        if not username or not password:
            return render(request, 'mainapp/cadastro.html', {
                'error': 'Usuário e senha são campos obrigatórios.'
            })

        if User.objects.filter(username=username).exists():
            return render(request, 'mainapp/cadastro.html', {
                'error': 'Nome de usuário já existe.'
            })

        user = User(username=username, email=email)
        user.password = password  
        user.save()
        return redirect('login')  

class LoginView(LoginView):
    template_name = 'mainapp/login.html'  
    redirect_authenticated_user = True  
    next_page = reverse_lazy('home')

class Biblioteca(LoginRequiredMixin,View):
    def get(self, request):
        livros = Livro.objects.all()
        return render(request, 'mainapp/biblioteca.html', {'livros': livros})


class LivroEmDetalhe(LoginRequiredMixin,View):
    def get(self, request, pk):
        livro = get_object_or_404(Livro, pk=pk)
        return render(request, 'mainapp/livro_detail.html', {'livro': livro})


class LivroCreateView(LoginRequiredMixin,View):
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
        return redirect('biblioteca')


class LivroUpdateView(LoginRequiredMixin,View):
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
        return redirect('biblioteca')


class LivroDeleteView(LoginRequiredMixin,View):
    def get(self, request, pk):
        livro = get_object_or_404(Livro, pk=pk)
        return render(request, 'mainapp/livro_confirm_delete.html', {'livro': livro})

    def post(self, request, pk):
        livro = get_object_or_404(Livro, pk=pk)
        livro.delete()
        return redirect('biblioteca')