---
layout: post
title: Installing and using Hadoop and Pyspark on Ubuntu with VirtualBox
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

Connecting to Github:

![image](https://github.com/jordanbell2357/jordanbell2357.github.io/assets/47544607/3e708dcb-4210-4f5c-ab5e-cc25a2b7896c)

Jupyter Lab:

![image](https://github.com/jordanbell2357/jordanbell2357.github.io/assets/47544607/3bb7f2c7-c91d-45ba-bc9e-7d329782e6fd)

![image](https://github.com/jordanbell2357/jordanbell2357.github.io/assets/47544607/4a504891-932f-43fa-994b-fbb29b39db7d)

Increasing disk size of Ubuntu virtual disk:

![image](https://github.com/jordanbell2357/jordanbell2357.github.io/assets/47544607/b86d251b-016e-462c-8562-4bd4d1d71220)

![image](https://github.com/jordanbell2357/jordanbell2357.github.io/assets/47544607/fedd42eb-c822-4e07-90c2-8cdf39e2b6a9)

![image](https://github.com/jordanbell2357/jordanbell2357.github.io/assets/47544607/84f1de18-9b32-41b5-8134-b8b4f747f340)

![image](https://github.com/jordanbell2357/jordanbell2357.github.io/assets/47544607/1e425474-328e-446d-a710-ed3405027da3)

![image](https://github.com/jordanbell2357/jordanbell2357.github.io/assets/47544607/3d945c5e-021e-4d70-8100-fa365f5c3c41)

![image](https://github.com/jordanbell2357/jordanbell2357.github.io/assets/47544607/5e2a7eaf-40cf-44e8-b754-8392300b1662)

![image](https://github.com/jordanbell2357/jordanbell2357.github.io/assets/47544607/76ff01a2-87c9-4b76-8755-4c2b2ecc84b0)

![image](https://github.com/jordanbell2357/jordanbell2357.github.io/assets/47544607/35ae8d81-93e7-4962-a5d2-eb3517c24b01)




