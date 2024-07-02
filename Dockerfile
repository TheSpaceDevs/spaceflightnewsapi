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

COPY --chown=${APP_USER}:${APP_USER} pyproject.toml poetry.lock README.md ./
RUN poetry install --no-interaction


FROM base
LABEL org.opencontainers.image.source=https://github.com/TheSpaceDevs/spaceflightnewsapi


COPY --chown=${APP_USER}:${APP_USER} --from=base ${APP_HOME} ${APP_HOME}
COPY --chown=${APP_USER}:${APP_USER} ./api ${APP_HOME}/api
COPY --chown=${APP_USER}:${APP_USER} ./snapy ${APP_HOME}/snapy
COPY --chown=${APP_USER}:${APP_USER} ./consumer ${APP_HOME}/consumer
COPY --chown=${APP_USER}:${APP_USER} ./manage.py ${APP_HOME}/


# Install the project again, to install the project in the final image (and have the version available)
RUN poetry install --no-interaction

ENV PATH="${APP_HOME}/.venv/bin:$PATH"


USER ${APP_USER}
EXPOSE 8000
