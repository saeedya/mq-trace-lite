FROM python:3.12-slim

WORKDIR /app

# system deps (برای build بعداً لازم میشه)
RUN apt-get update && apt-get install -y \
    gcc \
    build-essential \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Download IBM MQ Redistributable Client
RUN mkdir -p /opt/mqm \
    && wget -q https://public.dhe.ibm.com/ibmdl/export/pub/software/websphere/messaging/mqdev/redist/9.4.2.0-IBM-MQC-Redist-LinuxX64.tar.gz \
    && tar -xzf 9.4.2.0-IBM-MQC-Redist-LinuxX64.tar.gz -C /opt/mqm \
    && rm 9.4.2.0-IBM-MQC-Redist-LinuxX64.tar.gz

# poetry
RUN pip install poetry

ENV MQ_HOME=/opt/mqm
ENV LD_LIBRARY_PATH=/opt/mqm/lib64

RUN pip install pymqi

# copy deps
COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false \
    && poetry install --no-root

# copy code
COPY . .

CMD ["python", "-m", "mqtrace.cli.main"]