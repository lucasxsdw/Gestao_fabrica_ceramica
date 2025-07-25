"""
URL configuration for gestao_fabrica_ceramica project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from gestao_fabrica_ceramica import settings
from django.conf.urls.static import static


from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('funcionario/', include('funcionario.urls')),
    path('pagamento/', include('pagamento.urls')),
    path('material/', include('material.urls')),
    path('emprestimo/', include('emprestimo.urls')),
    path('auth/', include('usuarios.urls')),
    path('produto/', include('produto.urls')),
    path('producao/', include('producao.urls')),
]