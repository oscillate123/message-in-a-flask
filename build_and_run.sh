#!/bin/bash

workdir="/opt/dev/message-in-a-flask/"

# docker container setup
#docker kill mia
#docker build --rm -t thlab/mia:latest /opt/dev/message-in-a-flask
#docker image prune -f
#docker run --name mia -d --rm -it -p 5000:5000 thlab/mia:latest

# docker compose setup
docker-compose -f $workdir/mia-compose.yml up --build -d
docker image prune -f