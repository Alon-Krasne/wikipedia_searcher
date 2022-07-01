FROM python:3.10-alpine

RUN apk update && python -m pip install pipenv

COPY . /app
WORKDIR /app

RUN pipenv install