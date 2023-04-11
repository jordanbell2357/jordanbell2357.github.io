---
layout: post
title: Association of Faculties of Medicine of Canada (AFMC)
---

[Association of Faculties of Medicine of Canada (AFMC)](https://www.afmc.ca/)

[Canadian Medical Education Statistics (CMES)](https://www.afmc.ca/resources-data/data/canadian-medical-education-statistics-cmes/)

> Canadian Medical Education Statistics is the collection of information gathered from surveys distributed by the AFMC. The publication is released annually in the Spring.
>
> AFMC is the source of information on physician info and output through Canada’s undergraduate and postgraduate training system, the amount and types of doctors trained and how they are distributed and move throughout Canada. AFMC also gathers data pertaining to our faculties of medicine such as their faculty compliments, curriculum offerings, tuition fees, and research revenues. The data available in Canadian Medical Education Statistics are used by the Canadian faculties of medicine, the federal government, provincial/territorial ministries of health, and private industries as well as AFMC’s constituents.

`CMES-2021-Complete-EN.pdf`

Use [Tabula](https://tabula.technology/)

> Table H-1 MD Degrees Awarded by Canadian Universities by Sex of Graduates 1992 to 2021

<iframe src="https://docs.google.com/spreadsheets/d/e/2PACX-1vQfV54Wstj3i7CjqxRMBe8REnbBYuWuEkmOYsPncxQO-hCBNn1vC4cNZZJtKmYejg_XrkIAWnsdLKFv/pubhtml?widget=true&amp;headers=false"></iframe>

```
Year,Male,Female,Total,% Female
1992,983,766,1749,43.8
1993,979,723,1702,42.5
1994,939,747,1686,44.3
1995,948,791,1739,45.5
1996,842,843,1685,50.0
1997,783,794,1577,50.3
1998,828,776,1604,48.4
1999,756,838,1594,52.6
2000,796,782,1578,49.6
2001,766,771,1537,50.2
2002,770,773,1543,50.1
2003,794,865,1659,52.1
2004,818,938,1756,53.4
2005,758,1119,1877,59.6
2006,803,1154,1957,59.0
2007,846,1200,2046,58.7
2008,917,1205,2122,56.8
2009,999,1339,2338,57.3
2010,1019,1428,2447,58.4
2011,1080,1446,2526,57.2
2012,1102,1542,2643,58.3
2013,1140,1518,2658,57.1
2014,1213,1582,2795,56.6
2015,1261,1552,2813,55.2
2016,1294,1553,2847,54.5
2017,1214,1597,2811,56.8
2018,1302,1561,2863,54.5
2019,1288,1568,2856,54.9
2020,1237,1639,2876,57.0
2021,1235,1626,2861,56.8
```

Gnuplot:

```
set datafile separator ','
set timefmt '%Y'
set format x '%Y'
set xdata time
set title 'CMES2021. MD Degrees Awarded by Canadian Universities by Sex of Graduates 1992 to 2021'
set xlabel 'Year'
set ylabel 'MD Degrees Awarded by Canadian Universities'
plot for [col=2:4] 'H1.csv' using 1:col with linespoints title columnheader
```

![CMES2021. Table H-1: MD Degrees Awarded by Canadian Universities by Sex of Graduates 1992 to 2021](/images/AFMC/H1.png)