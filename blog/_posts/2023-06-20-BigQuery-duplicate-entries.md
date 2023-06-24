---
layout: post
title: BigQuery duplicate entries
topic: uscg-nais
---



<iframe src="https://docs.google.com/spreadsheets/d/e/2PACX-1vSl2M3TYzX_680dQLsTtoUjMmDFf14ZfPa6L9Xr7Ddj-67pT60qKCuClJjwqhrhOp6ij9H7qWX4FepN/pubhtml?gid=0&amp;single=true&amp;widget=true&amp;headers=false" width="100%" height="400"></iframe>

```sql
DELETE FROM `ais-data-385301.uscg.nais`
WHERE DATE(BaseDateTime) = '2022-01-23';
```

<iframe src="https://docs.google.com/spreadsheets/d/e/2PACX-1vSF0vY_ng_U__puWldyFqWhFygwLgSQUO2h72XL9UFuBAkTx9CpcKB6awf7z7XlYwR-m81BkGniIA_6/pubhtml?gid=0&amp;single=true&amp;widget=true&amp;headers=false" width="100%" height="400"></iframe>

```sql
CREATE TABLE `ais-data-385301.uscg.no_dups` AS
SELECT 
    *
FROM 
    (
        SELECT 
            *, 
            ROW_NUMBER() OVER(PARTITION BY MMSI, BaseDateTime ORDER BY MMSI) AS row_num 
        FROM 
            `ais-data-385301.uscg.nais`
    )
WHERE 
    row_num = 1;
```

```sql
CREATE TABLE `ais-data-385301.uscg.dups` AS
SELECT 
    *
FROM 
    (
        SELECT 
            *, 
            ROW_NUMBER() OVER(PARTITION BY MMSI, BaseDateTime ORDER BY MMSI) AS row_num 
        FROM 
            `ais-data-385301.uscg.nais`
    )
WHERE 
    row_num > 1;
```

```sql
SELECT COUNT(*) FROM `ais-data-385301.uscg.nais`;
```

`2966617246`

```sql
SELECT COUNT(*) FROM `ais-data-385301.uscg.no_dups`;
```

`2965744033`

```sql
SELECT COUNT(*) FROM `ais-data-385301.uscg.no_dups`;
```

`873213`


```bash
bq mk --time_partitioning_field BaseDateTime --time_partitioning_type DAY --schema MarineCadastre_schema.json ais-data-385301:uscg.nais_2022_partition_by_MMSI_and_BaseDateTime
```

```sql
INSERT INTO `ais-data-385301.uscg.nais_2022_partition_by_MMSI_and_BaseDateTime`
SELECT *
FROM `ais-data-385301.uscg.nais_2022_nodups`;
```
