---
layout: post
title: Elasticsearch and Kibana
---

[Kibana Fundamentals \| Elastic](https://learn.elastic.co/)

[Kibana Fundamentals Lab Guide \| Elastic](https://www.elastic.co/pdf/kibana-fundamentals-additional-resources.pdf)

Sample flight data:

![Sample Flight Data](/images/Elastic/SampleFlightData.png)

[How-to Series: Kibana \| Elastic](https://www.elastic.co/videos/training-how-to-series-stack)

```csv
timestamp,OriginCityName,DestCityName,Carrier,FlightDelayMin
"Apr 26, 2023 @ 11:58:20.000",Johannesburg,Sydney,"Kibana Airlines",255
"Apr 26, 2023 @ 11:53:34.000",Seoul,Hyderabad,"Kibana Airlines",360
"Apr 26, 2023 @ 11:50:34.000",Tokoname,Rome,"Logstash Airways",165
"Apr 26, 2023 @ 11:40:26.000",Bangor,"Jeju City","Logstash Airways",225
```

<iframe src="https://jordanbell2357.kb.us-central1.gcp.cloud.es.io:9243/app/dashboards#/view/fc61cdc0-e453-11ed-9f76-df3071b81ff4?embed=true&_g=(refreshInterval:(pause:!t,value:60000),time:(from:now-10d,to:now))&_a=()" height="600" width="800"></iframe>
