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

