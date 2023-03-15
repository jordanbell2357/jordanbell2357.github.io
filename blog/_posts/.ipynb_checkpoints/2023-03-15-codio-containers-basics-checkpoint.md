---
layout: post
title: My favorite material from Codio's Container Basics on Coursera 
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

<samp>
Docker version 23.0.1, build a5ee5b1
  
Docker Compose version v2.16.0
</samp>

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

Here is a simple flow chart:

```mermaid
graph TD;
    A-->B;
    A-->C;
    B-->D;
    C-->D;
```

```bash
sudo docker build code/

sudo docker images
```

<samp>
REPOSITORY    TAG       IMAGE ID       CREATED         SIZE
<none>        <none>    7553068eca5c   6 seconds ago   231MB
hello-world   latest    feb5d9fea6a5   17 months ago   13.3kB
</samp>
