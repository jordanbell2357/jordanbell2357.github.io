---
layout: post
title: Australian Maritime Safety Authority (AMSA) AIS Vessel Tracking Data
---

[Vessel Tracking Data \| Spatial@AMSA](https://www.operations.amsa.gov.au/Spatial/DataServices/DigitalData)

## February 2023

> **Vessel Traffic Data February2023**
>
> The Craft Tracking System (CTS) and Mariweb are AMSA’s vessel traffic
> databases. They collect vessel traffic data from a variety of sources, including
> terrestrial and satellite shipborne Automatic Identification System (AIS) data
> sources.
>
> This dataset has been built from AIS data extracted from CTS, and it contains vessel
> traffic data for the month of February 2023. The dataset covers the extents of
> Australia’s Search and Rescue Region.
>
> Each point within the dataset represents a vessel position report and is spatially and
> temporally defined by geographic coordinates and a Universal Time Coordinate
> (UTC) timestamp respectively.
>
> Coordinate System: WGS1984

```
71M     Vessel Traffic Data February2023.zip
```

`cts_monthly_dataset_02_2023_meta.pdf`

<table>
<thead>
  <tr>
    <th>Field name</th>
    <th>Type</th>
    <th>Description</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>CRAFT_ID</td>
    <td>Double</td>
    <td>Unique identifier for each vessel</td>
  </tr>
  <tr>
    <td>LON</td>
    <td>Double</td>
    <td>Longitude in decimal degrees</td>
  </tr>
  <tr>
    <td>LAT</td>
    <td>Double</td>
    <td>Latitude in decimal degrees</td>
  </tr>
  <tr>
    <td>COURSE</td>
    <td>Double</td>
    <td>Course over ground in decimal degrees</td>
  </tr>
  <tr>
    <td>SPEED</td>
    <td>Double</td>
    <td>Speed over ground in knots</td>
  </tr>
  <tr>
    <td>TYPE</td>
    <td>Text</td>
    <td>Vessel type</td>
  </tr>
  <tr>
    <td>SUBTYPE</td>
    <td>Text</td>
    <td>Vessel sub-type</td>
  </tr>
  <tr>
    <td>LENGTH</td>
    <td>Short integer</td>
    <td>Vessel length in metres</td>
  </tr>
  <tr>
    <td>BEAM</td>
    <td>Short integer</td>
    <td>Vessel beam in metres</td>
  </tr>
  <tr>
    <td>DRAUGHT</td>
    <td>Double</td>
    <td>Draught of the vessel, in metres.</td>
  </tr>
  <tr>
    <td>TIMESTAMP</td>
    <td>Text</td>
    <td>Vessel position report UTC timestamp in dd/mm/yyyy hh:mm:ss AM/PM format</td>
  </tr>
</tbody>
</table>

`cts_srr_02_2023_pt.shp` et al.

```bash
ogr2ogr -f CSV cts_srr_02_2023_pt.csv cts_srr_02_2023_pt.shp -lco GEOMETRY=AS_XYZ
```

```
345M    cts_srr_02_2023_pt.csv
```

```bash
head -n 5 cts_srr_02_2023_pt.csv
```

```
X,Y,Z,CRAFT_ID,LON,LAT,COURSE,SPEED,TYPE,SUBTYPE,LENGTH,BEAM,DRAUGHT,TIMESTAMP
115.693126667,-32.2264,0,-2146018332.00000000000,115.69312666700,-32.22640000000,354.50000000000,0.00000000000,unknown code 0,,"111","22",6.60000000000,1/02/2023 12:04:54 AM
115.698958333,-32.231845,0,-2146018332.00000000000,115.69895833300,-32.23184500000,302.80000000000,0.40000000000,unknown code 0,,"111","22",6.60000000000,1/02/2023 1:04:54 AM
115.694263,-32.20631,0,-2146018332.00000000000,115.69426300000,-32.20631000000,173.20000000000,0.50000000000,unknown code 0,,"111","22",0.00000000000,1/02/2023 2:07:24 AM
115.69418,-32.20669,0,-2146018332.00000000000,115.69418000000,-32.20669000000,181.10000000000,0.10000000000,unknown code 0,,"111","22",6.60000000000,1/02/2023 3:09:54 AM
```

## January 2023

```
76M     Vessel Traffic Data January 2023.zip
```

`cts_srr_01_2023_pt.shp` et al.

```bash
ogr2ogr -f CSV cts_srr_01_2023_pt.csv cts_srr_01_2023_pt.shp -lco GEOMETRY=AS_XYZ
```

```
374M    cts_srr_01_2023_pt.csv
```

```bash
head -n 5 cts_srr_01_2023_pt.csv
```

```
X,Y,Z,CRAFT_ID,LON,LAT,COURSE,SPEED,TYPE,SUBTYPE,LENGTH,BEAM,DRAUGHT,TIMESTAMP
106.506,-12.442666667,0,-2146018332.00000000000,106.50600000000,-12.44266666670,0.00000000000,0.00000000000,unknown code 0,,"111","22",0.00000000000,20/01/2023 5:06:00 AM
106.946,-13.5939999999999,0,-2146018332.00000000000,106.94600000000,-13.59400000000,0.00000000000,0.00000000000,unknown code 0,,"111","22",0.00000000000,20/01/2023 11:06:00 AM
107.403333333,-14.7806666669999,0,-2146018332.00000000000,107.40333333300,-14.78066666670,0.00000000000,0.00000000000,unknown code 0,,"111","22",0.00000000000,20/01/2023 5:06:00 PM
107.874666667,-15.9773333329999,0,-2146018332.00000000000,107.87466666700,-15.97733333330,0.00000000000,0.00000000000,unknown code 0,,"111","22",0.00000000000,20/01/2023 11:06:00 PM
```