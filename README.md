# 🏭 Sistema de gestão de fábrica de cerâmica

Este é um sistema web desenvolvido com Django para gerenciar uma fábrica de cerâmica. Ele permite o controle de funcionários, pagamentos, empréstimo , produção e materiais.

---

## 📋 Pré-requisitos

Certifique-se de ter o Python instalado em seu sistema:

```bash
python --version
```
---
## 🧪 Criar e ativar ambiente virtual (venv)

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

## 📦 Instalar dependências

Com o ambiente virtual ativado, instale todas as dependências listadas no arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

## ⚙️ Configurar o banco de dados

1. **Crie as tabelas no banco de dados com os seguintes comandos:**

```bash
python manage.py makemigrations
python manage.py migrate
```

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
