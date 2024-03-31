from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainapp, name="mainapp"),
    path('biblioteca/', views.Biblioteca.as_view(), name='livro_list'),
    path('livro/<int:pk>/', views.LivroEmDetalhe.as_view(), name='livro_detail'),
    path('criar/', views.LivroCreateView.as_view(), name='livro_create'),
    path('atualizar/<int:pk>/', views.LivroUpdateView.as_view(), name='livro_update'),
    path('deletar/<int:pk>/', views.LivroDeleteView.as_view(), name='livro_delete'),

]