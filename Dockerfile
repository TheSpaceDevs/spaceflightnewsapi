FROM python:3.12-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV POETRY_CACHE_DIR='/var/cache/pypoetry'
ENV POETRY_HOME='/usr/local'
ENV APP_HOME=/code
ENV APP_USER=appuser

RUN groupadd --system $APP_USER && \
    useradd --system --gid $APP_USER --create-home --home $APP_HOME $APP_USER

WORKDIR ${APP_HOME}

RUN pip install poetry
RUN poetry config virtualenvs.in-project true

ADD --chown=${APP_USER}:${APP_USER} pyproject.toml poetry.lock ./
RUN poetry install --no-interaction


FROM base
LABEL org.opencontainers.image.source=https://github.com/TheSpaceDevs/spaceflightnewsapi


COPY --chown=${APP_USER}:${APP_USER} --from=base ${APP_HOME} ${APP_HOME}
ADD --chown=${APP_USER}:${APP_USER} . ${APP_HOME}

# Install the project again, to install the project in the final image (and have the version available)
RUN poetry install --no-interaction

ENV PATH="${APP_HOME}/.venv/bin:$PATH"


USER ${APP_USER}
EXPOSE 8000
