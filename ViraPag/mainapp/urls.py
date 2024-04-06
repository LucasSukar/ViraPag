from django.urls import path
from . import views



urlpatterns = [
    path('',views.HomeView.as_view(),name='home' ),
    path('cadastro/',views.CadastroView.as_view(),name='cadastro'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('biblioteca/', views.Biblioteca.as_view(), name='biblioteca'),
    path('biblioteca/livro/<int:pk>/', views.LivroEmDetalhe.as_view(), name='livro_detail'),
    path('criarlivro/', views.LivroCreateView.as_view(), name='livro_create'),
    path('atualizar/<int:pk>/', views.LivroUpdateView.as_view(), name='livro_update'),
    path('livro/deletar/<int:pk>/', views.LivroDeleteView.as_view(), name='livro_delete'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('lista_desejos/', views.ListaDesejosView.as_view(), name='lista_desejos'),
    path('perfil/', views.PerfilView.as_view(), name='perfil'),
    
]