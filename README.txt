README
======

This package includes the following files. ------------------------------------------------------------------------------

|	docker-compose.yml
|       README.txt
|
|-------client
|       |  Dockerfile
|       |  requirements.txt
|       |
|       |__app
|             client.py
|
|-------server
|       |  Dockerfile
|       |  requirements.txt
|       |
|       |__app
|             server.py


Questions: -------------------------------------------------------------------------------------------------------------

1. What is a docker container? [2]

A Docker container image is a lightweight, standalone, executable package of software that includes everything needed to run an application: code, runtime, system tools, system libraries and settings.

2. What is the difference between a container and a virtual machine? [2]

Containers and virtual machines have similar resource isolation and allocation benefits, but function differently because containers virtualize the operating system instead of hardware. Containers are more portable and efficient.

Containers are an abstraction at the app layer that packages code and dependencies together. Multiple containers can run on the same machine and share the OS kernel with other containers, each running as isolated processes in user space.

Virtual machines (VMs) are an abstraction of physical hardware turning one server into many servers. The hypervisor allows multiple VMs to run on a single machine.  

3. What is the purpose of a Dockerfile? [2]

A Dockerfile is a text document that contains all the commands a user could call on the command line to assemble an image. Using docker build users can create an automated build that executes several command-line instructions in succession so that the user doesn't have to.

4. What is the purpose of a requirements.txt file? [2]

The requirements.txt file is a list of dependencies that are called in the Dockerfile with pip3 install to ensure that when the user runs the docker image they have the same working environment.

5. What is the purpose of a docker-compose.yml file? [2]

Compose is a tool for defining and running multi-container Docker applications. With Compose, you use a YAML file to configure your application’s services. Then, with a single command, you create and start all the services from your configuration. To learn more about all the features of Compose, see the list of features. Run your Docker app with 'docker-compose up' 

6. What is the difference between a docker image and docker container? [2]

A Docker image is an immutable (unchangeable) file that contains the source code, libraries, dependencies, tools, and other files needed for an application to run.

Since images are, in a way, just templates, you cannot start or run them. What you can do is use that template as a base to build a container. A container is, ultimately, just a running image. Once you create a container, it adds a writable layer on top of the immutable image, meaning you can now modify it.

The image-base on which you create a container exists separately and cannot be altered. When you run a containerized environment, you essentially create a read-write copy of that filesystem (docker image) inside the container. This adds a container layer which allows modifications of the entire copy of the image.

7. What command can be used to create an image from a Dockerfile? [2]

docker build <path>

8. What command will start a docker container? [2]

To start a container from a docker image file you will use the following command:
 docker run [OPTIONS] IMAGE [COMMAND] [ARG...]

To start one or more stopped containers you use the following command:
 docker start [OPTIONS] CONTAINER [CONTAINER...]

9. What command will stop a docker container? [2]

To stop one or more running containers tou use the following command:
 docker stop [OPTIONS] CONTAINER [CONTAINER...]

10. What command will remove a docker container? Image? [5]

To remove one or more containers use the command:
 docker stop [OPTIONS] CONTAINER [CONTAINER...]

To remove one or more imagaes use the command:
 docker rmi [OPTIONS] IMAGE [IMAGE...]

11. What command will list all running docker containers? all containers? [5]

The command to list all running containers is:
 docker container ls

12. What command will list all docker images?

The command to list all docker images is:
 docker images ls

13. What command do you use to deploy docker containers using information in the dockercompose.yml file? [2]

The command you use to compile based off of the yml file is:
 docker compose up

14. How can you specify in the docker-compose.yml file that you want docker containers to use the
hosts network? [5]

In the .yml file you can specify "network_mode: host" to ensure your containers use the host network.

15. How can you specify in the docker-compose.yml file where the Dockerfile for a particular container
is found?

You specify where the Dockerfiles are in the "build: <file-path>" command under the "services" section


Docker compose output ----------------------------------------------------------------------------------

PS C:\Users\Anhon\Desktop\CS-370\Homework\HW6> docker-compose up --build

