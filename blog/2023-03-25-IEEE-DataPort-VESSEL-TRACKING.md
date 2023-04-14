---
layout: post
title: IEEE DataPort - VESSEL TRACKING (AIS), VESSEL METADATA AND DIRWAY DATASETS
---

[VESSEL TRACKING (AIS), VESSEL METADATA AND DIRWAY DATASETS \| IEEE DataPort](https://ieee-dataport.org/open-access/vessel-tracking-ais-vessel-metadata-and-dirway-datasets)

> The dataset consists of vessel tracking data in the form of AIS observations in the Baltic Sea during years 2017-19. The AIS observations have been enriched with vessel metadata such as power, max speed and draft. The data has been collected for master’s thesis work and the data has been splitter into training and validation sets. The AIS observations do not cover all months of the collection period. 
>
> The observations are sorted by vessel mmsi. Each observation contains information of timestamp, mmsi, lat, lon, speed (meters per second), course (degrees), heading (degrees), turnrate (degrees per minute), breadth (meters), vessel_type, vessel_max_speed (meters per second), draft (meters), power, dwt (tons) and iceclass.

`ais_baltic_sea.zip`

```
49K Aug 25  2019 dirways_all_2018_2019.csv
1.7G Feb 18  2020 training_set.csv
14M Dec  8  2019 validation_set_summer.csv
7.1M Dec  2  2019 validation_set_winter.csv
```

```bash
head training_set.csv
```

```
,timestamp,mmsi,lat,lon,speed,course,heading,turnrate,breadth,vessel_type,vessel_max_speed,draft,power,dwt,iceclass
0,2017-11-02 11:19:07,205366000,54.34724166666667,9.99114,4.01,56.6,56.0,0.0,21.33,T,16.0,8.18,5820.0,13289.0,IA
1,2017-11-02 11:30:58,205366000,54.36034833333333,10.025336666666666,4.17,77.5,81.0,0.0,21.33,T,16.0,8.18,5820.0,13289.0,IA
2,2017-11-02 11:37:58,205366000,54.35957333333333,10.049203333333333,4.48,92.4,92.0,0.0,21.33,T,16.0,8.18,5820.0,13289.0,IA
3,2017-11-02 11:44:07,205366000,54.36549666666666,10.07132,3.81,44.9,46.0,0.0,21.33,T,16.0,8.18,5820.0,13289.0,IA
4,2017-11-02 11:56:08,205366000,54.37043666666667,10.109498333333333,2.73,103.6,103.0,0.0,21.33,T,16.0,8.18,5820.0,13289.0,IA
5,2017-11-02 12:07:19,205366000,54.367425,10.13177,1.49,102.8,103.0,0.0,21.33,T,16.0,8.18,5820.0,13289.0,IA
6,2017-11-02 12:14:27,205366000,54.36662833333333,10.138221666666666,0.77,101.1,102.0,0.0,21.33,T,16.0,8.18,5820.0,13289.0,IA
7,2017-11-02 12:26:27,205366000,54.366353333333336,10.140815,0.0,89.0,104.0,0.0,21.33,T,16.0,8.18,5820.0,13289.0,IA
8,2017-11-02 12:50:49,205366000,54.36626999999999,10.141121666666667,0.46,108.1,106.0,0.0,21.33,T,16.0,8.18,5820.0,13289.0,IA
```

![training_set.csv in QGIS](/images/IEEE/training_set_csv_QGIS.png)