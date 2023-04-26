---
layout: post
title: MarineCadastre.gov AIS Vessel Tracks 2021 and AIS Vessel Transit Counts 2021
---

[Vessel Traffic Data](https://marinecadastre.gov/ais/)

> AIS Vessel Tracks 2021
>
> A vessel track shows the location and characteristics of commercial, recreational, and other marine vessels as a sequence of positions transmitted by an Automatic Identification System (AIS). AIS signals are susceptible to interference and this can result in a gap within a vessel track. Vessels can have one or more tracks of any length. Furthermore, tracks will not necessarily start or stop at a well defined port, or when a vessel is not in motion. The distribution, type, and frequency of vessel tracks are a useful aid to understanding the risk of conflicting uses within a certain geographic area and are an efficient and spatially unbiased indicator of vessel traffic. The vessel track positions in this data set are collected and recorded from land-based antennas as part of a national network operated by the U.S. Coast Guard. These tracks were used to build the respective AIS Vessel Transit Counts 2021 layer, in which a single transit is counted each time a vessel track passes through, starts, or stops within a grid cell.

> AIS Vessel Transit Counts 2021
>
> Vessels traveling in U.S. coastal and inland waters frequently use Automatic Identification Systems (AIS) for navigation safety. The U.S. Coast Guard collects AIS records using shore-side antennas. These records have been filtered and converted from a series of points to a set of track lines, and then summarized at a 100 m grid cell resolution. A single transit is counted each time a vessel track passes through, starts, or stops within a grid cell. All vessel types have been included in this summary, including null and none reported types.

```bash
ogrinfo AISVesselTracks2021.gpkg
```

```
INFO: Open of `AISVesselTracks2021.gpkg'
      using driver `GPKG' successful.
1: AISVesselTracks2021 (Multi Line String)
```

```bash
ogrinfo -so AISVesselTracks2021.gpkg AISVesselTracks2021
```

```
INFO: Open of `AISVesselTracks2021.gpkg'
      using driver `GPKG' successful.

Layer name: AISVesselTracks2021
Geometry: Multi Line String
Feature Count: 6962768
Extent: (-169.111954, 10.773780) - (-60.000584, 51.578117)
Layer SRS WKT:
GEOGCRS["NAD83",
    DATUM["North American Datum 1983",
        ELLIPSOID["GRS 1980",6378137,298.257222101,
            LENGTHUNIT["metre",1]]],
    PRIMEM["Greenwich",0,
        ANGLEUNIT["degree",0.0174532925199433]],
    CS[ellipsoidal,2],
        AXIS["geodetic latitude (Lat)",north,
            ORDER[1],
            ANGLEUNIT["degree",0.0174532925199433]],
        AXIS["geodetic longitude (Lon)",east,
            ORDER[2],
            ANGLEUNIT["degree",0.0174532925199433]],
    USAGE[
        SCOPE["Geodesy."],
        AREA["North America - onshore and offshore: Canada - Alberta; British Columbia; Manitoba; New Brunswick; Newfoundland and Labrador; Northwest Territories; Nova Scotia; Nunavut; Ontario; Prince Edward Island; Quebec; Saskatchewan; Yukon. Puerto Rico. United States (USA) - Alabama; Alaska; Arizona; Arkansas; California; Colorado; Connecticut; Delaware; Florida; Georgia; Hawaii; Idaho; Illinois; Indiana; Iowa; Kansas; Kentucky; Louisiana; Maine; Maryland; Massachusetts; Michigan; Minnesota; Mississippi; Missouri; Montana; Nebraska; Nevada; New Hampshire; New Jersey; New Mexico; New York; North Carolina; North Dakota; Ohio; Oklahoma; Oregon; Pennsylvania; Rhode Island; South Carolina; South Dakota; Tennessee; Texas; Utah; Vermont; Virginia; Washington; West Virginia; Wisconsin; Wyoming. US Virgin Islands. British Virgin Islands."],
        BBOX[14.92,167.65,86.46,-47.74]],
    ID["EPSG",4269]]
Data axis to CRS axis mapping: 2,1
FID Column = OBJECTID
Geometry Column = Shape
MMSI: Integer (0.0)
TrackStartTime: DateTime (0.0)
TrackEndTime: DateTime (0.0)
VesselType: Integer (0.0)
Length: Real (0.0)
Width: Real (0.0)
Draft: Real (0.0)
DurationMinutes: Integer (0.0)
VesselGroup: String (25.0)
```



