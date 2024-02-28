FROM python:3.12-bullseye AS builder

RUN pip install poetry==1.7.1

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_CACHE_DIR='/tmp/poetry'

WORKDIR /app

COPY pyproject.toml poetry.lock ./
RUN touch README.md
RUN poetry install --no-dev --no-root
RUN rm -rf ${POETRY_CACHE_DIR}


FROM python:3.12-slim-bullseye AS runtime
WORKDIR /app

ENV VIRTUAL_ENV=/app/.venv \
    PATH="/app/.venv/bin:$PATH"

COPY --from=builder ${VIRTUAL_ENV} ${VIRTUAL_ENV}
COPY clouddnsflare /app/clouddnsflare

ENTRYPOINT ["python", "-m", "clouddnsflare"]


