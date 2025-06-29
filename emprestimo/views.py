from django.shortcuts import render, redirect, get_object_or_404
from .models import Emprestimo
from .forms import EmprestimoForm

def listar(request):
    materiais = Emprestimo.objects.all()
    return render(request, 'emprestimo/listar.html', {'materiais': materiais})

def detalhar(request, id):
    emprestimo = get_object_or_404(Emprestimo, id=id)
    return render(request, 'emprestimo/detalhar.html', {'emprestimo': emprestimo})

def adicionar(request):
    if request.method == 'POST':
        form = EmprestimoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('emprestimo:listar')
    else:
        form = EmprestimoForm()
    return render(request, 'emprestimo/form.html', {'form': form})

def editar(request, id):
    emprestimo = get_object_or_404(Emprestimo, id=id)
    if request.method == 'POST':
        form = EmprestimoForm(request.POST, instance=emprestimo)
        if form.is_valid():
            form.save()
            return redirect('emprestimo:listar')
    else:
        form = EmprestimoForm(instance=emprestimo)
    return render(request, 'emprestimo/form.html', {'form': form})

def excluir(request, id):
    emprestimo = get_object_or_404(Emprestimo, id=id)
    emprestimo.delete()
    return redirect('emprestimo:listar')
