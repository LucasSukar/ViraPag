from django.urls import path
from . import views

urlpatterns = [
    path('',views.HomeView.as_view(),name='home' ),
    path('cadastro/',views.CadastroView.as_view(),name='cadastro'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('biblioteca/', views.Biblioteca.as_view(), name='livro_list'),
    path('livro/<int:pk>/', views.LivroEmDetalhe.as_view(), name='livro_detail'),
    path('criar/', views.LivroCreateView.as_view(), name='livro_create'),
    path('atualizar/<int:pk>/', views.LivroUpdateView.as_view(), name='livro_update'),
    path('deletar/<int:pk>/', views.LivroDeleteView.as_view(), name='livro_delete'),
    path('lista_desejo/', views.IndexView.as_view(), name='desejo'),
]