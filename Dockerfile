## ------------------------------- Builder Stage ------------------------------ ##
FROM python:3.13-slim-trixie AS builder

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-install-project

## ------------------------------- Production Stage ------------------------------ ##
FROM python:3.13-slim-trixie AS production

RUN useradd --create-home appuser
USER appuser

WORKDIR /app

COPY . .
COPY --from=builder /app/.venv /app/.venv

ENV PATH="/app/.venv/bin:$PATH"

EXPOSE 80

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
