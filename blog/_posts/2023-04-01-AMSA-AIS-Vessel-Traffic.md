---
layout: post
title: Australian Maritime Safety Authority (AMSA) AIS Vessel Tracking Data
---

[Vessel Tracking Data \| Spatial@AMSA](https://www.operations.amsa.gov.au/Spatial/DataServices/DigitalData)

![AMSA Vessel Tracking Data](/images/AMSA/Digital-Data.png)

Vessel Traffic Data January 2020 to December 2020

> The Craft Tracking System (CTS) is AMSA's vessel traffic database. CTS collects vessel traffic data from a variety of sources, including terrestrial and satellite shipborne Automatic Identification System (AIS) data sources. This dataset has been built from AIS data extracted from CTS and contains vessel traffic data for the month of January 2020. The dataset covers the extents of Australia's Search and Rescue Region.

```
cts_srr_01_2020_pt.zip
cts_srr_02_2020_pt.zip
...
cts_srr_12_2020_pt.zip
```

`cts_srr_01_2020_pt.zip` is an archive containing `cts_srr_01_2020_pt.shp`, and the associated files (in particular,
`cts_srr_01_2020_pt.dbf`) for the ESRI shapefile format, and likewise for all the months.

These shapefiles are point sets (latitude and longitude, which other fields), rather than say boundaries. They are thus suitable to convert to CSV, which is substantially the most efficient format among shapefile, GeoJSON and CSV.[^1]

[^1]: Question for me to return to: understand how WKT, KML, KMZ work more deeply than I do for point sets.

