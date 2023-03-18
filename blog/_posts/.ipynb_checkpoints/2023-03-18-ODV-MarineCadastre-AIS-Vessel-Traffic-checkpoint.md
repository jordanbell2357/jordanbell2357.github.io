---
layout: post
title: Using Ocean Data View (ODV) with MarineCadastre.gov AIS Vessel Traffic
---

# ODV

[Ocean Data View (ODV)](https://odv.awi.de/)

# MarineCadastre.gov

[MarineCadastre.gov](https://marinecadastre.gov/)

![MarineCadastre.gov Vessel Traffic Data](/images/ODV/MarineCadastre-gov-Vessel-Traffic-Data.png)

## AIS_2017_06_21

```bash
du -h AIS_2017_06_21.csv
```

```
905M    AIS_2017_06_21.csv
```

```bash
head -n 5 AIS_2017_06_21.csv
```

```
MMSI,BaseDateTime,LAT,LON,SOG,COG,Heading,VesselName,IMO,CallSign,VesselType,Status,Length,Width,Draft,Cargo
367556028,2017-06-21T00:00:00,28.15498,-96.89194,5.7,51.2,47.0,,,,,15,,,,
338117119,2017-06-21T00:00:00,59.60455,-151.42022,0.0,271.4,511.0,,,,,0,,,,
367320010,2017-06-21T00:00:00,43.34561,-124.32150,0.0,357.6,511.0,,,,,,,,,
354580000,2017-06-21T00:00:01,26.13417,-79.92080,7.9,239.0,511.0,EMERALD EXPRESS,IMO9248332,HO2486,1004,0,57.91,11.58,2.3,70
```

![June 21, 2017 AIS Vessel Traffic](/images/ODV/AIS_2017_06_21_ODV.png)

![June 21, 2017 AIS Vessel Traffic for CONUS](/images/ODV/AIS_2017_06_21_ODV_CONUS.png)

Save Canvas as Image:

![Save Canvas as Image](/images/ODV/AIS_2017_06_21_Canvas.png)

X/Y Distribution:

![X/Y Distribution](/images/ODV/AIS_2017_06_21_XY_distribution.png)

X Histogram:

![X Histogram](/images/ODV/AIS_2017_06_21_X_Histogram.png)

Y Histogram:

![Y Histogram](/images/ODV/AIS_2017_06_21_Y_Histogram.png)

## AIS_2021_06_21

```bash
du -h AIS_2021_06_21.csv
```

```
918M    AIS_2021_06_21.csv
```

```bash
head -n 5 AIS_2021_06_21.csv
```

```
MMSI,BaseDateTime,LAT,LON,SOG,COG,Heading,VesselName,IMO,CallSign,VesselType,Status,Length,Width,Draft,Cargo,TransceiverClass
563073700,2021-06-21T00:00:07,36.94941,-76.01901,9.0,112.8,108.0,MAERSK MEMPHIS,IMO9348651,9V6171,71,5,299,40,13.1,71,A
367568120,2021-06-21T00:00:07,47.96343,-125.05863,5.5,159.7,511.0,SOUFFLE,IMO0000000,WDG7519,36,,10,3,,,B
303585000,2021-06-21T00:00:03,47.74071,-122.43953,10.5,162.0,511.0,VOYAGER,IMO0000000,WDM2014,37,,28,7,,,B
368005340,2021-06-21T00:00:01,42.79171,-78.98200,7.8,242.9,511.0,FLO,IMO0000000,WDJ7298,36,,13,6,,,B
```

Save Canvas as Image:

![Save Canvas as Image](/images/ODV/AIS_2021_06_21_Canvas.png)

X/Y Distribution:

![X/Y Distribution](/images/ODV/AIS_2021_06_21_XY_distribution.png)

X Histogram:

![X Histogram](/images/ODV/AIS_2021_06_21_X_Histogram.png)

Y Histogram:

![Y Histogram](/images/ODV/AIS_2021_06_21_Y_Histogram.png)

## AIS_2022_06_21

```bash
du -h AIS_2022_06_21.csv
```

```
886M    AIS_2022_06_21.csv
```

```bash
head -n 5 AIS_2022_06_21.csv
```

```
MMSI,BaseDateTime,LAT,LON,SOG,COG,Heading,VesselName,IMO,CallSign,VesselType,Status,Length,Width,Draft,Cargo,TransceiverClass
367757270,2022-06-21T00:00:01,29.96195,-90.23906,0.1,358.0,301.0,ST MATTHIAS,,WDJ2321,31,12,,,,57,A
366973590,2022-06-21T00:00:01,29.33022,-94.67887,18.4,302.0,302.0,LONE STAR,,WCY9015,,0,15,9,,,A
367318760,2022-06-21T00:00:02,39.84967,-75.31567,7.6,270.0,265.0,BOHEMIA,IMO9493004,WDD9977,31,0,30,10,4.0,32,A
367016590,2022-06-21T00:00:03,29.27181,-89.68693,8.9,212.6,511.0,MARY VIRGINIA,,WYR2142,30,15,56,12,0.0,30,A
```

Save Canvas as Image:

![Save Canvas as Image](/images/ODV/AIS_2022_06_21_Canvas.png)

X/Y Distribution:

![X/Y Distribution](/images/ODV/AIS_2022_06_21_XY_distribution.png)

X Histogram:

![X Histogram](/images/ODV/AIS_2022_06_21_X_Histogram.png)

Y Histogram:

![Y Histogram](/images/ODV/AIS_2022_06_21_Y_Histogram.png)