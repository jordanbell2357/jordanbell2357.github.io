---
layout: post
title: National AIS at 1 Minute Intervals Data on BigQuery
topic: uscg-nais
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

# Schema

[Specifying a schema](https://cloud.google.com/bigquery/docs/schemas)

`AIS_2022_06.json`

```json
[
  {
    "description": "Maritime Mobile Service Identity value",
    "mode": "REQUIRED",
    "name": "MMSI",
    "type": "STRING"
  },
  {
    "description": "Full UTC date and time",
    "mode": "REQUIRED",
    "name": "BaseDateTime",
    "type": "TIMESTAMP"
  },
  {
    "description": "decimal degrees. Latitude",
    "mode": "REQUIRED",
    "name": "LAT",
    "type": "FLOAT"
  },
  {
    "description": "decimal degrees. Longitude",
    "mode": "REQUIRED",
    "name": "LON",
    "type": "FLOAT"
  },
  {
    "description": "knots. Speed Over Ground",
    "mode": "NULLABLE",
    "name": "SOG",
    "type": "FLOAT"
  },
  {
    "description": "degrees. Course Over Ground",
    "mode": "NULLABLE",
    "name": "COG",
    "type": "FLOAT"
  },
  {
    "description": "degrees. True heading angle",
    "mode": "NULLABLE",
    "name": "Heading",
    "type": "FLOAT"
  },
  {
    "description": "Name as shown on the station radio license",
    "mode": "NULLABLE",
    "name": "VesselName",
    "type": "STRING"
  },
  {
    "description": "International Maritime Organization Vessel number",
    "mode": "NULLABLE",
    "name": "IMO",
    "type": "STRING"
  },
  {
    "description": "Call sign as assigned by FCC",
    "mode": "NULLABLE",
    "name": "CallSign",
    "type": "STRING"
  },
  {
    "description": "Vessel type as defined in NAIS specifications",
    "mode": "NULLABLE",
    "name": "VesselType",
    "type": "STRING"
  },
  {
    "description": "Navigation status as defined by the COLREGS",
    "mode": "NULLABLE",
    "name": "Status",
    "type": "STRING"
  },
  {
    "description": "Length of vessel (see NAIS specifications)",
    "mode": "NULLABLE",
    "name": "Length",
    "type": "FLOAT"
  },
  {
    "description": "Width of vessel (see NAIS specifications)",
    "mode": "NULLABLE",
    "name": "Width",
    "type": "FLOAT"
  },
  {
    "description": "Draft depth of vessel (see NAIS specifications)",
    "mode": "NULLABLE",
    "name": "Draft",
    "type": "FLOAT"
  },
  {
    "description": "Cargo type (see NAIS specification and codes)",
    "mode": "NULLABLE",
    "name": "Cargo",
    "type": "STRING"
  },
  {
    "description": "Class of AIS transceiver",
    "mode": "NULLABLE",
    "name": "TransceiverClass",
    "type": "STRING"
  }
]
```
 
[bq command-line tool reference](https://cloud.google.com/bigquery/docs/reference/bq-cli-reference)

# bq mk

```bash
bq mk --table --schema=AIS_2022_06.json uscg_nais.ais_2022_06
```

# bq show

```bash
bq show --schema --format=prettyjson ais-data-385301:uscg_nais.ais_2022_06
```

```bash
bq show --schema --format=prettyjson ais-data-385301:uscg_nais.ais_2022_06 | diff AIS_2022_06.json -
```

# bq load

```bash
for i in {01..30}; do \
bq load \
--source_format=CSV \
--max_bad_records=200 \
--schema=AIS_2022_06.json \
uscg_nais.ais_2022_06 \
gs://jordanbell2357marinecadastre/AIS_2022_06_${i}.csv; \
done
```

## bq query

```bash
bq query --use_legacy_sql=false 'SELECT COUNT(*) FROM ais-data-385301.uscg_nais.ais_2022_06;'
```

<pre>249325885</pre>


<pre>249 million 325 thousand 885 messages</pre>