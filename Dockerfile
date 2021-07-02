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

CMD /bin/sh -c "echo 'docker dev ready'; while sleep 1000; do :; done"
