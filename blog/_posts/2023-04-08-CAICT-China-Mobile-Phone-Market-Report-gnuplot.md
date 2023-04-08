---
layout: post
title: CAICT China Mobile Phone Market Report using Gnuplot
---

[中国信息通信研究院 (中国信通院)](http://www.caict.ac.cn/)

[China Academy of Information and Communications Technology (CAICT)](http://www.caict.ac.cn/english/)

[China Mobile Phone Market Report](http://www.caict.ac.cn/english/research/rs/)

<iframe src="https://docs.google.com/spreadsheets/d/e/2PACX-1vTUnPnud1-VdSYwXB4-myv2qKcNXLMeFLd2QlPEBs4WPQ9eoU7NiUmwGmozU7nbkKRzVSys-X-5z2hZ/pubhtml?widget=true&amp;headers=false" width="100%" height="600"></iframe>

```bash
head -n 5 CAICT.csv
```

```
Month,CN: Mobile Phone: Shipment: Smart Phone (million),CN: Mobile Phone: Shipment (million),CN: Mobile Phone: Shipment: Local Brand (million),CN: Mobile Phone: Shipment: 5G (million),CN: Mobile Phone: Shipment: 4G (million),CN: Mobile Phone: Shipment: 3G (million),CN: Mobile Phone: Shipment: 2G (million)
2012-01-01,11.023,24.006,,,,13.345,10.661
2012-02-01,12.695,29.989,,,,15.034,14.955
2012-03-01,17.451,39.586,29.427,,,20.350,19.236
2012-04-01,18.114,35.287,27.263,,,19.984,15.303
```

```bash
tail -n 5 CAICT.csv
```

```
2020-04-01,40.782,41.728,37.982,16.382,,,
2020-05-01,32.661,33.759,30.970,15.643,,,
2020-06-01,27.706,28.630,27.283,17.513,,,
2020-07-01,21.256,22.301,20.724,13.911,,,
2020-08-01,25.624,26.907,24.432,16.170,,,
2020-09-01,22.001,23.334,21.563,13.990,,,
2020-10-01,25.014,26.153,20.322,16.760,,,
2020-11-01,27.710,29.584,20.680,20.136,,,
2020-12-01,25.218,26.595,20.553,18.200,,,
2021-01-01,39.572,40.120,33.726,27.278,,,
```

[Time/date specifiers \| Gnuplot](http://www.gnuplot.info/docs_4.2/node185.html)

`CAICT.gp`

```
set datafile separator ','
set timefmt '%Y-%m-%d'
set format x '%m/%y'
set xdata time
set title 'CAICT China Mobile Phone Market Report'
set xlabel 'Month'
set ylabel 'Million/month'
plot for [col=2:8] 'CAICT.csv' using 1:col with lines title columnheader
```

![CAICT China Mobile Phone Market Report](/images/CAICT/CAICT_China_Mobile_Phone_Market_Report.png)