---
layout: post
title: MarineCadastre.gov AIS data on BigQuery
topic: MarineCadastre
---

# curl

```bash
for i in {01..30}; do \
curl -O https://coast.noaa.gov/htdata/CMSP/AISDataHandler/2022/AIS_2022_06_${i}.zip; \
unzip AIS_2022_06_${i}.zip; \
rm AIS_2022_06_${i}.zip;
done
```

# gsutil

```bash
for i in {01..30}; do \
gsutil cp AIS_2022_06_${i}.csv gs://jordanbell2357marinecadastre/; \
rm AIS_2022_06_${i}.csv; \
done
```

# bq

[bq command-line tool reference](https://cloud.google.com/bigquery/docs/reference/bq-cli-reference)

[Specifying a schema](https://cloud.google.com/bigquery/docs/schemas)

```bash
for i in {01..30}; do \
bq load \
--source_format=CSV \
NAIS.AIS_2022_06_${i} \
gs://jordanbell2357marinecadastre/AIS_2022_06_${i}.csv; \
done
```
