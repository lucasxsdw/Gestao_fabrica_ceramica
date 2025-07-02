from django.shortcuts import render, redirect, get_object_or_404
from .models import Emprestimo
from .forms import EmprestimoForm

def listar(request):
    emprestimos = Emprestimo.objects.all()
    return render(request, 'emprestimo/listar.html', {'emprestimos': emprestimos})

def detalhar(request, id):
    emprestimo = get_object_or_404(Emprestimo, id=id)
    return render(request, 'emprestimo/detalhar.html', {'emprestimo': emprestimo})

def adicionar(request):
    if request.method == 'POST':
        form = EmprestimoForm(request.POST)
        if form.is_valid():
            emprestimo = form.save(commit=False)
            emprestimo.definir_data_devolucao()
            emprestimo.save()
            return redirect('listar_emprestimos')
    else:
        form = EmprestimoForm()
    return render(request, 'emprestimo/form.html', {'form': form})

def editar(request, id):
    emprestimo = get_object_or_404(Emprestimo, id=id)
    if request.method == 'POST':
        form = EmprestimoForm(request.POST, instance=emprestimo)
        if form.is_valid():
            emprestimo = form.save(commit=False)
            emprestimo.definir_data_devolucao()
            emprestimo.save()
            return redirect('listar_emprestimos')
    else:
        form = EmprestimoForm(instance=emprestimo)
    return render(request, 'emprestimo/form.html', {'form': form})

def excluir(request, id):
    emprestimo = get_object_or_404(Emprestimo, id=id)
    emprestimo.delete()
    return redirect('listar_emprestimos')
