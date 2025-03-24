# Usar uma imagem Python Slim para otimização de espaço
FROM python:3.12-slim AS python-base

# Definir variáveis de ambiente para otimização
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

# Instalar dependências essenciais
RUN apt-get update && apt-get install --no-install-recommends -y \
        curl build-essential libpq-dev gcc libc-dev \
    && pip install --no-cache-dir poetry \
    && poetry --version \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Criar diretório de trabalho
WORKDIR /app

# Copiar apenas os arquivos essenciais para instalar dependências
COPY poetry.lock pyproject.toml ./

# Instalar todas as dependências (não apenas as de produção)
RUN poetry install --no-root

# Copiar o restante do código-fonte
COPY . .

# Expor a porta padrão do Django
EXPOSE 8000

# Comando para rodar a aplicação
CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]

