FROM python:3.11
LABEL org.opencontainers.image.source https://github.com/TheSpaceDevs/spaceflightnewsapi
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY pyproject.toml .
RUN pip install --upgrade pip
RUN pip install poetry && \
    poetry export -o requirements.txt && \
    pip install -r requirements.txt
COPY . .
