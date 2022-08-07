#!/usr/bin/bash env
docker-compose up -d
docker images 
docker tag flask-boilerplate_app:latest ratoloko765/flask-boilerplate_app:latest
docker login
docker push ratoloko765/flask-boilerplate_app:latest
