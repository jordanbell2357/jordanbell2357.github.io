---
layout: post
title: "CMA: Active Physicians by Country of MD Graduation, Canada, 2008-2019"
---

[Canadian Medical Association (CMA) Physician Data Centre](https://www.cma.ca/physician-data-centre)

[Physicians by country of MD graduation, Canada, 2008-2019](https://www.cma.ca/sites/default/files/2019-11/2019-10-phys-by-country.pdf)

We copy the tables from `2019-10-phys-by-country.pdf` using [Tabula](https://tabula.technology/).

<iframe src="https://docs.google.com/spreadsheets/d/e/2PACX-1vQYGHxiQ4naBwSqQ_QEYk3e6pNgN-RY8kUQelIypd8-fpy9Cm2H_dsFbJxq5RoEZN1OP5r_E_SDKv0E/pubhtml?widget=true&amp;headers=false" width="100%" height="600"></iframe>

```
set datafile separator ','
set timefmt '%Y'
set format x '%Y'
set xdata time
set title 'Active Physicians by Country of MD Graduation, Canada, 2008-2019 (CMA 2019)'
set xlabel 'Year'
set ylabel 'Active Physicians'
plot 'CMA_2019.csv' using 1:2 with linespoints title columnheader, \
'CMA_2019.csv' using 1:3 with linespoints title columnheader, \
'CMA_2019.csv' using 1:6 with linespoints title columnheader, \
'CMA_2019.csv' using 1:14 with linespoints title columnheader, \
'CMA_2019.csv' using 1:30 with linespoints title columnheader, \
'CMA_2019.csv' using 1:42 with linespoints title columnheader, \
'CMA_2019.csv' using 1:71 with linespoints title columnheader, \
'CMA_2019.csv' using 1:88 with linespoints title columnheader, \
'CMA_2019.csv' using 1:128 with linespoints title columnheader, \
'CMA_2019.csv' using 1:153 with linespoints title columnheader, \
'CMA_2019.csv' using 1:157 with linespoints title columnheader, \
'CMA_2019.csv' using 1:162 with linespoints title columnheader, \
'CMA_2019.csv' using 1:163 with linespoints title columnheader
```

![Active Physicians by Country of MD Graduation, Canada, 2008-2019: World](/images/CMA/A.png)

![Active Physicians by Country of MD Graduation, Canada, 2008-2019: Other than North America](/images/CMA/B.png)

![Active Physicians by Country of MD Graduation, Canada, 2008-2019: North America](/images/CMA/C.png)