---
layout: post
title: BigQuery LAG, LEAD, OVER, PARTITION
topic: uscg-nais
---

[Navigation functions \| BigQuery Documentation](https://cloud.google.com/bigquery/docs/reference/standard-sql/navigation_functions)

```sql
CREATE OR REPLACE TABLE `ais-data-385301.uscg.vessel_port_max_stay` AS
WITH time_at_port AS (
    SELECT
        v.MMSI,
        v.BaseDateTime,
        p.WPI_Number,
        v.time_diff_minutes
    FROM 
        `ais-data-385301.uscg.nais_2022_timestamp_diff` AS v
    JOIN
        `ais-data-385301.nga.wpi_us_filtered` AS p
    ON
        ST_DWithin(v.vessel_geography, p.port_geography, 20000) -- distance within 20km
    WHERE
        v.time_diff_minutes >= 60  -- time difference is at least 1 hour
),
ordered_stays AS (
    SELECT *,
        LAG(WPI_Number) OVER (PARTITION BY MMSI ORDER BY BaseDateTime) AS last_port,
        LEAD(WPI_Number) OVER (PARTITION BY MMSI ORDER BY BaseDateTime) AS next_port
    FROM time_at_port
),
continuous_stays AS (
    SELECT *,
        SUM(CASE WHEN WPI_Number = last_port THEN 0 ELSE 1 END) OVER (PARTITION BY MMSI ORDER BY BaseDateTime) AS stay_group
    FROM ordered_stays
),
grouped_stays AS (
    SELECT 
        MMSI,
        WPI_Number,
        MIN(BaseDateTime) AS stay_start,
        MAX(BaseDateTime) AS stay_end,
        SUM(time_diff_minutes) AS total_duration
    FROM continuous_stays
    GROUP BY MMSI, WPI_Number, stay_group
)
SELECT *
FROM grouped_stays
WHERE total_duration >= 60
ORDER BY MMSI, stay_start;
```
