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

WORKDIR /code/
COPY --from=builder /code /code
COPY . /code
ENV PATH="/code/.venv/bin:$PATH"
