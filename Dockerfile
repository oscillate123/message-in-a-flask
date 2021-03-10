FROM ubuntu:20.04

MAINTAINER Oscar THL "oscar@theheroloop.com"

RUN apt-get update -y && apt-get install -y python3-pip python3-flask

COPY ./requirements.txt /app/requirements.txt

COPY ./flask-app /app/flask-app

WORKDIR /app

RUN pip3 install -r requirements.txt

ENV FLASK_DEBUG=1
ENV FLASK_APP=/app/flask-app
ENV FLASK_ENV=development

ENTRYPOINT flask run --host=0.0.0.0
