from pyexpat.errors import messages
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from .models import Funcionario
from .forms import FuncionarioForm
from django.contrib import messages



def listar_funcionarios(request):
    funcionario = Funcionario.objects.all()
    return render(request, 'funcionario/listar.html', {'funcionarios': funcionario})


def add_Func(request):
    if request.method == 'POST':
        form = FuncionarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('funcionario:listar_funcionarios')
    else:
        form = FuncionarioForm()
        
    return render(request, 'funcionario/form.html', {'form': form, 'modo': 'adicionar'})


def editar_func(request, id):
    func = get_object_or_404(Funcionario, pk=id)
    if request.method == 'POST':
        form = FuncionarioForm(request.POST, instance=func)
        if form.is_valid():
             form.save()
             return redirect('funcionario:listar_funcionarios')
    else:
        form = FuncionarioForm(instance=func)
    return render(request, 'funcionario/form.html', {'form': form, 'modo': 'editar'})



def excluir_func(request, id):
    funcionario = get_object_or_404(Funcionario, pk=id)
    funcionario.delete()
    messages.success(request, "Funcionário excluído com sucesso!")
    return redirect('funcionario:listar_funcionarios')

    

    
def detail_func(request, pk):
    funcionario = get_object_or_404(Funcionario, pk=pk)
    return render(request, 'funcionario/detalhar.html', {'funcionario': funcionario})

