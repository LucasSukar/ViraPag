from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Livro, Categoria
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.db.models import Count
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator



class HomeView(View):
    def get(self, request):
        contexto = {}
        if request.user.is_authenticated:
            total_livros = Livro.objects.count()
            generos_ordenados = Livro.objects.values('genero__genero').annotate(total=Count('genero')).order_by('-total')
            if generos_ordenados:
                
                maior_contagem = generos_ordenados.first()['total']
                menor_contagem = generos_ordenados.last()['total']

                
                generos_mais_comuns = generos_ordenados.filter(total=maior_contagem)
                generos_menos_comuns = generos_ordenados.filter(total=menor_contagem)

                generos_mais_comuns_nomes = [g['genero__genero'] for g in generos_mais_comuns]
                generos_menos_comuns_nomes = [g['genero__genero'] for g in generos_menos_comuns]

                contexto['genero_mais_comum'] = ', '.join(generos_mais_comuns_nomes)
                contexto['genero_menos_comum'] = ', '.join(generos_menos_comuns_nomes)
            else:
                contexto['genero_mais_comum'] = 'Indisponível'
                contexto['genero_menos_comum'] = 'Indisponível'

            contexto['total_livros'] = total_livros

        return render(request, 'mainapp/home.html', contexto)
    
class CadastroView(View):
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
        user.set_password(password)
        user.save()
        return redirect('login')  

class LoginView(LoginView):
    template_name = 'mainapp/login.html'  
    redirect_authenticated_user = True  
    next_page = reverse_lazy('home')
   
    
class LogoutView(View):
    @method_decorator(csrf_protect)
    def post(self, request):
        logout(request)
        return redirect('home')

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
    
