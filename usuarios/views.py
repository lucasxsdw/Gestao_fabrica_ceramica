from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import authenticate, login as login_django, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404

def cadastro(request):
    if request.method == 'GET':
        return render(request, 'usuarios/cadastro.html')

    username = request.POST.get('username')
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    email = request.POST.get('email')
    password1 = request.POST.get('password1')
    password2 = request.POST.get('password2')

    if password1 != password2:
        return render(
            request,
            'usuarios/cadastro.html',
            {'erro': 'As senhas não conferem.'}
        )

    if User.objects.filter(username=username).exists():
        return render(
            request,
            'usuarios/cadastro.html',
            {'erro': 'Já existe um usuário com esse nome.'}
        )

    user = User.objects.create_user(
        username=username,
        first_name=first_name,
        last_name=last_name,
        email=email,
        password=password1
    )
    user.save()

    return redirect('index');


def login(request):
    if request.method == 'GET':
        return render(request, 'usuarios/login.html')

    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(username=username, password=password)

    if user is not None:
        login_django(request, user)
        return redirect('index')

    else:
        return render(
            request,
            'usuarios/login.html',
            {'erro': 'Usuário ou senha inválidos.'}
        )


def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
@permission_required('usuarios.view_user', raise_exception=True)
def listar(request):
    usuarios = User.objects.all()
    return render(request, 'usuarios/listar.html', {'usuarios': usuarios})

""" @login_required
def detalhar(request, id):
    usuario = get_object_or_404(User, id=id)

    return render(request, 'usuarios/detalhar.html', {'usuario': usuario}) """

@login_required
@permission_required('usuarios.change_user', raise_exception=True)
def editar(request, id):
    usuario = get_object_or_404(User, id=id)

    if request.method == 'GET':
        form = UserChangeForm(instance=usuario)
        return render(request, 'usuarios/form.html', {'form': form, 'usuario': usuario})

    form = UserChangeForm(request.POST, instance=usuario)
    if form.is_valid():
        form.save()
        return redirect('listar_usuarios')

    return render(request, 'usuarios/form.html', {'form': form, 'usuario': usuario})

@login_required
@permission_required('usuarios.delete_user', raise_exception=True)
def excluir(request, id):
    usuario = get_object_or_404(User, id=id)
    usuario.delete()
    return redirect('listar_usuarios')