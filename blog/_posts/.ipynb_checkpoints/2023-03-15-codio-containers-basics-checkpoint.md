---
layout: post
title: My favorite material from Codio's Container Basics on Coursera
topic: training
---

[Container Creation and Orchestration Basics \| Codio](https://www.coursera.org/learn/codio-container-creation-and-orchestration-basics)

```bash
sudo mkdir -p /etc/apt/keyrings

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

echo \
"deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
$(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update

sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin

docker --version

docker compose version
```

<samp>Docker version 23.0.1, build a5ee5b1</samp>
  
<samp>Docker Compose version v2.16.0</samp>

```bash
sudo mkdir code

sudo touch code/numbers.txt

8
4
3
1
7
22
48
100
9

sudo touch code/evenOdd.sh
```

```bash
#!bin/bash

file='numbers.txt'

while read number; do
  remainder=$((number%2))
  if [ $remainder == 0 ]; then
        echo "Number is even"
    else
        echo "Number is odd"
  fi
done < $file
```

```bash
cd ..

sudo docker login

sudo touch code/Dockerfile
```

```bash
FROM centos

ADD . /code

WORKDIR /code

ENTRYPOINT ["bash", "evenOdd.sh"]
```

```bash
sudo docker build code/

sudo docker images
```

```
REPOSITORY    TAG       IMAGE ID       CREATED         SIZE
<none>        <none>    7553068eca5c   6 seconds ago   231MB
hello-world   latest    feb5d9fea6a5   17 months ago   13.3kB
```

```bash
sudo docker build -t even-odd code/

sudo docker images
```

```
REPOSITORY    TAG       IMAGE ID       CREATED          SIZE
even-odd      latest    7553068eca5c   16 minutes ago   231MB
hello-world   latest    feb5d9fea6a5   17 months ago    13.3kB
```

```bash
sudo docker run --name eo-container even-odd
```

> This is a very simple example of a running a custom image in a container. The general process, however, is common. Create a Dockerfile specific to our needs. We chose our own operating system, copied over the files we need, and then gave a command to run an application. The resulting container is an isolated environment that runs our application on startup and then stops once the application is done.

```bash
cat server/server.py
```

```python3
from http.server import BaseHTTPRequestHandler, HTTPServer

class ContainerRequests(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write('Hello from a Docker container\n'.encode())
        
    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write('Hello from port 9000.\n'.encode())

host = '0.0.0.0'
port = 9000
HTTPServer((host, port), ContainerRequests).serve_forever()
```

```bash
sudo touch server/Dockerfile
```

```bash
FROM python

Add . /code

WORKDIR /code

ENTRYPOINT ["python", "server.py"]
```

```bash
sudo docker build -t python_server server/

sudo docker run -d --name web_server python_server
```

```
CONTAINER ID   IMAGE           COMMAND              CREATED          STATUS          PORTS     NAMES
8e7877cbeb26   python_server   "python server.py"   17 seconds ago   Up 16 seconds             web_server
```

> We can add a flag when running our image to map a port on the Linux VM to the port in the container. Before we can do that, we first need to remove the web_server container.

```bash
sudo docker stop web_server

sudo docker rm web_server

sudo docker run -p 80:9000 -d --name web_server python_server
```

```
CONTAINER ID   IMAGE           COMMAND              CREATED              STATUS              PORTS                                   NAMES
1056057c44f4   python_server   "python server.py"   About a minute ago   Up About a minute   0.0.0.0:80->9000/tcp, :::80->9000/tcp   web_server
```

```bash
curl 0.0.0.0:80

curl -X POST 0.0.0.0:80
```

```
Hello from a Docker container

Hello from port 9000.
```

```bash
sudo docker stop web_server
```

> Containers need an operating system but they are also environments to run specific applications. That means they may need special packages installed as well. Instead of building on top of a general purpose image like CentOS, you can select an image for a specific programming language, database, web server, or other tools like load balancers, content management, etc.
>
> Choosing one of these task-specific images as a starting point offers a convenience of not having to specify which software you have to install. On the last page, the base image in our Dockerfile was python. We used this instead of centos so that we did not have to install Python ourselves.


```bash
sudo touch birthday/Dockerfile
```

```bash
FROM alpine

ADD . /code

WORKDIR /code

RUN apk add py3-pip python3

RUN python3 -m pip install -r requirements.txt

ENTRYPOINT ["python3", "main.py"]
```

```bash
sudo docker build -t birthday-image birthday/

sudo docker images
```

```
REPOSITORY       TAG       IMAGE ID       CREATED          SIZE
birthday-image   latest    92f31c7d65ec   9 seconds ago    85.9MB
python_server    latest    3c61b2f2d123   10 minutes ago   921MB
even-odd         latest    7553068eca5c   32 minutes ago   231MB
hello-world      latest    feb5d9fea6a5   17 months ago    13.3kB
```

```bash
sudo touch code/passwords.txt

Super-secret password

sudo docker build -t even-odd:0.2 code/

sudo docker run -d -t --name secrets even-odd:0.2
```

>  Stop all running containers with a single command.

```bash
sudo docker stop $(sudo docker container ls -q)
```

![Codio](/images/Codio/Codio-Custom-Images.png)

![Codio](/images/Codio/Codio-Container-Registries.png)

![Docker](/images/Docker/docker101tutorial.png)

![Docker](/images/Docker/Getting-Started-Getting-Started.png)

![Docker](/images/Docker/March_15_2023.png)

![Docker](/images/Docker/Todo-App.png)

![Docker Playground](/images/Docker/Docker-Playground.png)