from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.lista_autores, name='lista_autores'), 
    path('<int:pk>/', views.detalhe_autor, name='detalhe_autor'),
    path('novo/', views.criar_autor, name='criar_autor'),
    path('<int:pk>/editar/', views.editar_autor, name='editar_autor'),
    path('<int:pk>/excluir/', views.excluir_autor, name='excluir_autor'),

    
    path('livros/', views.lista_livros, name='lista_livros'),
    path('livros/<int:pk>/', views.detalhe_livro, name='detalhe_livro'),
    path('livros/novo/', views.criar_livro, name='criar_livro'),
    path('livros/<int:pk>/editar/', views.editar_livro, name='editar_livro'),
    path('livros/<int:pk>/excluir/', views.excluir_livro, name='excluir_livro'),
]
