#!/usr/bin/bash env
export dockerhub_repo=ratoloko765

echo 'export dockerhub_repo=ratoloko765' >> ~/.bashrc 
source ~/.bashrc

docker-compose up -d
docker images 
docker tag flask-boilerplate_app:latest ${dockerhub_repo}/flask-boilerplate_app:latest
docker login
docker push ${dockerhub_repo}/flask-boilerplate_app:latest
docker-compose up -d
docker images 
docker tag flask-boilerplate_app:latest ratoloko765/flask-boilerplate_app:latest
docker login
docker push ratoloko765/flask-boilerplate_app:latest
