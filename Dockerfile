FROM python:3.11
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY pyproject.toml .
RUN pip install --upgrade pip
RUN pip install poetry && \
    poetry export -o requirements.txt && \
    pip install -r requirements.txt
COPY . .
