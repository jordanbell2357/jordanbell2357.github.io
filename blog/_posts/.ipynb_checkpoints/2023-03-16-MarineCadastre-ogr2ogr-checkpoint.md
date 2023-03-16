---
layout: post
title: MarineCadastre.gov
---

[AccessAIS \| BOEM, NOAA, U.S. Coast Guard Navigation Center](https://marinecadastre.gov/accessais/)

[Vessel Traffic Data](https://marinecadastre.gov/ais/)

[GDAL documentation » Programs » ogrmerge.p](https://gdal.org/programs/ogrmerge.html)

The following creates shapefiles from geodatabase files.

```bash
unzip AISVesselTracks2018GreatLakes.zip

ogr2ogr -f "ESRI Shapefile" AISVesselTracks2018GreatLakes GreatLakes.gdb
```

The following merges the shapefiles into a shapefile with a month field.

```bash
ogrmerge.py -single -o Tracks_2018_merged.shp Tracks_2018_*.shp -src_layer_field_name month
```




