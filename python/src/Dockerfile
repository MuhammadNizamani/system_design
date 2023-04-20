FROM python:10.3-slim-bullseye
RUN apt-get-update \
    && apt-get install -y --no-install-recommends --no-install-suggests \
    build-essentails default-libmysqlclint-dev \
    && pip install  --no-cache-dir --upgrade pip

WORKDIR /app
COPY ./requirement.txt /app
RUN 