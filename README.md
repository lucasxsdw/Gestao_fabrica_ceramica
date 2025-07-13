# 🏭 Sistema de gestão de fábrica de cerâmica

Desenvolvido por: [Lucas Ryan](https://github.com/lucasxsdw), [Natan Frota](https://github.com/natanfrota) e [Sancho Augusto](https://github.com/SanchoArruda).

Este sistema web desenvolvido com Bootstrap e Django tem o objetivo de informatizar o gerenciamento de uma fábrica de cerâmica, substituindo controles manuais em papel por um sistema digital. Ele permite administrar de forma mais eficiente os dados relacionados a funcionários, pagamentos, materiais, empréstimos, produtos e produção.

---

## 📋 Pré-requisitos

Certifique-se de ter o Python instalado em seu sistema:

```bash
python --version
```
---
## 🧪 Criar e ativar o ambiente virtual (venv)

1. Clone o repositório e crie o ambiente virtual na raiz do projeto:

```bash
python -m venv venv
```

2. Ative o ambiente virtual:

- **Linux/macOS:**
```bash
source venv/bin/activate
```

- **Windows:**
```bash
venv\Scripts\activate
```

---

## 📦 Instalar as dependências

Com o ambiente virtual ativado, instale todas as dependências listadas no arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

## ⚙️ Configurar o banco de dados

Crie as tabelas no banco de dados com os seguintes comandos:

```bash
python manage.py makemigrations funcionario material pagamento producao produto emprestimo
python manage.py migrate
```

---

## 👤 Criar o primeiro usuário (superusuário)

Antes de acessar o sistema, é necessário criar um usuário administrador para gerenciar os dados:

```bash
python manage.py createsuperuser
```

Siga as instruções na linha de comando para definir o nome de usuário, e-mail (opcional) e senha. Após isso, você poderá fazer login no sistema.

---


## 🚀 Executar o servidor de desenvolvimento

Com tudo configurado, execute o servidor local:

```bash
python manage.py runserver
```

Acesse o sistema através do navegador no seguinte endereço:

```
http://127.0.0.1:8000/
```

---

## 🎥 Demonstração em vídeo
Uma demonstração do sistema em funcionamento está disponível no [YouTube](https://youtu.be/79H8R3laky0).
