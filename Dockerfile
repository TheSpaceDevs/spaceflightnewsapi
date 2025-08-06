FROM ghcr.io/astral-sh/uv:python3.13-bookworm-slim AS builder

# Get the required UV tokens for the project
ARG UV_INDEX_TSD_USERNAME
ARG UV_INDEX_TSD_PASSWORD

# Set the UV tokens as environment variables
ENV UV_INDEX_TSD_USERNAME=$UV_INDEX_TSD_USERNAME
ENV UV_INDEX_TSD_PASSWORD=$UV_INDEX_TSD_PASSWORD

# Set the environment variables for the UV build
ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy

WORKDIR /app
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project --no-dev \

ADD src/ /app/src/

# Sync the project into a new environment, using the frozen lockfile
RUN uv sync --frozen --no-dev


FROM ghcr.io/astral-sh/uv:python3.13-bookworm-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PATH="/app/.venv/bin:$PATH"

# Update the package os dependencies
RUN apt-get update && apt-get upgrade -y

WORKDIR /app

# Copy the project files into the image
COPY --from=builder --chown=app:app /app /app

EXPOSE 8000

CMD ["gunicorn", "snapy.wsgi", "--bind", ":8000", "--workers", "2", "--access-logfile", "-", "--error-logfile", "-"]
