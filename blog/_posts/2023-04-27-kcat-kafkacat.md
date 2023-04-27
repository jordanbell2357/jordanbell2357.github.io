---
layout: post
title: kcat (kafkacat)
---

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