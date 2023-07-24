---
layout: post
title: Installing and using Hadoop with VirtualBox
---

[How To Install Hadoop in Stand-Alone Mode on Ubuntu 20.04. Published on February 15, 2022. By Tony Tran and Hanif Jetha. DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-install-hadoop-in-stand-alone-mode-on-ubuntu-20-04)

`ubuntu-22.04.2-desktop-amd64.iso`

```bash
su
usermod -aG ubuntu sudo
```

`wget https://dlcdn.apache.org/hadoop/common/hadoop-3.3.6/hadoop-3.3.6.tar.gz`

`tar -xvzf hadoop-3.3.6.tar.gz`

`su mv hadoop-3.3.6 /usr/local/hadoop`

![image](https://github.com/jordanbell2357/jordanbell2357.github.io/assets/47544607/27948f3f-a26a-49bc-b356-f5d834bf2da0)

`wget https://repo.anaconda.com/archive/Anaconda3-2023.07-1-Linux-x86_64.sh`

`bash Anaconda3-2023.07-1-Linux-x86_64.sh`

![image](https://github.com/jordanbell2357/jordanbell2357.github.io/assets/47544607/5e6176c9-d4f3-46f2-bfa1-8237e401d1b0)

In the following screenshots, we see Pyspark being used with Hadoop and a file successfully written to the local file system.

```python
predictions.select('prediction', 'label').write \
    .format('csv') \
    .option('header', 'true') \
    .save('predictions.csv')
```

![image](https://github.com/jordanbell2357/jordanbell2357.github.io/assets/47544607/e79d3191-ce4f-4be4-b342-6395116fad18)

![image](https://github.com/jordanbell2357/jordanbell2357.github.io/assets/47544607/1d2421ab-fd3d-4320-abc5-6397f1de31ae)
