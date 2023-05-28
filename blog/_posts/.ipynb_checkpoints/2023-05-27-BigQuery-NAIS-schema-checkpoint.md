---
layout: post
title: USCG NAIS National AIS at 1 Minute Intervals CSV schema for BigQuery
topic: uscg-nais
toc: true
---

{% include toc.html %}

Office for Coastal Management, 2023: Nationwide Automatic Identification System 2022, <https://www.fisheries.noaa.gov/inport/item/67336>. GUID: gov.noaa.nmfs.inport:67336. Updated: February 6, 2023.

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

`MarineCadastre_schema.json`

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
    "mode": "REQUIRED",
    "name": "SOG",
    "type": "FLOAT"
  },
  {
    "description": "degrees. Course Over Ground",
    "mode": "REQUIRED",
    "name": "COG",
    "type": "FLOAT"
  },
  {
    "description": "degrees. True heading angle",
    "mode": "REQUIRED",
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
    "mode": "REQUIRED",
    "name": "TransceiverClass",
    "type": "STRING"
  }
]
```
 
[bq command-line tool reference](https://cloud.google.com/bigquery/docs/reference/bq-cli-reference)

# bq mk

```bash
bq mk --table --schema=MarineCadastre_schema.json uscg.nais
```

# bq show

```bash
bq show --schema --format=prettyjson ais-data-385301:uscg.nais
```

```bash
bq show --schema --format=prettyjson ais-data-385301:uscg.nais | diff MarineCadastre_schema.json -
```

# bq load

```bash
for i in {01..30}; do \
bq load \
--source_format=CSV \
--max_bad_records=200 \
--schema=MarineCadastre_schema.json \
uscg.nais \
gs://jordanbell2357marinecadastre/AIS_2022_06_${i}.csv; \
done
```

`max_bad_records=200` is chosen because `max_bad_records=100` fails. (That is, at least one daily CSV file has have more than
100 records not fitting the schema `MarineCadastre_schema.json`, but there is no daily CSV file with more than 200 records not fitting the schema.)

## bq query

```bash
bq query --use_legacy_sql=false 'SELECT COUNT(*) FROM ais-data-385301.uscg.nais;'
```

<pre>249325885</pre>

<pre>249 million 325 thousand 885 messages</pre>