FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

# The uv provided image is not working, so we're installing it ourselves.
# The installer requires curl (and certificates) to download the release archive
RUN apt-get update && apt-get install -y

# Copy the project into the image
ADD api/ /app/api/
ADD consumer/ /app/consumer/
ADD snapy/ /app/snapy/
ADD manage.py pyproject.toml uv.lock README.md /app/

# Sync the project into a new environment, using the frozen lockfile
WORKDIR /app
RUN uv sync

EXPOSE 8000
