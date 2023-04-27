---
layout: post
title: Snowflake Datalake Workshop DLKW
---

[ESS-DLKW Badge 4: Data Lake Workshop](https://learn.snowflake.com)

# LISTAGG

```sql
SELECT * FROM mels_smoothie_challenge_db.trails.cherry_creek_trail;
```

```bash
head results.csv
```

```csv
POINT_ID,TRAIL_NAME,LNG,LAT,COORD_PAIR
1,Cherry Creek Trail,-105.00836000,39.75430990,-105.00836000 39.75430990
2,Cherry Creek Trail,-105.00833000,39.75432000,-105.00833000 39.75432000
3,Cherry Creek Trail,-105.00830000,39.75429000,-105.00830000 39.75429000
4,Cherry Creek Trail,-105.00825000,39.75423000,-105.00825000 39.75423000
5,Cherry Creek Trail,-105.00818000,39.75404000,-105.00818000 39.75404000
6,Cherry Creek Trail,-105.00811000,39.75383000,-105.00811000 39.75383000
7,Cherry Creek Trail,-105.00811000,39.75383000,-105.00811000 39.75383000
8,Cherry Creek Trail,-105.00805000,39.75366000,-105.00805000 39.75366000
9,Cherry Creek Trail,-105.00800000,39.75352000,-105.00800000 39.75352000
```

```sql
SELECT
'LINESTRING(' || listagg(coord_pair, ',')
WITHIN GROUP (
        ORDER BY
            point_id
    ) || ')' AS my_linestring
FROM cherry_creek_trail
WHERE point_id BETWEEN 1 and 20
GROUP BY trail_name;
```

We copy the query result to clipbard and use
[OpenStreetMap WKT Playground](https://clydedacruz.github.io/openstreetmap-wkt-playground/)

# OpenStreetMap WKT Playground

## First 10 points:

![OpenStreetMap WKT Playground: 10 points with LINESTRING](/images/Snowflake/OpenStreetMap_WKT_Playground_10_points.jpeg)

## First 30 points:

![OpenStreetMap WKT Playground: 30 points with LINESTRING](/images/Snowflake/OpenStreetMap_WKT_Playground_30_points.jpeg)

## All (3527) points:

![OpenStreetMap WKT Playground: 3527 points with LINESTRING](/images/Snowflake/OpenStreetMap_WKT_Playground_3527_points.jpeg)