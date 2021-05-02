# api_db
Python API based on Fastapi 

To execute a project, we must:

1. Create a network in Docker and attach containers

~$ docker network create -d bridge --subnet=172.18.0.0/16  api-network

~$ docker network connect api-network fastapi-app
~$ docker network connect api-network mysql 
~$ docker network connect api-network mongo 


2. Launch containers with folling parameters:

~$ docker container run -it --name fastapi-app -v /home/data:/home/app/ --ip 172.18.0.3 -p 8000:8000 -d fast-api
~$ docker container run -it --name mysql -v /home/data/:/home/api/ --ip 172.18.0.2 -p 3306:3306 -d mysql-fastapi
~$ docker container run -it --name mongo -v /home/data/:/home/api/ --ip 172.18.0.4 -p 27017:27017 -d mongo
