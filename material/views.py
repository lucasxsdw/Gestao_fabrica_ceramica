from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Material
from .forms import MaterialForm
from django.contrib.auth.decorators import login_required

@login_required
def listar(request):
    materiais = Material.objects.all()
    return render(request, 'material/listar.html', {'materiais': materiais})

@login_required
def detalhar(request, id):
    material = get_object_or_404(Material, id=id)
    return render(request, 'material/detalhar.html', {'material': material})

@login_required
def adicionar(request):
    if request.method == 'POST':
        form = MaterialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_materiais')
    else:
        form = MaterialForm()
    return render(request, 'material/form.html', {'form': form})

@login_required
def editar(request, id):
    material = get_object_or_404(Material, id=id)
    if request.method == 'POST':
        form = MaterialForm(request.POST, instance=material)
        if form.is_valid():
            form.save()
            return redirect('listar_materiais')
    else:
        form = MaterialForm(instance=material)
    return render(request, 'material/form.html', {'form': form})

@login_required
def excluir(request, id):
    material = get_object_or_404(Material, id=id)
    material.delete()
    return redirect('listar_materiais')

@login_required
def obter_dias_emprestimo(request, id):
    material = get_object_or_404(Material, id=id)
    quantidade_dias = material.dias_de_emprestimo
    contexto = {'quantidade_dias': quantidade_dias}
    return JsonResponse(contexto)