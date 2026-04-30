# Docker Dev Environment

## Start

```bash
cd docker
docker compose up --build
```

## Services

ibm-mq: local IBM MQ server
app: MQ Trace Lite CLI container


## Run CLI inside container
```bash
docker compose run --rm app poetry run python -m mqtrace.cli.main --help
```

Example:

```bash
docker compose run --rm app poetry run python -m mqtrace.cli.main inspect --queue DLQ.TEST
```

## Local Secrets

Copy the example environment file:

```bash
cp .env.example .env
```

Update values if needed.

Never commit .env.

## Notes
- App runs inside container
- MQ config is passed using environment variables
- This environment is for local development only