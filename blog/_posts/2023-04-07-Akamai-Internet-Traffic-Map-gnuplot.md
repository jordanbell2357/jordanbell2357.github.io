---
layout: post
title: Akamai Internet Traffic Map using Gnuplot
---

[Internet Traffic Map](https://www.akamai.com/internet-station/traffic-map)

![DNS trends and traffic](/images/Akamai/DNS_trends_and_traffic.png)

<https://www.akamai.com/dv/traffic/dns-trends-traffic/dns_total_traffic_trend.json>

`dns_total_traffic_trend.json`

`dns.csv`

```
Date,DNS Total Traffic Trend (G)
2016-01-01,59412125812
2016-01-02,59686411092
2016-01-03,58831870867
2016-01-04,68714275506
```

```
set datafile separator ','
set timefmt '%Y-%m-%d'
set format x '%Y'
set xdata time
set title 'Akamai Internet Traffic Map. ©2023 Akamai Technologies'
set xlabel 'Date'
set ylabel 'G'
plot for [col=2:2] 'dns.csv' using 1:col with lines title columnheader
```

![DNS trends and traffic using Gnuplot](/images/Akamai/dns.png)