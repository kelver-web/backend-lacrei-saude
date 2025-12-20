FROM python:3.12-slim

# Evita arquivos .pyc e buffer
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Dependências do sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Poetry
RUN pip install poetry

# Copia dependências
COPY pyproject.toml poetry.lock* /app/

# Desativa venv do poetry
RUN poetry config virtualenvs.create false

# Instala dependências
RUN poetry install --no-interaction --no-ansi

# Copia projeto
COPY . /app/

# Porta padrão
EXPOSE 8000

# Comando default
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
