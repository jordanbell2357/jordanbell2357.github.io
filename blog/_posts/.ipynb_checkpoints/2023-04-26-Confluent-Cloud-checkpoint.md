---
layout: post
title: Confluent Cloud
topic: cli
---

[Install the Confluent CLI \| Confluent Documentation](https://docs.confluent.io/confluent-cli/current/install.html)

```bash
cd ~/

curl -sL --http1.1 https://cnfl.io/cli | sh -s -- latest

export PATH="/home/$USER/bin:$PATH"
```

Then we follow [Connect Confluent CLI to Confluent Cloud Cluster](https://docs.confluent.io/confluent-cli/current/connect.html). For me, the key parts are:

```bash
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

# Schema Registry

[Get started with Confluent Stream Governance \| Learn - Confluent Cloud](https://confluent.cloud/learn)

> Try out a basic workflow to leverage schemas in Kafka with Confluent Cloud. You'll start by enabling Schema Registry for an environment, create a Kafka topic, define a schema for that topic, then produce and consume properly formatted messages. You can experiment with introducing data that doesn't meet the schema definitions or adds fields not originally scoped, and learn how to work with versioning and compatibility settings to fit your use cases.


![Finish Getting Started with Schema Registry](/images/Confluent/Topics-Confluent-Cloud.png)

```
=== Confluent Cloud API key: lsrc-nw80nk ===

API key:
F3PLLTOYG76ZW5R2

API secret:
mK7oAqsyUiQa6znly7aDYrlHOk9aVyppR1wsIJ69HnBtGLtV8xtkf+Vohh4XRM6A
```

```bash
confluent environment use env-pr0mzm
```

```bash
confluent kafka cluster use lkc-knrwgg
```

```bash
confluent api-key create --resource lkc-knrwgg
```

```
+------------+------------------------------------------------------------------+
| API Key    | O4TIZRY7JFUG6LHI                                                 |
| API Secret | EqAkcV7FhscsxuC82MNqkDZr0PyTCiJyunQlcKDPkSjdByHrlMCZPRtXufWaqy8o |
+------------+------------------------------------------------------------------+
```

```
confluent api-key use O4TIZRY7JFUG6LHI --resource lkc-knrwgg
```

The following command is run in the same directory that contains `schema-orders-value-v1.avsc`.

```
confluent kafka topic produce orders --value-format avro --schema schema-orders-value-v1.avsc
```

```
{"orderId":2122453, "orderTime": 1607641868, "orderAddress":"899 W Evelyn Ave, Mountain View, CA 94041"}
{"orderId":2123453, "orderTime": 1682445330, "orderAddress":"Toronto, ON"}
```

```bash
confluent kafka topic consume orders --value-format avro --from-beginning
```

```
{"orderId":2123453,"orderTime":1682445330,"orderAddress":"Toronto, ON"}
{"orderId":2122453,"orderTime":1607641868,"orderAddress":"899 W Evelyn Ave, Mountain View, CA 94041"}
```

```bash
confluent kafka topic delete orders
```

```bash
confluent kafka cluster delete lkc-knrwgg
```

![Confluent CLI](/images/Confluent/ccloud-learn-kafka.png)

# Confluent REST Proxy

[Getting Started with Apache Kafka and Confluent REST Proxy \| Confluent Developer](https://developer.confluent.io/get-started/rest/)

```bash
docker compose -f rest-proxy.yml up -d
```

![docker compose rest-proxy.yml](/images/Confluent/docker_rest_proxy_yml.png)

![Seeing container appear in Docker Desktop](/images/Confluent/docker_desktop_rest_proxy_yml.png)

Create and consume three events for the `purchases` topic:

```bash
curl -X POST \
     -H "Content-Type: application/vnd.kafka.json.v2+json" \
     -H "Accept: application/vnd.kafka.v2+json" \
     --data '{"records":[{"key":"jsmith","value":"alarm clock"},{"key":"htanaka","value":"batteries"},{"key":"awalther","value":"bookshelves"}]}' \
     "http://localhost:8082/topics/purchases"
```

![purchases topic](/images/Confluent/purchases.png)