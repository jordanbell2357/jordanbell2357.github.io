---
layout: post
title: Australian Maritime Safety Authority (AMSA) AIS Vessel Tracking Data
---

[Vessel Tracking Data \| Spatial\@AMSA](https://www.operations.amsa.gov.au/Spatial/DataServices/DigitalData)

![AMSA Vessel Tracking Data](/images/AMSA/Digital-Data.png)

Vessel Traffic Data January 2020 to December 2020

> The Craft Tracking System (CTS) is AMSA's vessel traffic database. CTS collects vessel traffic data from a variety of sources, including terrestrial and satellite shipborne Automatic Identification System (AIS) data sources. This dataset has been built from AIS data extracted from CTS and contains vessel traffic data for the month of January 2020. The dataset covers the extents of Australia's Search and Rescue Region.

etc.

There is a zipped shapefile for each month of 2020.

![QGIS Attribute Table](/images/AMSA/Attribute_Table.png)

The attributes include a timestamp, and we can thus merge the shapefiles without having to create a new attribute (flag for the month).

![QGIS Merge Vector Layers](/images/AMSA/QGIS_AMSA_merge.png)




