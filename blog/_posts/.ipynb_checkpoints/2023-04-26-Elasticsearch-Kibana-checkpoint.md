---
layout: post
title: Elasticsearch and Kibana
---

# Kibana Sample Data Flights

[Kibana Fundamentals \| Elastic](https://learn.elastic.co/)

[Kibana Fundamentals Lab Guide \| Elastic](https://www.elastic.co/pdf/kibana-fundamentals-additional-resources.pdf)

[How-to Series: Kibana \| Elastic](https://www.elastic.co/videos/training-how-to-series-stack)

```csv
timestamp,OriginCityName,DestCityName,Carrier,FlightDelayMin
"Apr 26, 2023 @ 11:58:20.000",Johannesburg,Sydney,"Kibana Airlines",255
"Apr 26, 2023 @ 11:53:34.000",Seoul,Hyderabad,"Kibana Airlines",360
"Apr 26, 2023 @ 11:50:34.000",Tokoname,Rome,"Logstash Airways",165
"Apr 26, 2023 @ 11:40:26.000",Bangor,"Jeju City","Logstash Airways",225
```

![Kibana Sample Data Flights](/images/Elastic/Kibana_Sample_Data_Flights.jpeg)

# Elastic Stack Geospatial

[Elastic Stack Geospatial](https://www.elastic.co/geospatial)

[Import geospatial data \| Kibana Guide](https://www.elastic.co/guide/en/kibana/current/import-geospatial-data.html)

# amychan331/json-to-geojson

We use [amychan331/json-to-geojson](https://github.com/amychan331/json-to-geojson) to convert `AIS_2023_04_20.json` to
`AIS_2023_04_20.geojson`. (See post on BarentsWatch AIS API.)

# Elastic Maps Service

Messages in `AIS_2023_04_20.geojson`:

![Points in AIS_2023_04_20.geojson](/images/Elastic/AIS_2023_04_20.jpeg)

Cluster map with hexagons, by message count:

![Cluster map with hexagons, by message count for AIS_2023_04_20.geojson](/images/Elastic/AIS_2023_04_20_cluster_hexagon.jpeg)

Applying filter `shipType : 80` (tankers):

![Filtering to tankers in AIS_2023_04_20.geojson](/images/Elastic/shipType_80.jpeg)