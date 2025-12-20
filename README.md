# 🌈 Desafio Back-end – Lacrei Saúde

API RESTful para **Gerenciamento de Consultas Médicas**, desenvolvida com foco em **qualidade de código, segurança, boas práticas e preparação para produção**, conforme o desafio técnico da **Lacrei Saúde**.

Este projeto visa apoiar a construção de soluções que ampliam o acesso à saúde inclusiva e de qualidade para a comunidade LGBTQIAPN+ 💙.

---

## 🧠 Visão Geral

A API permite:

- Cadastro e gerenciamento de **profissionais da saúde**
- Cadastro e gerenciamento de **consultas médicas**
- Associação de consultas a profissionais
- Busca de consultas pelo **ID do profissional**
- Autenticação, validação e sanitização de dados
- Documentação automática da API (Swagger / Redoc)
- Execução via Docker e pronta para deploy em cloud (AWS)

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.12**
- **Django 6 + Django REST Framework**
- **PostgreSQL**
- **Poetry** (gerenciamento de dependências)
- **Docker & Docker Compose**
- **GitHub Actions** (CI/CD)
- **Swagger / Redoc** (documentação da API)

---

## 📦 Estrutura do Projeto

```
backend_lacrei/
├── app
├── appointments
├── professionals
├── docker-compose.yml
├── Dockerfile
├── pyproject.toml
├── poetry.lock
└── README.md
```

---
## ⚙️ Setup do Projeto (Local)
1️⃣ Clonar o repositório:

- git clone https://github.com/seu-usuario/backend_lacrei.git
cd backend_lacrei

2️⃣ Instalar dependências:
- poetry install

3️⃣ Ativar ambiente virtual:
- poetry shell

4️⃣ Criar arquivo de variáveis de ambiente:
- DEBUG=True
- SECRET_KEY=sua_secret_key
- DATABASE_URL=postgres://postgres:postgres@localhost:5432/lacrei

5️⃣ Executar migrações:
- python manage.py migrate

6️⃣ Criar superusuário:
- python manage.py createsuperuser

7️⃣ Subir servidor:
- python manage.py runserver

API disponível em:
- http://localhost:8000
---

---
## 🐳 Setup com Docker (Recomendado)
Subir containers:
- docker compose up --build

Executar migrações:
- docker compose exec lacrei_api python manage.py migrate

Criar superusuário:
- docker compose exec lacrei_api python manage.py createsuperuser

Acessos
API:      http://localhost:8000
Swagger:  http://localhost:8000/api/schema/swagger-ui/
Redoc:    http://localhost:8000/api/schema/redoc/

---

---
## 🔐 Segurança

Validação e sanitização de dados via serializers

Proteção contra SQL Injection (ORM Django)

Autenticação via Token/JWT

CORS configurado

Variáveis sensíveis via .env

Logs de erros e acessos
---

---
## 📚 Endpoints Principais
Profissionais:
- GET    /api/professionals/
- POST   /api/professionals/
- PUT    /api/professionals/{id}/
- DELETE /api/professionals/{id}/

Consultas:
- GET  /api/appointments/
- POST /api/appointments/
- GET  /api/appointments/professional/{professional_id}/
---

---
## 🧪 Testes Automatizados
Executar testes localmente:
- python manage.py test

Executar testes via Docker:
- docker compose exec lacrei_api python manage.py test

Cobertura:
- CRUD de profissionais
- CRUD de consultas
- Testes de erro e validações
---

---
## 🚀 CI/CD – GitHub Actions

Pipeline automatizado com:

Lint → Testes → Build → Deploy

Workflows localizados em:

.github/workflows/
---

--- 
## ☁️ Deploy (AWS)

Ambiente de Staging

Ambiente de Produção

Containers Docker

Banco de dados PostgreSQL

Variáveis sensíveis protegidas via GitHub Secrets

---

---
## 🔄 Rollback

Reversão de deploy via GitHub Actions

Re-deploy automático da última versão estável

Estratégia preparada para Blue/Green Deploy
---

---
## 💳 Integração com Asaas (Bônus)

Proposta de integração via API REST

Mock de split de pagamento

Arquitetura preparada para integração futura com serviços financeiros
---

---
## ✅ Checklist do Desafio

CRUD de profissionais

CRUD de consultas

Busca de consultas por ID do profissional

Segurança e autenticação

Docker + PostgreSQL

Testes automatizados

CI/CD

Deploy

Documentação completa

Swagger / Redoc
---

---
### 📦 Gerenciamento de Dependências

O projeto utiliza **Poetry** para gerenciamento de dependências.

As versões exatas estão travadas no arquivo:

- `poetry.lock`

Opcionalmente, pode-se gerar um `requirements.txt` com:

```bash
poetry self add poetry-plugin-export
poetry export -f requirements.txt --output requirements.txt
```
---

---
## 💙 Considerações Finais

Projeto desenvolvido com foco em qualidade, segurança e impacto social, alinhado aos valores da Lacrei Saúde.

🌈 Código é cuidado. Tecnologia transforma realidades.
---
