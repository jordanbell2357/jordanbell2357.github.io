---
layout: post
title: Confluent
---

[Install the Confluent CLI \| Confluent Documentation](https://docs.confluent.io/confluent-cli/current/install.html)

```bash
cd ~/

curl -sL --http1.1 https://cnfl.io/cli | sh -s -- latest

export PATH="/home/$USER/bin:$PATH"
```

---

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

---

[Quick Start for Confluent Cloud](https://docs.confluent.io/cloud/current/get-started/index.html)

[Streaming ETL and Analytics on Confluent with Maritime AIS Data. June 1, 2021. Robin Moffatt \| Confluent Technology Blog](https://www.confluent.io/blog/streaming-etl-and-analytics-for-real-time-location-tracking/)

[Console Producer and Consumer with (de)serializers](https://developer.confluent.io/tutorials/kafka-console-consumer-producer-avro/confluent.html)