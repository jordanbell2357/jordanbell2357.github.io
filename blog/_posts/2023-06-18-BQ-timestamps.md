---
layout: post
title: BigQuery timestamps
topic: uscg-nais
---

Find days of 2022 for which we have not loaded daily CSV data file:

```sql
WITH all_dates AS (
  SELECT DATE(d) AS missing_date
  FROM UNNEST(GENERATE_DATE_ARRAY(DATE('2022-01-01'), DATE('2022-12-31'))) AS d
)
SELECT FORMAT_TIMESTAMP('%Y-%m-%d', missing_date) AS missing_dates
FROM all_dates
LEFT JOIN (
  SELECT DISTINCT DATE(BaseDateTime) AS existing_date
  FROM `ais-data-385301.uscg.nais`
  WHERE BaseDateTime >= TIMESTAMP('2022-01-01') AND BaseDateTime < TIMESTAMP('2023-01-01')
) AS existing_dates
ON all_dates.missing_date = existing_dates.existing_date
WHERE existing_dates.existing_date IS NULL
ORDER BY missing_dates;
```
