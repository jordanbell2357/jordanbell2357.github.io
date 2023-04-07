---
layout: post
title: DHL Global Connectedness Index (GCI) with Gnuplot
---

# DHL Global Connectedness Index (GCI)

[DHL Global Connectedness Index (GCI)](https://www.dhl.com/global-en/delivered/globalization/global-connectedness-index.html)

[DHL Global Connectedness Index \| NYU Stern](https://www.stern.nyu.edu/experience-stern/about/departments-centers-initiatives/centers-of-research/center-future-management/dhl-initiative-globalization/dhl-global-connectedness-index)

{% assign table_rows1 = site.data.DHL_GCI %}

<div style="overflow-x:auto;">
  <table>
      {% for row in table_rows1 %}
          {% if forloop.first %}
              <tr>
                  {% for pair in row %}
                      <th>
                          {{ pair[0] }}
                      </th>
                  {% endfor %}
              </tr>
          {% endif %}

          {% tablerow pair in row %}
              {{ pair[1] }}
          {% endtablerow %}
      {% endfor %}
  </table>
</div>

# Gnuplot

```
head -n 5 DHL_GCI.csv
```

```
year,overall,trade,people,capital,information
2001,100,100,100,100,100
2002,97.9827,100.3042,100.9841,92.2775,102.8764
2003,101.8877,101.8284,101.5175,99.617,107.6942
2004,107.3731,105.9474,102.9709,106.1532,117.948
```

[Time/Date data \| Gnuplot](http://gnuplot.info/docs_5.5/loc4651.html)

`DHL_GCI.gp`

```
set datafile separator ','
set timefmt '%Y'
set format x '%Y'
set xdata time
set title 'DHL Global Connectedness Index (GCI)'
set xlabel 'Year'
set ylabel 'Index'
plot for [col=2:5] 'DHL_GCI.csv' using 1:col with linespoints title columnheader
```

```bash
gnuplot -p DHL_GCI.gp
```

![DHL Global Connectedness Index (GCI) with Gnuplot](/images/DHL/DHL_GCI.png)