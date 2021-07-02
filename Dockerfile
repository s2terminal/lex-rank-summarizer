FROM python:3.9.5-slim AS base
WORKDIR /app

RUN apt-get update && apt-get install -y \
    git \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

RUN pip install poetry

COPY pyproject.toml ./
COPY poetry.lock ./
RUN poetry config virtualenvs.in-project true
RUN poetry install

FROM base AS dev

CMD /bin/sh -c "echo 'docker dev ready'; while sleep 1000; do :; done"

FROM base AS prod

COPY ./src ./src
ENTRYPOINT ["poetry", "run", "lex-rank-summarizer"]
