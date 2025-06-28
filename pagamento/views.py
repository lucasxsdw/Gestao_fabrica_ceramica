from django.shortcuts import render, redirect, get_object_or_404
from .models import Pagamento
from .forms import PagamentoForm

def pagamento_list(request):
    pagamentos = Pagamento.objects.all()
    return render(request, 'pagamento/list.html', {'pagamentos': pagamentos})

def pagamento_create(request):
    form = PagamentoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('pagamento_list')
    return render(request, 'pagamento/form.html', {'form': form})

def pagamento_update(request, pk):
    pagamento = get_object_or_404(Pagamento, pk=pk)
    form = PagamentoForm(request.POST or None, instance=pagamento)
    if form.is_valid():
        form.save()
        return redirect('pagamento_list')
    return render(request, 'pagamento/form.html', {'form': form})

def pagamento_delete(request, pk):
    pagamento = get_object_or_404(Pagamento, pk=pk)
    if request.method == "POST":
        pagamento.delete()
        return redirect('pagamento_list')
    return render(request, 'pagamento/confirm_delete.html', {'object': pagamento})
