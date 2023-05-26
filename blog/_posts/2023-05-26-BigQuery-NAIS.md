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

```bash
for i in {01..30}; do \
bq load \
--autodetect \
--source_format=CSV \
AIS_2022_06_21_to_27.AIS_2022_06_${i} \
gs://jordanbell2357marinecadastre/AIS_2022_06_${i}.csv; \
done
```

The default value of the flag `max_bad_records` is 0. Running the above, we get the errors:

<pre>
Error while reading data, error message: Error detected while parsing row starting at position: 674418299. Error: Data between close quote character (") and field separator. File: gs://jordanbell2357marinecadastre/AIS_2022_06_08.csv

Error while reading data, error message: CSV processing encountered too many errors, giving up. Rows: 71085; errors: 1; max bad: 0; error percent: 0
</pre>

Invoking the flag `max_bad_records` and setting it equal to 10, as

```bash
for i in {01..30}; do \
bq load \
--autodetect \
--max_bad_records=10 \
--source_format=CSV \
AIS_2022_06_21_to_27.AIS_2022_06_${i} \
gs://jordanbell2357marinecadastre/AIS_2022_06_${i}.csv; \
done
```

we get the erorors:

<pre>
Error while reading data, error message: CSV table encountered too many errors, giving up. Rows: 551003; errors: 11. Please look into the errors[] collection for more details. File: gs://jordanbell2357marinecadastre/AIS_2022_06_08.csv

Error while reading data, error message: CSV processing encountered too many errors, giving up. Rows: 3036859; errors: 11; max bad: 10; error percent: 0

Error while reading data, error message: Error detected while parsing row starting at position: 674418299. Error: Data between close quote character (") and field separator. File: gs://jordanbell2357marinecadastre/AIS_2022_06_08.csv

Error while reading data, error message: Error detected while parsing row starting at position: 680437787. Error: Data between close quote character (") and field separator. File: gs://jordanbell2357marinecadastre/AIS_2022_06_08.csv

Error while reading data, error message: Error detected while parsing row starting at position: 685760530. Error: Data between close quote character (") and field separator. File: gs://jordanbell2357marinecadastre/AIS_2022_06_08.csv

Error while reading data, error message: Error detected while parsing row starting at position: 686876527. Error: Data between close quote character (") and field separator. File: gs://jordanbell2357marinecadastre/AIS_2022_06_08.csv

Error while reading data, error message: Error detected while parsing row starting at position: 689606906. Error: Data between close quote character (") and field separator. File: gs://jordanbell2357marinecadastre/AIS_2022_06_08.csv
</pre>

Likewise `max_bad_records=100` has errors.

It turns out that `max_bad_records=200` is large enough for all the CSV files to be loaded
from Cloud Storage to BigQuery (each table going from a CSV file on Cloud Storage to a table in
BigQuery loses at most 200 ("corrupt") rows.

```bash
for i in {01..30}; do \
bq load \
--autodetect \
--max_bad_records=200 \
--source_format=CSV \
AIS_2022_06_21_to_27.AIS_2022_06_${i} \
gs://jordanbell2357marinecadastre/AIS_2022_06_${i}.csv; \
done
```

# BigQuery SQL

The schema auto-detection for each CSV file `AIS_2022_06_21_to_27.AIS_2022_06_${i}` is

```json
[
  {
    "name": "MMSI",
    "mode": "NULLABLE",
    "type": "INTEGER",
    "description": null,
    "fields": []
  },
  {
    "name": "BaseDateTime",
    "mode": "NULLABLE",
    "type": "TIMESTAMP",
    "description": null,
    "fields": []
  },
  {
    "name": "LAT",
    "mode": "NULLABLE",
    "type": "FLOAT",
    "description": null,
    "fields": []
  },
  {
    "name": "LON",
    "mode": "NULLABLE",
    "type": "FLOAT",
    "description": null,
    "fields": []
  },
  {
    "name": "SOG",
    "mode": "NULLABLE",
    "type": "FLOAT",
    "description": null,
    "fields": []
  },
  {
    "name": "COG",
    "mode": "NULLABLE",
    "type": "FLOAT",
    "description": null,
    "fields": []
  },
  {
    "name": "Heading",
    "mode": "NULLABLE",
    "type": "FLOAT",
    "description": null,
    "fields": []
  },
  {
    "name": "VesselName",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": null,
    "fields": []
  },
  {
    "name": "IMO",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": null,
    "fields": []
  },
  {
    "name": "CallSign",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": null,
    "fields": []
  },
  {
    "name": "VesselType",
    "mode": "NULLABLE",
    "type": "INTEGER",
    "description": null,
    "fields": []
  },
  {
    "name": "Status",
    "mode": "NULLABLE",
    "type": "INTEGER",
    "description": null,
    "fields": []
  },
  {
    "name": "Length",
    "mode": "NULLABLE",
    "type": "INTEGER",
    "description": null,
    "fields": []
  },
  {
    "name": "Width",
    "mode": "NULLABLE",
    "type": "INTEGER",
    "description": null,
    "fields": []
  },
  {
    "name": "Draft",
    "mode": "NULLABLE",
    "type": "FLOAT",
    "description": null,
    "fields": []
  },
  {
    "name": "Cargo",
    "mode": "NULLABLE",
    "type": "INTEGER",
    "description": null,
    "fields": []
  },
  {
    "name": "TransceiverClass",
    "mode": "NULLABLE",
    "type": "STRING",
    "description": null,
    "fields": []
  }
]
```

# CREATE TABLE AS SELECT and UNION ALL

[Query syntax \| BigQuery](https://cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax)

[Data definition language (DDL) statements in GoogleSQL](https://cloud.google.com/bigquery/docs/reference/standard-sql/data-definition-language)

```sql
CREATE TABLE `ais-data-385301.NAIS.AIS_2022_06` AS
(
(SELECT MMSI,BaseDateTime,LAT,LON,SOG,COG,Heading,VesselType,Status,Length,Width FROM ais-data-385301.NAIS.AIS_2022_06_01)
UNION ALL
(SELECT MMSI,BaseDateTime,LAT,LON,SOG,COG,Heading,VesselType,Status,Length,Width FROM ais-data-385301.NAIS.AIS_2022_06_02)
UNION ALL
(SELECT MMSI,BaseDateTime,LAT,LON,SOG,COG,Heading,VesselType,Status,Length,Width FROM ais-data-385301.NAIS.AIS_2022_06_03)
UNION ALL
(SELECT MMSI,BaseDateTime,LAT,LON,SOG,COG,Heading,VesselType,Status,Length,Width FROM ais-data-385301.NAIS.AIS_2022_06_04)
UNION ALL
(SELECT MMSI,BaseDateTime,LAT,LON,SOG,COG,Heading,VesselType,Status,Length,Width FROM ais-data-385301.NAIS.AIS_2022_06_05)
UNION ALL
(SELECT MMSI,BaseDateTime,LAT,LON,SOG,COG,Heading,VesselType,Status,Length,Width FROM ais-data-385301.NAIS.AIS_2022_06_06)
UNION ALL
(SELECT MMSI,BaseDateTime,LAT,LON,SOG,COG,Heading,VesselType,Status,Length,Width FROM ais-data-385301.NAIS.AIS_2022_06_07)
UNION ALL
(SELECT MMSI,BaseDateTime,LAT,LON,SOG,COG,Heading,VesselType,Status,Length,Width FROM ais-data-385301.NAIS.AIS_2022_06_08)
UNION ALL
(SELECT MMSI,BaseDateTime,LAT,LON,SOG,COG,Heading,VesselType,Status,Length,Width FROM ais-data-385301.NAIS.AIS_2022_06_09)
UNION ALL
(SELECT MMSI,BaseDateTime,LAT,LON,SOG,COG,Heading,VesselType,Status,Length,Width FROM ais-data-385301.NAIS.AIS_2022_06_10)
UNION ALL
(SELECT MMSI,BaseDateTime,LAT,LON,SOG,COG,Heading,VesselType,Status,Length,Width FROM ais-data-385301.NAIS.AIS_2022_06_11)
UNION ALL
(SELECT MMSI,BaseDateTime,LAT,LON,SOG,COG,Heading,VesselType,Status,Length,Width FROM ais-data-385301.NAIS.AIS_2022_06_12)
UNION ALL
(SELECT MMSI,BaseDateTime,LAT,LON,SOG,COG,Heading,VesselType,Status,Length,Width FROM ais-data-385301.NAIS.AIS_2022_06_13)
UNION ALL
(SELECT MMSI,BaseDateTime,LAT,LON,SOG,COG,Heading,VesselType,Status,Length,Width FROM ais-data-385301.NAIS.AIS_2022_06_14)
UNION ALL
(SELECT MMSI,BaseDateTime,LAT,LON,SOG,COG,Heading,VesselType,Status,Length,Width FROM ais-data-385301.NAIS.AIS_2022_06_15)
UNION ALL
(SELECT MMSI,BaseDateTime,LAT,LON,SOG,COG,Heading,VesselType,Status,Length,Width FROM ais-data-385301.NAIS.AIS_2022_06_16)
UNION ALL
(SELECT MMSI,BaseDateTime,LAT,LON,SOG,COG,Heading,VesselType,Status,Length,Width FROM ais-data-385301.NAIS.AIS_2022_06_17)
UNION ALL
(SELECT MMSI,BaseDateTime,LAT,LON,SOG,COG,Heading,VesselType,Status,Length,Width FROM ais-data-385301.NAIS.AIS_2022_06_18)
UNION ALL
(SELECT MMSI,BaseDateTime,LAT,LON,SOG,COG,Heading,VesselType,Status,Length,Width FROM ais-data-385301.NAIS.AIS_2022_06_19)
UNION ALL
(SELECT MMSI,BaseDateTime,LAT,LON,SOG,COG,Heading,VesselType,Status,Length,Width FROM ais-data-385301.NAIS.AIS_2022_06_20)
UNION ALL
(SELECT MMSI,BaseDateTime,LAT,LON,SOG,COG,Heading,VesselType,Status,Length,Width FROM ais-data-385301.NAIS.AIS_2022_06_21)
UNION ALL
(SELECT MMSI,BaseDateTime,LAT,LON,SOG,COG,Heading,VesselType,Status,Length,Width FROM ais-data-385301.NAIS.AIS_2022_06_22)
UNION ALL
(SELECT MMSI,BaseDateTime,LAT,LON,SOG,COG,Heading,VesselType,Status,Length,Width FROM ais-data-385301.NAIS.AIS_2022_06_23)
UNION ALL
(SELECT MMSI,BaseDateTime,LAT,LON,SOG,COG,Heading,VesselType,Status,Length,Width FROM ais-data-385301.NAIS.AIS_2022_06_24)
UNION ALL
(SELECT MMSI,BaseDateTime,LAT,LON,SOG,COG,Heading,VesselType,Status,Length,Width FROM ais-data-385301.NAIS.AIS_2022_06_25)
UNION ALL
(SELECT MMSI,BaseDateTime,LAT,LON,SOG,COG,Heading,VesselType,Status,Length,Width FROM ais-data-385301.NAIS.AIS_2022_06_26)
UNION ALL
(SELECT MMSI,BaseDateTime,LAT,LON,SOG,COG,Heading,VesselType,Status,Length,Width FROM ais-data-385301.NAIS.AIS_2022_06_27)
UNION ALL
(SELECT MMSI,BaseDateTime,LAT,LON,SOG,COG,Heading,VesselType,Status,Length,Width FROM ais-data-385301.NAIS.AIS_2022_06_28)
UNION ALL
(SELECT MMSI,BaseDateTime,LAT,LON,SOG,COG,Heading,VesselType,Status,Length,Width FROM ais-data-385301.NAIS.AIS_2022_06_29)
UNION ALL
(SELECT MMSI,BaseDateTime,LAT,LON,SOG,COG,Heading,VesselType,Status,Length,Width FROM ais-data-385301.NAIS.AIS_2022_06_30)
);
```

Wrap the above in `CREATE TABLE AS SELECT`

The attributes MMSI, Status, VesselType, and Cargo are type integer. These integers are like ID numbers - they are not ordinal.

For further exploration, we cast these columns to type string.

```sql
-- Step 1: Create a new column with the desired string type
ALTER TABLE `ais-data-385301.NAIS.AIS_2022_06` ADD COLUMN new_column STRING;

-- Step 2: Update the new column by casting values from the original column to string
UPDATE `ais-data-385301.NAIS.AIS_2022_06`
SET new_column = CAST(Status AS STRING)
WHERE Status IS NOT NULL;

-- Step 3: Drop the original column
ALTER TABLE `ais-data-385301.NAIS.AIS_2022_06` DROP COLUMN Status;

-- Step 4: Rename the new column to match the name of the original column
ALTER TABLE `ais-data-385301.NAIS.AIS_2022_06` RENAME COLUMN new_column TO Status;
```

# Parameterized query

[Running parameterized queries](https://cloud.google.com/bigquery/docs/parameterized-queries#bq)

## Schema check

`schema_check.sql`:

```sql
DECLARE start_day INT64;
DECLARE end_day INT64;
DECLARE table_names ARRAY<STRING>;
DECLARE table_count INT64 DEFAULT 0;
DECLARE column_diffs ARRAY<STRUCT<column_name STRING, data_type STRING>>;

-- Generate the table names based on the start and end day parameters
SET table_names = ARRAY(
  SELECT CONCAT('ais-data-385301.NAIS.AIS_2022_06_', LPAD(CAST(day AS STRING), 2, '0'))
  FROM UNNEST(GENERATE_ARRAY(start_day, end_day)) AS day
);
SET table_count = ARRAY_LENGTH(table_names);

-- Check for schema differences
FOR table_name IN UNNEST(table_names) DO
  SET column_diffs = ARRAY(
    SELECT AS STRUCT column_name, data_type
    FROM `ais-data-385301.INFORMATION_SCHEMA.COLUMNS`
    WHERE table_name = table_name
    EXCEPT DISTINCT
    SELECT AS STRUCT column_name, data_type
    FROM UNNEST(column_diffs)
  );
END FOR;

-- Return the schema differences
SELECT column_name, data_type
FROM UNNEST(column_diffs);
```

```bash
bq query \
  --use_legacy_sql=false \
  --parameter='start_day:INT64:1' \
  --parameter='end_day:INT64:30' \
  --format=prettyjson \
  "$(cat schema_check.sql | tr '\n' ' ')"
```

Output:

<pre>
Waiting on bqjob_rda6f5245cf69416_00000188591dd105_1 ... (0s) Current status: DONE   
[]
</pre>

Therefore, the tables have identical schema.


## UNION ALL and CTAS

```bash
bq query --use_legacy_sql=false --parameter=start_day:INT64:1,end_day:INT64:30,table_name:STRING:'ais-data-385301.NAIS.AIS_2022_06' "$(cat parameterized_query.sql)"
```

`parameterized_query.sql`:

```sql
DECLARE start_day INT64 DEFAULT @start_day;
DECLARE end_day INT64 DEFAULT @end_day;
DECLARE table_name STRING DEFAULT @table_name;
DECLARE query_string STRING;

SET query_string = '';

FOR i IN start_day TO end_day DO
  SET query_string = CONCAT(query_string, 'SELECT MMSI, BaseDateTime, LAT, LON, SOG, COG, Heading, VesselType, Status, Length, Width FROM `', table_name, '_', LPAD(CAST(i AS STRING), 2, '0'), '` UNION ALL ');
END FOR;

-- Remove the trailing "UNION ALL" from the last subquery
SET query_string = SUBSTR(query_string, 1, LENGTH(query_string) - LENGTH(' UNION ALL '));

-- Create the final table using the dynamic query
EXECUTE IMMEDIATE CONCAT('CREATE TABLE `', table_name, '` AS (', query_string, ')');
```