Building server
[+] Building 22.1s (14/14) FINISHED
 => [internal] load build definition from Dockerfile                                                                                                                                                                0.0s 
 => => transferring dockerfile: 32B                                                                                                                                                                                 0.0s 
 => [internal] load .dockerignore                                                                                                                                                                                   0.0s 
 => => transferring context: 35B                                                                                                                                                                                    0.0s 
 => resolve image config for docker.io/docker/dockerfile:1                                                                                                                                                         10.8s 
 => CACHED docker-image://docker.io/docker/dockerfile:1@sha256:42399d4635eddd7a9b8a24be879d2f9a930d0ed040a61324cfdf59ef1357b3b2                                                                                     0.0s 
 => [internal] load build definition from Dockerfile                                                                                                                                                                0.0s 
 => [internal] load .dockerignore                                                                                                                                                                                   0.0s 
 => [internal] load metadata for docker.io/library/python:3.8-slim-buster                                                                                                                                          10.6s 
 => [internal] load build context                                                                                                                                                                                   0.0s 
 => => transferring context: 1.39kB                                                                                                                                                                                 0.0s 
 => [1/5] FROM docker.io/library/python:3.8-slim-buster@sha256:9e3036f6b032794efb662f3c579c4c35d0b678bc793590e3e2e217cb5bf1e11b                                                                                     0.0s 
 => CACHED [2/5] COPY requirements.txt .                                                                                                                                                                            0.0s 
 => CACHED [3/5] RUN python -m pip install -r requirements.txt                                                                                                                                                      0.0s 
 => CACHED [4/5] WORKDIR /app                                                                                                                                                                                       0.0s 
 => [5/5] COPY . /app                                                                                                                                                                                               0.0s 
 => exporting to image                                                                                                                                                                                              0.1s 
 => => exporting layers                                                                                                                                                                                             0.1s 
 => => writing image sha256:42b3b14bb2b48fb6f0ca24719543e55ccfabec61b8e3ec69603a286cb75f168c                                                                                                                        0.0s 
 => => naming to docker.io/library/hw6_server                                                                                                                                                                       0.0s 

Use 'docker scan' to run Snyk tests against images to find vulnerabilities and learn how to fix them
Building client
[+] Building 0.5s (10/10) FINISHED
 => [internal] load build definition from Dockerfile                                                                                                                                                                0.0s 
 => => transferring dockerfile: 32B                                                                                                                                                                                 0.0s 
 => [internal] load .dockerignore                                                                                                                                                                                   0.0s 
 => => transferring context: 35B                                                                                                                                                                                    0.0s 
 => [internal] load metadata for docker.io/library/python:3.8-slim-buster                                                                                                                                           0.3s 
 => [1/5] FROM docker.io/library/python:3.8-slim-buster@sha256:9e3036f6b032794efb662f3c579c4c35d0b678bc793590e3e2e217cb5bf1e11b                                                                                     0.0s 
 => [internal] load build context                                                                                                                                                                                   0.0s 
 => => transferring context: 94B                                                                                                                                                                                    0.0s 
 => CACHED [2/5] COPY requirements.txt .                                                                                                                                                                            0.0s 
 => CACHED [3/5] RUN python -m pip install -r requirements.txt                                                                                                                                                      0.0s 
 => CACHED [4/5] WORKDIR /app                                                                                                                                                                                       0.0s 
 => CACHED [5/5] COPY . /app                                                                                                                                                                                        0.0s 
 => exporting to image                                                                                                                                                                                              0.0s 
 => => exporting layers                                                                                                                                                                                             0.0s 
 => => writing image sha256:e1c79f2ced38549915e209ae2aaeefd016525ff5c8c70da5e96637fc6d1f5f5d                                                                                                                        0.0s 
 => => naming to docker.io/library/hw6_client                                                                                                                                                                       0.0s 

Use 'docker scan' to run Snyk tests against images to find vulnerabilities and learn how to fix them
Recreating hw6_server_1 ... done
Recreating hw6_client_1 ... done
Attaching to hw6_server_1, hw6_client_1
server_1  | Reading value 5
server_1  |  * Serving Flask app "server" (lazy loading)
server_1  |  * Environment: production
server_1  |    WARNING: This is a development server. Do not use it in a production deployment.
server_1  |    Use a production WSGI server instead.
server_1  |  * Debug mode: off
server_1  |  * Running on all addresses.
server_1  |    WARNING: This is a development server. Do not use it in a production deployment.
server_1  |  * Running on http://172.24.0.2:5000/ (Press CTRL+C to quit)
server_1  | 172.24.0.1 - - [10/Nov/2021 05:34:44] "GET / HTTP/1.1" 200 -
client_1  | The square root of 5 is: 2.23606797749979
hw6_client_1 exited with code 0
