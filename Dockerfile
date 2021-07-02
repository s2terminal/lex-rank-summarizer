FROM python:3.9.5-slim
WORKDIR /app

RUN apt-get update && apt-get install -y \
    git \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

RUN pip install poetry

COPY pyproject.toml ./
RUN poetry config virtualenvs.in-project true
RUN poetry install

CMD poetry run lex-rank-summarizer
