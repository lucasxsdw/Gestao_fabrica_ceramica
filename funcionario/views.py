from pyexpat.errors import messages
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from .models import Funcionario
from .forms import FuncionarioForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required  

@permission_required('funcionario.view_funcionario', raise_exception=True)
@login_required
def listar_funcionarios(request):
    funcionario = Funcionario.objects.all()
    return render(request, 'funcionario/listar.html', {'funcionarios': funcionario})


@permission_required('funcionario.add_funcionario', raise_exception=True)
@login_required
def add_Func(request):
    if request.method == 'POST':
        form = FuncionarioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Funcionário adicionado com sucesso!")
            return redirect('funcionario:listar_funcionarios')
    else:
        form = FuncionarioForm()
        
    return render(request, 'funcionario/form.html', {'form': form, 'modo': 'adicionar'})


@permission_required('funcionario.change_funcionario', raise_exception=True)
@login_required
def editar_func(request, id):
    func = get_object_or_404(Funcionario, pk=id)
    if request.method == 'POST':
        form = FuncionarioForm(request.POST, request.FILES, instance=func)
        if form.is_valid():
             form.save()
             messages.success(request, "Funcionário editado com sucesso!")
             return redirect('funcionario:listar_funcionarios')
    else:
        form = FuncionarioForm(instance=func)
    return render(request, 'funcionario/form.html', {'form': form, 'modo': 'editar'})


@permission_required('funcionario.delete_funcionario', raise_exception=True)
@login_required
def excluir_func(request, id):
    funcionario = get_object_or_404(Funcionario, pk=id)
    funcionario.delete()
    messages.success(request, "Funcionário excluído com sucesso!")
    return redirect('funcionario:listar_funcionarios')


@permission_required('funcionario.detail_funcionario', raise_exception=True)
@login_required
def detail_func(request, pk):
    funcionario = get_object_or_404(Funcionario, pk=pk)
    return render(request, 'funcionario/detalhar.html', {'funcionario': funcionario})

