---
layout: post
title: Confluent
---

[Install the Confluent CLI \| Confluent Documentation](https://docs.confluent.io/confluent-cli/current/install.html)

[Quick Start for Confluent Cloud](https://docs.confluent.io/cloud/current/get-started/index.html)

[Streaming ETL and Analytics on Confluent with Maritime AIS Data. June 1, 2021. Robin Moffatt \| Confluent Technology Blog](https://www.confluent.io/blog/streaming-etl-and-analytics-for-real-time-location-tracking/)

[Console Producer and Consumer with (de)serializers](https://developer.confluent.io/tutorials/kafka-console-consumer-producer-avro/confluent.html)

```bash
curl -sL --http1.1 https://cnfl.io/cli | sh -s -- latest

export PATH="/home/$USER/bin:$PATH"
```

confluent login
confluent environment use env-pr0mzm
confluent kafka cluster use lkc-knrwgg
confluent api-key create --resource lkc-knrwgg

```
+------------+------------------------------------------------------------------+
| API Key    | HHLRFLOLBI656XMF                                                 |
| API Secret | e7dpO16zo5+UW6aPsvLpaRks+oFI42KXQPC0XhF5botneGYucJ8A9oxusKIrYmB7 |
+------------+------------------------------------------------------------------+
```

confluent api-key use HHLRFLOLBI656XMF --resource lkc-knrwgg

```
=== Confluent Cloud API key: lsrc-nw80nk ===

API key:
JPT6UFEOJPF4YSKE

API secret:
p9/U8tXCrJP7zXrtprucJyGiO5TwGXzCbD4BM61Fr6qsG2Jcsu+lelGlcPljEaMF
```

Use JPT6UFEOJPF4YSKE as API key when prompted in next command:

confluent kafka topic produce orders --value-format avro --schema "C:/Users/jorda/Downloads/schema-orders-value-v1.avsc"

{"orderId":2122453, "orderTime": 1607641868, "orderAddress":"899 W Evelyn Ave, Mountain View, CA 94041"}

confluent kafka topic consume orders --value-format avro --from-beginning


![Finish Getting Started with Schema Registry](/images/Confluent/Topics-Confluent-Cloud.png)