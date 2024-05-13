from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import logout, update_session_auth_hash
from django.db.models import Count, F
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
from django.contrib import messages
from .models import Livro, Categoria, ListaDesejos, BookHistory, Comentario
from django.contrib.auth.hashers import make_password
from .utils import fetch_book_info_by_title
from django.utils import timezone
from django.http import HttpResponseRedirect

class HomeView(View):
    def get(self, request):
        contexto = {'user': request.user if request.user.is_authenticated else None}
        if request.user.is_authenticated:
            livros_usuario = Livro.objects.filter(usuario=request.user)
            total_livros = livros_usuario.count()
            generos_ordenados = livros_usuario.values('genero__genero').annotate(total=Count('genero')).order_by('-total')

            if generos_ordenados:
                generos_mais_comuns = generos_ordenados.filter(total=generos_ordenados.first()['total'])
                generos_menos_comuns = generos_ordenados.filter(total=generos_ordenados.last()['total'])

                contexto['genero_mais_comum'] = ', '.join([g['genero__genero'] for g in generos_mais_comuns])
                contexto['genero_menos_comum'] = ', '.join([g['genero__genero'] for g in generos_menos_comuns])
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

class Biblioteca(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('home')
        else:
            # Obtém todos os livros do usuário, ordenados pelo status de favorito
            livros = Livro.objects.filter(usuario=request.user, in_collection=True).order_by(F('is_favorite').desc(nulls_last=True))
            
            # Atualiza as URLs das capas dos livros, se disponíveis
            for livro in livros:
                book_info = fetch_book_info_by_title(livro.titulo)
                if book_info:
                    livro.cover_url = book_info.get('cover_url')
            
            return render(request, 'mainapp/biblioteca.html', {'livros': livros})
        
class LivroEmDetalhe(LoginRequiredMixin, View):
    def get(self, request, pk):
        livro = get_object_or_404(Livro, pk=pk)
        book_info = None
       
        if not livro.isbn:
            book_info = fetch_book_info_by_title(livro.titulo)
            if book_info:
                livro.isbn = book_info.get('isbn')
                livro.cover_url = book_info.get('cover_url')
                livro.save()
            else:
                livro.cover_url = book_info.get('cover_url') if livro.isbn else None
        
        
        comentarios = Comentario.objects.filter(livro=livro)
        
        return render(request, 'mainapp/livro_detail.html', {'livro': livro, 'comentarios': comentarios})



class LivroCreateView(LoginRequiredMixin, View):
    def get(self, request):
        categorias = Categoria.objects.all()
        return render(request, 'mainapp/livro_form.html', {'categorias': categorias})

    def post(self, request):
        titulo = request.POST.get('titulo').strip()
        autor = request.POST.get('autor').strip()
        anopublicado = request.POST.get('anopublicado').strip()
        genero_id = request.POST.get('genero').strip()
        
        if not titulo or not autor or not anopublicado:
            messages.error(request, 'Todos os campos são obrigatórios.')
            return redirect('livro_create')

        if Livro.objects.filter(titulo__iexact=titulo, usuario=request.user).exists():
            messages.error(request, 'Um livro com este nome já existe na sua biblioteca.')
            return redirect('livro_create')

        genero = get_object_or_404(Categoria, id=genero_id)
        Livro.objects.create(titulo=titulo, autor=autor, anopublicado=anopublicado, genero=genero, usuario=request.user)
        messages.success(request, 'Livro adicionado com sucesso!')
        return redirect('biblioteca')


class LivroUpdateView(LoginRequiredMixin, View):
    def get(self, request, pk):
        livro = get_object_or_404(Livro, pk=pk)
        status_leitura = livro.status_leitura
        return render(request, 'mainapp/livro_update.html', {'livro': livro, 'categorias': Categoria.objects.all(), 'status_leitura': status_leitura})

    def post(self, request, pk):
        livro = get_object_or_404(Livro, pk=pk)
        livro.titulo = request.POST.get('titulo')
        livro.autor = request.POST.get('autor')
        livro.anopublicado = request.POST.get('anopublicado')
        livro.genero = get_object_or_404(Categoria, pk=request.POST.get('genero'))
        novo_status_leitura = request.POST.get('status_leitura')

        if livro.status_leitura != 'NL' and novo_status_leitura == 'NL':
            if BookHistory.objects.filter(user=request.user, book_title=livro.titulo, author=livro.autor).exists():
                BookHistory.objects.filter(user=request.user, book_title=livro.titulo, author=livro.autor).delete()
                messages.success(request, 'Livro editado com sucesso!')

        elif novo_status_leitura in ['L', 'EL']:
            if not BookHistory.objects.filter(user=request.user, book_title=livro.titulo, author=livro.autor).exists():
                BookHistory.objects.create(
                    user=request.user,
                    book_title=livro.titulo,
                    author=livro.autor,
                )
                messages.success(request, 'Livro editado com sucesso!')

        livro.status_leitura = novo_status_leitura

        if livro.status_leitura != 'L':
            livro.avaliacao = None

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

class PerfilView(LoginRequiredMixin,View):
    def get(self, request):
        if not request.user.is_authenticated:
            
            return redirect('home')
        else:
            usuario=request.user.username
            email=request.user.email
            context = {'usuario': usuario, 'email': email}
            return render(request, 'mainapp/perfil.html', context)

class MudarSenhaView(LoginRequiredMixin, View):

    def get(self, request):
        return render(request, 'mainapp/mudar_senha.html')

    def post(self, request):
        senha_antiga = request.POST.get('senha_antiga')
        nova_senha = request.POST.get('nova_senha')
        confirmar = request.POST.get('confirmar')

        if not request.user.check_password(senha_antiga):
            messages.error(request, 'Sua senha antiga foi digitada errado. Tente novamente.')
        elif nova_senha != confirmar:
            messages.error(request, 'Por favor, digite sua senha nova igual ao escrito no primeiro campo.')
        else:
            request.user.password = make_password(nova_senha)
            request.user.save()
            update_session_auth_hash(request, request.user)  
            messages.success(request, 'Sua senha foi atualizada com sucesso!')
            return redirect('home')

        return render(request, 'mainapp/mudar_senha.html')
    
class AddListaDesejosView(LoginRequiredMixin, View):
    def get(self, request):
        categorias = Categoria.objects.all()
        return render(request, 'mainapp/add_lista.html', {'categorias': categorias})

    def post(self, request):
        titulo = request.POST.get('titulo').strip()
        autor = request.POST.get('autor').strip()
        anopublicado = request.POST.get('anopublicado').strip()
        genero_id = request.POST.get('genero').strip()
        
        if not titulo or not autor or not anopublicado:
            messages.error(request, 'Todos os campos são obrigatórios.')
            return redirect('livro_create')

        genero = get_object_or_404(Categoria, id=genero_id)
        
        
        livro = Livro(titulo=titulo, autor=autor, anopublicado=anopublicado, genero=genero, in_wishlist=True, in_collection=False,usuario=request.user)
        livro.save()
        
       
        wishlist, created = ListaDesejos.objects.get_or_create(usuario=request.user)
        wishlist.livros.add(livro)  
        
        messages.success(request, "Livro adicionado à lista de desejos com sucesso.")
        return redirect('lista_desejos')
        
        

class ListaDesejosView(LoginRequiredMixin, View):
    def get(self, request):
        wishlist, created = ListaDesejos.objects.get_or_create(usuario=request.user)
        livros_desejados = wishlist.livros.all()
        return render(request, 'mainapp/lista_desejos.html', {'livros_desejados': livros_desejados})    

class RemoverDaListaView(LoginRequiredMixin, View):
    def post(self, request,**kwargs):
        livro_id = kwargs.get('livro_id')
        livro = get_object_or_404(Livro, id=livro_id)
        wishlist = ListaDesejos.objects.get(usuario=request.user)
        wishlist.livros.remove(livro)
        livro.delete()
        messages.success(request, "Livro removido da lista de desejos com sucesso.")
        return redirect('lista_desejos')
    
class AddParaColecaoView(LoginRequiredMixin, View):
    def post(self, request, livro_id):
        livro = get_object_or_404(Livro, id=livro_id, usuario=request.user)
        livro.in_wishlist = False
        livro.in_collection = True
        livro.save()
        
        wishlist = ListaDesejos.objects.filter(usuario=request.user).first()
        if wishlist:
            wishlist.livros.remove(livro)

        messages.success(request, "Livro adicionado à coleção com sucesso.")
        return redirect('lista_desejos')  
    

class BookHistoryView(LoginRequiredMixin, View):
    def get(self, request):
        book_history = BookHistory.objects.filter(user=request.user)
        return render(request, 'mainapp/book_history.html', {'book_history': book_history})

    def post(self, request, livro_id):
        livro = get_object_or_404(Livro, id=livro_id, usuario=request.user)
        BookHistory.objects.create(
            user=request.user,
            book_title=livro.titulo,
            author=livro.autor,
            date_started=livro.date_added,
            date_finished=timezone.now()
        )
        livro.delete()      
        return redirect('book_history')
    
class RemoveFromHistoryView(View):
    def post(self, request, livro_id):
        book = get_object_or_404(BookHistory, pk=livro_id, user=request.user)
        book.delete()
        messages.success(request, "Livro removido do histórico.")
        return redirect('book_history')


class AdicionarComentarioView(LoginRequiredMixin, View):
    def get(self, request, livro_id):
        livro = get_object_or_404(Livro, id=livro_id)
        return render(request, 'mainapp/adicionar_comentario.html', {'livro': livro})

    def post(self, request, livro_id):
        texto = request.POST.get('texto').strip()
        livro = get_object_or_404(Livro, id=livro_id)

        if not texto:
            messages.error(request, 'Por favor, adicione um texto ao comentário.')
            return redirect('adicionar_comentario', livro_id=livro_id)

        Comentario.objects.create(autor=request.user, texto=texto, livro=livro)
        messages.success(request, 'Comentário adicionado com sucesso.')
        return redirect('livro_detail', pk=livro_id)

class DeletarComentarioView(LoginRequiredMixin, View):
    def post(self, request, comentario_id):
        comentario = get_object_or_404(Comentario, id=comentario_id)
        comentario.delete()
        messages.success(request, 'Comentário removido com sucesso.')
        return redirect('livro_detail', pk=comentario.livro.id)
    
class AvaliacaoLivroView(LoginRequiredMixin, View):
    def get(self, request, livro_id):
        livro = Livro.objects.get(pk=livro_id)
        return render(request, 'mainapp/avaliacao.html', {'livro': livro})
    
    def post(self, request, livro_id):
        livro = Livro.objects.get(pk=livro_id)
        avaliacao = int(request.POST.get('avaliacao'))
        
        if livro.avaliacao:
            livro.avaliacao = avaliacao

        else:
            livro.avaliacao = avaliacao
        
        livro.save()
        return redirect('livro_detail', pk=livro_id)

class AdicionarFavoritoView(LoginRequiredMixin, View):
    def post(self, request, livro_id):
        livro = get_object_or_404(Livro, id=livro_id, usuario=request.user)
        
        if livro.is_favorite:
            livro.is_favorite = False
        else:
            livro.is_favorite = True
        
        livro.save()
        return HttpResponseRedirect(reverse('livro_detail', kwargs={'pk': livro_id}))