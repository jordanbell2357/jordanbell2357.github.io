---
layout: post
title: Shanghai Containerized Freight Index (SCFI) (上海出口集装箱运价指数) using Gnuplot
---

[Shanghai Containerized Freight Index (SCFI) = 上海出口集装箱运价指数(SCFI)](https://en.sse.net.cn/home)

[![Shanghai Shipping Exchange](/images/SCFI/Shanghai-Shipping-Exchange.png)](https://en.sse.net.cn/indices/scfinew.jsp)

```bash
head -n 5 SCFI.csv
```

```
Week,SCFI
2009-10-16,1000
2009-10-23,1009.05
2009-10-30,1035.74
2009-11-06,1061.71
```

```bash
tail -n 5 SCFI.csv
```

```
2023-03-03,931.08
2023-03-10,906.55
2023-03-17,909.72
2023-03-24,908.35
2023-03-31,923.78
```

[Time/Date data \| Gnuplot](http://gnuplot.info/docs_5.5/loc4651.html)

`SCFI.gp`

```
set datafile separator ','
set timefmt '%Y-%m-%d'
set format x '%W-%Y'
set xdata time
set title 'Shanghai Containerized Freight Index (SCFI) 上海出口集装箱运价指数'
set xlabel 'Week-Year'
set ylabel 'Index'
plot for [col=2:2] 'SCFI.csv' using 1:col with linespoints title columnheader
```

![Shanghai Containerized Freight Index (SCFI) using Gnuplot](/images/SCFI/SCFI.png)