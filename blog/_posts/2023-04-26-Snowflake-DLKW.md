---
layout: post
title: Snowflake Datalake Workshop (DLKW)
---

[ESS-DLKW Badge 4: Data Lake Workshop](https://learn.snowflake.com)

# LISTAGG

```sql
SELECT * FROM mels_smoothie_challenge_db.trails.cherry_creek_trail;
```

```bash
head -n 5 results.csv
```

```csv
POINT_ID,TRAIL_NAME,LNG,LAT,COORD_PAIR
1,Cherry Creek Trail,-105.00836000,39.75430990,-105.00836000 39.75430990
2,Cherry Creek Trail,-105.00833000,39.75432000,-105.00833000 39.75432000
3,Cherry Creek Trail,-105.00830000,39.75429000,-105.00830000 39.75429000
4,Cherry Creek Trail,-105.00825000,39.75423000,-105.00825000 39.75423000
```

```bash
tail -n 1 results.csv
```

```
3526,Cherry Creek Trail,-104.75672000,39.38905000,-104.75672000 39.38905000
```

```sql
SELECT
'LINESTRING(' || listagg(coord_pair, ',')
WITHIN GROUP (
        ORDER BY
            point_id
    ) || ')' AS my_linestring
FROM cherry_creek_trail
WHERE point_id BETWEEN 1 and 10
GROUP BY trail_name;
```

We copy the query result to clipbard and use
[OpenStreetMap WKT Playground](https://clydedacruz.github.io/openstreetmap-wkt-playground/)

# OpenStreetMap WKT Playground

## First 10 points:

![OpenStreetMap WKT Playground: 10 points with LINESTRING](/images/Snowflake/OpenStreetMap_WKT_Playground_10_points.jpeg)

## First 20 points:

`WHERE point_id BETWEEN 1 and 20`

![OpenStreetMap WKT Playground: 20 points with LINESTRING](/images/Snowflake/OpenStreetMap_WKT_Playground_20_points.jpeg)

## All (3526) points:

Remove WHERE clause.

![OpenStreetMap WKT Playground: 3526 points with LINESTRING](/images/Snowflake/OpenStreetMap_WKT_Playground_3526_points.jpeg)