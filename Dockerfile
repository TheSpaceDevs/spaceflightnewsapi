FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

# Update the package os dependencies
RUN apt-get update && apt-get install -y

# Copy the project files into the image
ADD api/ /app/api/
ADD consumer/ /app/consumer/
ADD snapy/ /app/snapy/
ADD manage.py pyproject.toml uv.lock README.md /app/

# Sync the project into a new environment, using the frozen lockfile
WORKDIR /app
RUN uv sync --frozen --no-dev

EXPOSE 8000
