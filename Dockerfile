FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

# Get the required UV tokens for the project
ARG UV_INDEX_TSD_USERNAME
ARG UV_INDEX_TSD_PASSWORD

# Set the UV tokens as environment variables
ENV UV_INDEX_TSD_USERNAME=$UV_INDEX_TSD_USERNAME
ENV UV_INDEX_TSD_PASSWORD=$UV_INDEX_TSD_PASSWORD

# Update the package os dependencies
RUN apt-get update && apt-get install -y

# Copy the project files into the image
ADD pyproject.toml uv.lock README.md /app/
ADD src/ /app/src/

# Sync the project into a new environment, using the frozen lockfile
WORKDIR /app
RUN uv sync --frozen --no-dev

EXPOSE 8000
