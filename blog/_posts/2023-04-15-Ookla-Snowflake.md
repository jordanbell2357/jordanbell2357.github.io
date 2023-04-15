---
layout: post
title: Ookla Global Fixed Broadband Open Data on Snowflake
---

[Global Fixed Broadband Open Data](https://app.snowflake.com/marketplace/listing/GZSTZ107UL27/ookla-global-fixed-broadband-open-data?available=available)

> Global fixed broadband and mobile (cellular) network performance, allocated to zoom level 16 web mercator tiles (approximately 610.8 meters by 610.8 meters at the equator). Data is provided in both Shapefile format as well as Apache Parquet with geometries represented in Well Known Text (WKT) projected in EPSG:4326. Download speed, upload speed, and latency are collected via the Speedtest by Ookla applications for Android and iOS and averaged for each tile. Measurements are filtered to results containing GPS-quality location accuracy.
>
> Speedtest by Ookla Global Fixed and Mobile Network Performance Maps was accessed on DATE from https://registry.opendata.aws/speedtest-global-performance. Speedtest® by Ookla® Global Fixed and Mobile Network Performance Maps. Based on analysis by Ookla of Speedtest Intelligence® data for [DATA TIME PERIOD]. Provided by Ookla and accessed [DAY MONTH YEAR]. Ookla trademarks used under license and reprinted with permission.
>
> Tile Attributes
>
> Each tile contains the following adjoining attributes:
>
> - Field Name Type Description
> - avg_d_kbps Integer The average download speed of all tests performed in the tile, represented in kilobits per second.
> - avg_u_kbps Integer The average upload speed of all tests performed in the tile, represented in kilobits per second.
> - avg_lat_ms Integer The average latency of all tests performed in the tile, represented in milliseconds
> - tests Integer The number of tests taken in the tile.
> - devices Integer The number of unique devices contributing tests in the tile.
> - quadkey Text The quadkey representing the tile.

````
GLOBAL_FIXED_BROADBAND_OPEN_DATA / PUBLIC / OPEN_OOKLA_BROADBAND__2022_07_01_PERFORMANCE_FIXED_TILES_2022_07_01_PERFORMANCE_FIXED_TILES
```

![Table preview](/images/Ookla/OPEN_OOKLA_BROADBAND__2022_07_01_PERFORMANCE_FIXED_TILES_2022_07_01_PERFORMANCE_FIXED_TILES-Table.png)

```sql
SELECT * FROM OPEN_OOKLA_BROADBAND__2022_07_01_PERFORMANCE_FIXED_TILES_2022_07_01_PERFORMANCE_FIXED_TILES;
```

![Global Fixed Broadband Open Data](/images/Ookla/Global-Fixed-Broadband-Open-Data-Usage-Example-Snowflake.png)

`OPEN_OOKLA_BROADBAND__2022_07_01_PERFORMANCE_FIXED_TILES_2022_07_01_PERFORMANCE_FIXED_TILES.csv`

`head -n 5`

```
QUADKEY,TILE,AVG_D_KBPS,AVG_U_KBPS,AVG_LAT_MS,TESTS,DEVICES,__HEVO_ID,__HEVO__INGESTED_AT,__HEVO__LOADED_AT,__HEVO__MARKED_DELETED
23200000000000,"POLYGON((-157.428588867188 70.4827310882277, -157.423095703125 70.4827310882277, -157.423095703125 70.4808957888748, -157.428588867188 70.4808957888748, -157.428588867188 70.4827310882277))",2004,612,103,2,1,69,1667600267702,1667600363517,FALSE
23200000000000,"POLYGON((-148.86474609375 70.3131876426957, -148.859252929688 70.3131876426957, -148.859252929688 70.3113370300076, -148.86474609375 70.3113370300076, -148.86474609375 70.3131876426957))",112348,91928,18,1,1,100,1667600267710,1667600363517,FALSE
23200000000000,"POLYGON((-149.205322265625 70.3002298451582, -149.199829101562 70.3002298451582, -149.199829101562 70.2983780627737, -149.205322265625 70.2983780627737, -149.205322265625 70.3002298451582))",23535,40771,22,4,3,91,1667600267708,1667600363517,FALSE
23200000000000,"POLYGON((-148.474731445312 70.3372304111597, -148.46923828125 70.3372304111597, -148.46923828125 70.3353819690557, -148.474731445312 70.3353819690557, -148.474731445312 70.3372304111597))",7997,36370,35,2,1,102,1667600267711,1667600363517,FALSE
```

