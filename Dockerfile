FROM python:3.8

RUN mkdir /app
WORKDIR /app

RUN apt update

COPY ./Pipfile /app/Pipfile
COPY ./Pipfile.lock /app/Pipfile.lock

RUN pip install pipenv
RUN pipenv install
RUN pipenv install gunicorn