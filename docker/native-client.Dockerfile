FROM python:3.12-slim

WORKDIR /app

# system deps (برای build بعداً لازم میشه)
RUN apt-get update && apt-get install -y \
    gcc \
    build-essential \
    wget \
    && rm -rf /var/lib/apt/lists/*

# poetry
RUN pip install poetry

# copy deps
COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false \
    && poetry install --no-root

# copy code
COPY . .

CMD ["python", "-m", "mqtrace.cli.main"]