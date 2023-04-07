---
layout: post
title: Ericsson Mobility Report November 2022 using Gnuplot
---

[Ericsson Mobility Report November 2022](https://www.ericsson.com/en/reports-and-papers/mobility-report)

[Mobility Visualizer](https://www.ericsson.com/en/reports-and-papers/mobility-report/mobility-visualizer)

`Ericsson.csv`

```
Year,Region,Technology,Device,Million
2028,World Total,WCDMA/HSPA,Smartphones,60.286
2028,World Total,LTE,Smartphones,3135.245
2028,World Total,5G,Smartphones,4665.431
2027,World Total,WCDMA/HSPA,Smartphones,71.384
2027,World Total,LTE,Smartphones,3753.992
2027,World Total,5G,Smartphones,3843.965
2026,World Total,WCDMA/HSPA,Smartphones,82.162
2026,World Total,LTE,Smartphones,4150.04
2026,World Total,5G,Smartphones,3223.059
2025,World Total,CDMA,Smartphones,0.492
2025,World Total,WCDMA/HSPA,Smartphones,215.187
2025,World Total,LTE,Smartphones,4392.227
2025,World Total,5G,Smartphones,2662.503
2024,World Total,CDMA,Smartphones,1.622
2024,World Total,WCDMA/HSPA,Smartphones,444.072
2024,World Total,LTE,Smartphones,4604.085
2024,World Total,5G,Smartphones,2095.384
2023,World Total,CDMA,Smartphones,2.177
2023,World Total,WCDMA/HSPA,Smartphones,600.692
2023,World Total,LTE,Smartphones,4757.083
2023,World Total,5G,Smartphones,1539.193
2022,World Total,CDMA,Smartphones,2.898
2022,World Total,WCDMA/HSPA,Smartphones,798.186
2022,World Total,LTE,Smartphones,4818.558
2022,World Total,5G,Smartphones,978.245
2021,World Total,CDMA,Smartphones,3.465
2021,World Total,WCDMA/HSPA,Smartphones,1035.789
2021,World Total,LTE,Smartphones,4705.841
2021,World Total,5G,Smartphones,516.938
2020,World Total,CDMA,Smartphones,3.848
2020,World Total,WCDMA/HSPA,Smartphones,1237.535
2020,World Total,LTE,Smartphones,4447.034
2020,World Total,5G,Smartphones,154.257
2019,World Total,Other technologies,Smartphones,0.852
2019,World Total,CDMA,Smartphones,5.593
2019,World Total,GSM/EDGE,Smartphones,4.909
2019,World Total,WCDMA/HSPA,Smartphones,1427.243
2019,World Total,LTE,Smartphones,4052.114
2019,World Total,5G,Smartphones,12.48
2018,World Total,Other technologies,Smartphones,0.007
2018,World Total,CDMA,Smartphones,18.745
2018,World Total,TD-SCDMA,Smartphones,15.189
2018,World Total,GSM/EDGE,Smartphones,14.142
2018,World Total,WCDMA/HSPA,Smartphones,1588.503
2018,World Total,LTE,Smartphones,3320.887
2018,World Total,5G,Smartphones,0.11
2017,World Total,Other technologies,Smartphones,0.017
2017,World Total,CDMA,Smartphones,19.671
2017,World Total,TD-SCDMA,Smartphones,5.218
2017,World Total,GSM/EDGE,Smartphones,29.47
2017,World Total,WCDMA/HSPA,Smartphones,1737.411
2017,World Total,LTE,Smartphones,2560.621
2016,World Total,Other technologies,Smartphones,0.021
2016,World Total,CDMA,Smartphones,47.903
2016,World Total,TD-SCDMA,Smartphones,8.804
2016,World Total,GSM/EDGE,Smartphones,42.539
2016,World Total,WCDMA/HSPA,Smartphones,1709.369
2016,World Total,LTE,Smartphones,1807.711
2015,World Total,Other technologies,Smartphones,0.779
2015,World Total,CDMA,Smartphones,163.216
2015,World Total,TD-SCDMA,Smartphones,54.605
2015,World Total,GSM/EDGE,Smartphones,82.218
2015,World Total,WCDMA/HSPA,Smartphones,1633.939
2015,World Total,LTE,Smartphones,1037.676
2014,World Total,Other technologies,Smartphones,1.335
2014,World Total,CDMA,Smartphones,199.363
2014,World Total,TD-SCDMA,Smartphones,244.355
2014,World Total,GSM/EDGE,Smartphones,117.699
2014,World Total,WCDMA/HSPA,Smartphones,1242.858
2014,World Total,LTE,Smartphones,468.882
2013,World Total,Other technologies,Smartphones,1.519
2013,World Total,CDMA,Smartphones,215.727
2013,World Total,TD-SCDMA,Smartphones,199.906
2013,World Total,GSM/EDGE,Smartphones,104.228
2013,World Total,WCDMA/HSPA,Smartphones,983.716
2013,World Total,LTE,Smartphones,187.265
2012,World Total,Other technologies,Smartphones,1.588
2012,World Total,CDMA,Smartphones,186.898
2012,World Total,TD-SCDMA,Smartphones,93.539
2012,World Total,GSM/EDGE,Smartphones,77.82
2012,World Total,WCDMA/HSPA,Smartphones,719.859
2012,World Total,LTE,Smartphones,71.099
2011,World Total,Other technologies,Smartphones,3.477
2011,World Total,CDMA,Smartphones,109.749
2011,World Total,TD-SCDMA,Smartphones,54.17
2011,World Total,GSM/EDGE,Smartphones,98.263
2011,World Total,WCDMA/HSPA,Smartphones,432.119
2011,World Total,LTE,Smartphones,9.252
```

```bash
grep 5G Ericsson.csv | cut -d ',' -f 1,5 > 5G.csv
grep LTE Ericsson.csv | cut -d ',' -f 1,5 > LTE.csv
grep WCDMA/HSPA Ericsson.csv | cut -d ',' -f 1,5 > WCDMA_HSPA.csv
grep GSM/EDGE Ericsson.csv | cut -d ',' -f 1,5 > GSM_EDGE.csv
grep TD-SCDMA Ericsson.csv | cut -d ',' -f 1,5 > TD-SCDMA.csv
grep ",CDMA" Ericsson.csv | cut -d ',' -f 1,5 > CDMA.csv
grep 'Other technologies' Ericsson.csv | cut -d ',' -f 1,5 > Other.csv
```

`Ericsson.gp`:

```
set datafile separator ','
set timefmt '%Y'
set format x '%Y'
set xdata time
set title 'Ericsson Mobility Report November 2022'
set xlabel 'Year'
set ylabel 'Mobile subscriptions (Unit: Million)'
plot '5G.csv' using 1:2 with linespoints title '5G', \
'LTE.csv' using 1:2 with linespoints title 'LTE', \
'WCDMA_HSPA.csv' using 1:2 with linespoints title 'WCDMA/HSPA', \
'GSM_EDGE.csv' using 1:2 with linespoints title 'GSM/EDGE', \
'CDMA.csv' using 1:2 with linespoints title 'CDMA', \
'TD-SCDMA.csv' using 1:2 with linespoints title 'TD-SCDMA', \
'Other.csv' using 1:2 with linespoints title 'Other technologies'
```

![Ericsson Mobility Report November 2022 using Gnuplot](/images/Ericsson/Ericsson.png)