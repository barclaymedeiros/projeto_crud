from django.shortcuts import render, redirect, get_object_or_404
from .models import Filme
from .forms import FilmeForm

def lista_filmes(request):
    filmes = Filme.objects.all()
    return render(request, 'core/lista_de_filmes.html', {'filmes': filmes})

def salvar_filme(request):
    if request.method == 'POST':
        form = FilmeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:lista-filmes')
    else:
        form = FilmeForm()
    return render(request, 'core/salvar_filme.html', {'form': form})

def excluir_filme(request, filme_id):
    filme = get_object_or_404(Filme, pk=filme_id)
    filme.delete()
    return redirect('core:lista-filmes')

def atualizar_filme(request, filme_id):
    filme = get_object_or_404(Filme, pk=filme_id)
    if request.method == 'POST':
        form = FilmeForm(request.POST, instance=filme)
        if form.is_valid():
            form.save()
            return redirect('core:lista-filmes')
    else:
        form = FilmeForm(instance=filme)
    return render(request, 'core/atualizar_filme.html', {'form': form})