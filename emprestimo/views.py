from django.shortcuts import render, redirect, get_object_or_404
from .models import Emprestimo
from .forms import EmprestimoForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def listar(request):
    emprestimos = Emprestimo.objects.all()
    return render(request, 'emprestimo/listar.html', {'emprestimos': emprestimos})

@login_required
def detalhar(request, id):
    emprestimo = get_object_or_404(Emprestimo, id=id)
    return render(request, 'emprestimo/detalhar.html', {'emprestimo': emprestimo})

@login_required
def adicionar(request):
    if request.method == 'POST':
        form = EmprestimoForm(request.POST)
        if form.is_valid():
            emprestimo = form.save(commit=False)
            emprestimo.definir_data_devolucao()
            emprestimo.save()
            messages.success(request, "Empréstimo adicionado com sucesso!")
            return redirect('listar_emprestimos')
    else:
        form = EmprestimoForm()
    return render(request, 'emprestimo/form.html', {'form': form})

@login_required
def editar(request, id):
    emprestimo = get_object_or_404(Emprestimo, id=id)
    if request.method == 'POST':
        form = EmprestimoForm(request.POST, instance=emprestimo)
        if form.is_valid():
            emprestimo = form.save(commit=False)
            emprestimo.definir_data_devolucao()
            emprestimo.save()
            messages.success(request, "Empréstimo editado com sucesso!")
            return redirect('listar_emprestimos')
    else:
        form = EmprestimoForm(instance=emprestimo)
    return render(request, 'emprestimo/form.html', {'form': form})

@login_required
def excluir(request, id):
    emprestimo = get_object_or_404(Emprestimo, id=id)
    emprestimo.delete()
    messages.success(request, "Empréstimo excluído com sucesso!")
    return redirect('listar_emprestimos')
