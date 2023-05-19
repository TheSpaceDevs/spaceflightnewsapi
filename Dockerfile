FROM python:3.11 AS builder

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV POETRY_CACHE_DIR='/var/cache/pypoetry'
ENV POETRY_HOME='/usr/local'

WORKDIR /code/
COPY pyproject.toml poetry.lock /code/

RUN curl -sSL 'https://install.python-poetry.org' | python
RUN poetry config virtualenvs.in-project true
RUN poetry install --no-interaction --no-root --no-ansi


FROM python:3.11
LABEL org.opencontainers.image.source https://github.com/TheSpaceDevs/spaceflightnewsapi

ARG RELEASE_VERSION
ENV SNAPI_VERSION=$RELEASE_VERSION

RUN groupadd appuser \
    && useradd -g appuser -m appuser

USER appuser

WORKDIR /code/
COPY --chown=appuser --from=builder /code /code
COPY --chown=appuser . /code
ENV PATH="/code/.venv/bin:$PATH"
EXPOSE 8000
