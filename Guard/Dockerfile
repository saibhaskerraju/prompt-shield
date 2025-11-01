# Default to Python 3.12
ARG BASE_IMAGE=python:3.12-slim
FROM ${BASE_IMAGE}

# Set the working directory for your application
WORKDIR /app

# Copy the entrypoint.sh script first, as it is the most critical file.

RUN apt-get update && apt-get install -y dos2unix

COPY pyproject.toml /app/
COPY poetry.lock /app

RUN pip install --no-cache-dir -U pip==25.2 setuptools==80.9.0 && pip install --no-cache-dir poetry==1.8.3
RUN poetry config virtualenvs.create false && poetry install

COPY entrypoint.sh /app/
COPY . /app

RUN dos2unix /app/entrypoint.sh && \
    chmod +x /app/entrypoint.sh

# Set the entrypoint for the container.
ENTRYPOINT ["/app/entrypoint.sh"]