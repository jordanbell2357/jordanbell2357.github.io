---
layout: post
title: MarineCadastre.gov AIS Vessel Tracks using GDAL and QGIS
---

[AccessAIS \| BOEM, NOAA, U.S. Coast Guard Navigation Center](https://marinecadastre.gov/accessais/)

[Vessel Traffic Data](https://marinecadastre.gov/ais/)

# AISVesselTracks2018GreatLakes

[GDAL documentation » Programs » ogrmerge.p](https://gdal.org/programs/ogrmerge.html)

The following creates shapefiles from geodatabase files.

```bash
unzip AISVesselTracks2018GreatLakes.zip

ogr2ogr -f "ESRI Shapefile" AISVesselTracks2018GreatLakes GreatLakes.gdb
```

The following merges the shapefiles into a shapefile with a month field and makes a zip archive of the shapefile directory.

```bash
ogrmerge.py -single -o Tracks_2018_merged.shp Tracks_2018_*.shp -src_layer_field_name month

mkdir ../AISVesselTracks2018GreatLakes_merged

mv Tracks_2018_merged* ../AISVesselTracks2018GreatLakes_merged
```

Make zipfile of shapefile:

```bash
zip -r AISVesselTracks2018GreatLakes_merged.zip AISVesselTracks2018GreatLakes_merged
```

![MarineCadastre.gov AccessAIS](/images/MarineCadastre/AccessAIS-MarineCadastre-gov.png)

![MarineCadastre.gov Data](/images/MarineCadastre/MarineCadastre-gov-Vessel-Traffic-Data.png)

![QGIS Monthly AIS Vessel Tracks](/images/MarineCadastre/QGIS_monthly.png)

Merged with QGIS:

![Merged with QGIS](/images/MarineCadastre/QGIS_merge.png)

Merged with GDAL:

![Merged with GDAL](/images/MarineCadastre/GDAL_merge.png)

# 12NM Territorial Sea and Principal Ports

![12NM Territorial Sea and Principal Ports](/images/MarineCadastre/PrincipalPorts.png)