---
layout: post
title: BigQuery ST_GEOGPOINT
topic: uscg-nais
---

[Geography functions \| BigQuery Documentation](https://cloud.google.com/bigquery/docs/reference/standard-sql/geography_functions)

```sql
ALTER TABLE `ais-data-385301.uscg.nais_2022_nodups`
ADD COLUMN vessel_geography GEOGRAPHY;

UPDATE `ais-data-385301.uscg.nais_2022_nodups`
SET vessel_geography = ST_GEOGPOINT(LON, LAT)
WHERE LON IS NOT NULL AND LAT IS NOT NULL;
```

`This statement modified 2,965,744,033 rows in nais_2022_nodups.`

```sql
ALTER TABLE `ais-data-385301.nga.wpi_us`
ADD COLUMN port_geography GEOGRAPHY;

UPDATE `ais-data-385301.nga.wpi_us`
SET port_geography = ST_GEOGPOINT(Longitude, Latitude)
WHERE Longitude IS NOT NULL AND Latitude IS NOT NULL;
```

```sql
CREATE TABLE `ais-data-385301.uscg.nais_2022_simplified` AS
SELECT 
    MMSI, 
    BaseDateTime, 
    vessel_geography
FROM 
    `ais-data-385301.uscg.nais_2022_nodups`;
```

`This statement modified 666 rows in wpi_us.`

[Navigation functions \| BigQuery Documentation](https://cloud.google.com/bigquery/docs/reference/standard-sql/navigation_functions#lag)

```sql
CREATE TABLE `ais-data-385301.uscg.nais_2022_timestamp_diff` AS
SELECT
    MMSI,
    BaseDateTime,
    vessel_geography,
    TIMESTAMP_DIFF(
        BaseDateTime, 
        LAG(BaseDateTime) OVER (PARTITION BY MMSI ORDER BY BaseDateTime), 
        MINUTE
    ) AS time_diff_minutes
FROM 
    `ais-data-385301.uscg.nais_2022_simplified`;
```

```sql
CREATE TABLE `ais-data-385301.uscg.vessel_port_visit` AS
SELECT
    v.MMSI,
    v.BaseDateTime,
    p.Main_Port_Name,
    v.time_diff_minutes
FROM 
    `ais-data-385301.uscg.nais_2022_timestamp_diff` AS v
JOIN
    `ais-data-385301.nga.wpi_us_filtered` AS p
ON
    ST_DWithin(v.vessel_geography, p.port_geography, 20000) -- distance within 20km
WHERE
    v.time_diff_minutes >= 60  -- time difference is at least 1 hour
ORDER BY 
    v.MMSI, v.BaseDateTime;
```
