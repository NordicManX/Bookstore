FROM python:3.12.1-slim as python-base

ENV PYTHONUNBUFFERED=1 \
PYTHONDONTWRITEBYTECODE=1 \
PIP_NO_CACHE_DIR=off \
PIP_DISABLE_PIP_VERSION_CHECK=on \
PIP_DEFAULT_TIMEOUT=100 \
POETRY_HOME="/opt/poetry" \
POETRY_VIRTUALENVS_IN_PROJECT=true \
POETRY_NO_INTERACTION=1 \
PYSETUP_PATH="/opt/pysetup" \
VENV_PATH="/opt/pysetup/.venv"
ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

RUN apt-get update \
  && apt-get install --no-install-recommends -y \
    curl \
    build-essential

RUN pip install poetry

RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2

# Criar o diretório antes de copiar os arquivos
RUN mkdir -p $PYSETUP_PATH
WORKDIR $PYSETUP_PATH

# Copiar os arquivos de dependências
COPY poetry.lock pyproject.toml ./

RUN poetry install --only main --no-root

WORKDIR /app

COPY . /app/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
