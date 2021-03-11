#!/bin/bash

docker kill mia
docker build --rm -t thlab/mia:latest ./
docker image prune -f
docker run --name mia -d --rm -it -p 5000:5000 thlab/mia:latest
