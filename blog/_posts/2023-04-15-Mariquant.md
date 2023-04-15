---
layout: post
title: Creating sea routes from the sea of AIS data by Mariquant
---

This post is my gloss doing a close reading of:

[Creating sea routes from the sea of AIS data. Alexei Novikov. Mariquant. May 15, 2019. Towards Data Science (TDS)](https://towardsdatascience.com/creating-sea-routes-from-the-sea-of-ais-data-30bc68d8530e)

> Mariquant has hourly data from one of the AIS data providers for the bulkers and tankers from the beginning of 2016 to the middle of 2018. This data has information from around 19 000 unique ships with records, occupying approximately 100 Gb as uncompressed parquet file.

> We used distance to the port, distance to the previous port, speed of the ship, radial velocity of the ship (as if circling the port) and speed in the direction to the port, as the features of the classifier. We manually constructed training and testing sets separately marking ‘loitering’, anchoring, port approaching and general voyage points. We had around 6 400 points in the training and 1600 points in the testing set. Anchoring points are less represented in the sets, as they create fewer problems in the distance calculations.

> We found that distance to the port, distance to the previous port, speed of the ship are the most important features, having a score of 0.42, 0.21 and 0.28 correspondingly and radial speed and speed in the direction to the port have a score of 0.04 and 0.05.

> We found that irrespectively from the scores of the classifiers, additional cleanup is required for our large dataset. Sometimes small parts of the port approach trajectories were mistakenly identified as loitering parts, and we had to apply conservative check requiring anchoring and loitering parts of the trajectories to be long enough and either be self-intersecting, or the distance travelled in the direction to the port should be smaller compared to the total length travelled.
>
> After all these checks we average the position of the vessel for the loitering and anchoring parts of the trajectories.

`WorldRoutes.html`

![WorldRoutes.html](/images/Mariquant/WorldRoutes.png)

```bash
head -n 5 distances.csv
```

```
,trip_count,prev_port,next_port,distance,frequency
7682,1984063,4410,3658,460.63814769485793,1.0
7062,1948666,3658,7083,372.7538137212947,1.0
2712,1287366,7083,7084,26.578905957417856,1.0
7248,1950728,7084,2814,9.200891935648707,1.0
```

```bash
head -n 5 ports.csv
```

```
,PORT_NAME,INDEX_NO,coords
49159,Terminal Pesquero Cta. Quiane,,"((-70.31722387298942, -18.513597026467323),)"
49164,Oil Berth,,"((-61.86886473007713, 17.150384410999997),)"
16,Port of Basamuk,,"((146.14295817405977, -5.53913255687803),)"
26,Victoria,,"((-123.32715191091728, 48.402783083729446),)"
```

```bash
head -n 5 routes.csv
```

```
,trip_count,prev_port,next_port,lat,lon,frequency
7641,1984063,4410,3658,45.764835,-87.05328753692308,1.0
7642,1984063,4410,3658,45.60853333,-87.03821667,1.0
7643,1984063,4410,3658,45.56013333,-87.03423333,1.0
7644,1984063,4410,3658,45.48103333,-87.01585,1.0
```