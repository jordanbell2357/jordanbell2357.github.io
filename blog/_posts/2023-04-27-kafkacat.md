---
layout: post
title: kafkacat
---

# kcat

[edenhill/kcat](https://github.com/edenhill/kcat):

```bash
git clone https://github.com/edenhill/kcat.git
cd kcat
bash bootstrap.sh
./configure
make
sudo make install
```

# confluentinc/demo-scene/maritime-ais

[confluentinc/demo-scene/maritime-ais](https://github.com/confluentinc/demo-scene/tree/master/maritime-ais)

We follow the above example.

We run `nc` locally and use `kcat` to send messages to the Confluent Cloud environment
`env-qr9drm`, to the cluster `lkc-nw8d2z`, to the topic `ais2`, 
where the cluster's bootstrap server endpoint is `pkc-419q3.us-east4.gcp.confluent.cloud:9092`, and
where `3FPYLWJU5MMU2TL2` is an API key for the cluster.

The syntax we end up with does not invoke the environment ID or the cluster ID, but we do not
know that beforehand; above we laid out all the parameters at our disposal.

We use `gpsdecode` from `gpsd-clients`.

```bash
ENVIRONMENT_ID='env-qr9drm'
CLUSTER_ID='lkc-nw8d2z'
BOOTSTRAP_SERVER='pkc-419q3.us-east4.gcp.confluent.cloud:9092'
API_KEY='3FPYLWJU5MMU2TL2'
API_SECRET= #

nc 153.44.253.27 5631 | \
gpsdecode | \
kcat -b $BOOTSTRAP_SERVER \
-X security.protocol=SASL_SSL \
-X sasl.mechanisms=PLAIN \
-X sasl.username=$API_KEY \
-X sasl.password=$API_SECRET \
-t ais2 \
-K ':' \
-D '\n' \
-P
```

![kcat](/images/Confluent/ais2_kcat.jpeg)

# Deploying on EC2 instance

We create an EC2 instance running Ubuntu:

![EC2 instance running Ubuntu](/images/Confluent/aws_ec2_instance.jpeg)

Connect to EC2 instance using OpenSSH. On WSL2, to get the permissions on the `.pem` file to `400`,
we move it to the Ubuntu home directory: there seemed to be issues with permissions keeping it in a Windows created directory.

Connected with OpenSSH to the instance, we do the following.

[Install the Confluent CLI \| Confluent Documentation](https://docs.confluent.io/confluent-cli/current/install.html)

```bash
cd ~/

curl -sL --http1.1 https://cnfl.io/cli | sh -s -- latest

export PATH="/home/$USER/bin:$PATH"

ENVIRONMENT_ID='env-qr9drm'
CLUSTER_ID='lkc-nw8d2z'
TOPIC_ID='ais2'
API_KEY='3FPYLWJU5MMU2TL2'
API_SECRET= #

confluent login --save
confluent environment use $ENVIRONMENT_ID
confluent kafka cluster use $CLUSTER_ID
confluent api-key store $API_KEY $API_SECRET --resource $TOPIC_ID
```

Then we make the file `my_command.sh`:

```bash
#!/bin/bash
# my_command.sh

nc 153.44.253.27 5631 | \
gpsdecode | \
kcat -b $BOOTSTRAP_SERVER \
-X security.protocol=SASL_SSL \
-X sasl.mechanisms=PLAIN \
-X sasl.username=$API_KEY \
-X sasl.password=$API_SECRET \
-t ais2 \
-K ':' \
-D '\n' \
-P
```

Then:

```bash
nohup bash my_command.sh &
exit
```

In Confluent Cloud, we see after exiting OpenSSH, the EC2 instance continues to send messages to the topic.

![EC2 instance sending messages to Confluent Cloud](/images/Confluent/aws_nohup.jpeg)