from django import forms
from .models import Autor, Livro

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nome', 'data_nascimento']

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['titulo', 'ano_publicacao', 'autor']
