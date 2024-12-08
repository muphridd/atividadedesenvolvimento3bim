from django.shortcuts import render, get_object_or_404, redirect
from .models import Autor, Livro
from .forms import AutorForm, LivroForm

# pagina inicial
def pagina_inicial(request):
    return render(request, 'livros/pagina_inicial.html')

# autor - crud 
def lista_autores(request):
    autores = Autor.objects.all()
    return render(request, 'livros/autor_list.html', {'autores': autores})

def detalhe_autor(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    return render(request, 'livros/autor_detail.html', {'autor': autor})

def criar_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_autores')
    else:
        form = AutorForm()
    return render(request, 'livros/autor_form.html', {'form': form})

def editar_autor(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == 'POST':
        form = AutorForm(request.POST, instance=autor)
        if form.is_valid():
            form.save()
            return redirect('lista_autores')
    else:
        form = AutorForm(instance=autor)
    return render(request, 'livros/autor_form.html', {'form': form})

def excluir_autor(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == 'POST':
        autor.delete()
        return redirect('lista_autores')
    return render(request, 'livros/autor_confirm_delete.html', {'autor': autor})

# livro crud
def lista_livros(request):
    livros = Livro.objects.all()
    return render(request, 'livros/livro_list.html', {'livros': livros})

def detalhe_livro(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    return render(request, 'livros/livro_detail.html', {'livro': livro})

def criar_livro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_livros')
    else:
        form = LivroForm()
    return render(request, 'livros/livro_form.html', {'form': form})

def editar_livro(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    if request.method == 'POST':
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            form.save()
            return redirect('lista_livros')
    else:
        form = LivroForm(instance=livro)
    return render(request, 'livros/livro_form.html', {'form': form})

def excluir_livro(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    if request.method == 'POST':
        livro.delete()
        return redirect('lista_livros')
    return render(request, 'livros/livro_confirm_delete.html', {'livro': livro})
