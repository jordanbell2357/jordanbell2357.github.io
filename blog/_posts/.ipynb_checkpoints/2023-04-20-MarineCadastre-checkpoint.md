---
layout: post
title: MarineCadastre
---


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