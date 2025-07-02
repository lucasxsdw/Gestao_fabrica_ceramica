from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as login_django, logout
from django.contrib.auth.decorators import login_required


def cadastro(request):
    if request.method == 'GET':
        return render(request, 'usuarios/cadastro.html')

    username = request.POST.get('username')
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    email = request.POST.get('email')
    password1 = request.POST.get('password1')
    password2 = request.POST.get('password2')

    # Verifica se as senhas conferem
    if password1 != password2:
        return render(
            request,
            'usuarios/cadastro.html',
            {'erro': 'As senhas não conferem.'}
        )

# Verifica se o usuário já existe
    if User.objects.filter(username=username).exists():
        return render(
            request,
            'usuarios/cadastro.html',
            {'erro': 'Já existe um usuário com esse nome.'}
        )

# Cria o usuário
    user = User.objects.create_user(
        username=username,
        first_name=first_name,
        last_name=last_name,
        email=email,
        password=password1
    )
    user.save()

    return HttpResponse('Usuário cadastrado com sucesso!')


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
    logout(request)          # Django limpa auth_user_id
    return redirect('login')