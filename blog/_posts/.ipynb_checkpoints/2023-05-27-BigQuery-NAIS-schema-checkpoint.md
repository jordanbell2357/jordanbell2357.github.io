---
layout: post
title: USCG NAIS National AIS at 1 Minute Intervals CSV schema for BigQuery
topic: uscg-nais
toc: true
---

{% include toc.html %}

# Office for Coastal Management, 2023: Nationwide Automatic Identification System 2022

[OCM Metadata Library](https://www.fisheries.noaa.gov/inport/item/37112)

Office for Coastal Management, 2023: Nationwide Automatic Identification System 2022, <https://www.fisheries.noaa.gov/inport/item/67336>. GUID: gov.noaa.nmfs.inport:67336. Updated: February 6, 2023.

## Item Identification

<table>
  <caption>Item Identification</caption>
<tbody>
  <tr>
    <td>Title:</td>
    <td>Nationwide Automatic Identification System 2022</td>
  </tr>
  <tr>
    <td>Status:</td>
    <td>Completed</td>
  </tr>
  <tr>
    <td>Publication Date:</td>
    <td>2022-06-03</td>
  </tr>
  <tr>
    <td>Abstract:</td>
    <td>Automatic Identification Systems (AIS) are a navigation safety device that transmits and monitors the location and characteristics of many vessels in U.S. and international waters in real-time. In the U.S. the Coast Guard and industry collect AIS data, which can also be used for a variety of coastal management purposes. NOAA and BOEM have worked jointly to make available these data from the U.S. Coast Guards national network of AIS receivers. The original records were filtered to a one-minute frequency rate, and subset to depict the location and description of vessels broadcasting within the Exclusive Economic Zone.</td>
  </tr>
  <tr>
    <td>Purpose:</td>
    <td>To support ocean planning activities pursuant to the Executive Order Regarding the Ocean Policy to Advance the Economic, Security, and Environmental Interests of the United States, the Energy Policy Act, the Rivers and Harbors Act, and the Coastal Zone Management Act.</td>
  </tr>
  <tr>
    <td>Supplemental Information:</td>
    <td>Bureau Code: 006:48, Program Code: 006:055</td>
  </tr>
</tbody>
</table>

<table>
  <caption>Data Quality</caption>
<tbody>
  <tr>
    <td>Horizontal Positional Accuracy:</td>
    <td>Compiled to meet 10 meters horizontal accuracy at 95% confidence level</td>
  </tr>
  <tr>
    <td>Bias:</td>
    <td>Presence and absence of a record is dependent on the:<br>a) Fixed and unpublished location and height of the receiving antenna relative to the dynamic position, antenna height and wattage of the transmitting vessel,<br>b) Interference of the radio frequency transmission between the vessel and the receiving antenna, and the<br>c) Interference in the collection of the record originating from the vessel</td>
  </tr>
  <tr>
    <td>Completeness Measure:</td>
    <td>a) Visual analysis of daily record byte count over a year long period<br>b) Verbal and email communications with U.S. Coast Guard Navigation Center personnel</td>
  </tr>
  <tr>
    <td>Completeness Report:</td>
    <td>Records were received from all U.S. Coast Guard NAIS terrestrial receivers. The source data from the U.S. Coast Guard contained very few Type 2 messages for the period February 11 to March 22.</td>
  </tr>
  <tr>
    <td>Conceptual Consistency:</td>
    <td>These data are logically consistent</td>
  </tr>
</tbody>
</table>

## Data Set Information

<table>
  <caption>Data Set Information</caption>
<tbody>
  <tr>
    <td>Data Set Scope Code:</td>
    <td>Data Set</td>
  </tr>
  <tr>
    <td>Maintenance Frequency:</td>
    <td>None Planned</td>
  </tr>
  <tr>
    <td>Data Presentation Form:</td>
    <td>Map (digital)</td>
  </tr>
  <tr>
    <td>Entity Attribute Overview:</td>
    <td>MMIS, BaseDateTime, LAT, LON, SOG, COG, Heading, VesselName, IMO, CallSign, VesselType, Status, Length, Width, Draft, Cargo, TransceiverClass (see more here: https://coast.noaa.gov/data/marinecadastre/ais/data-dictionary.pdf)</td>
  </tr>
  <tr>
    <td>Distribution Liability:</td>
    <td>https://www.marinecadastre.gov/about/disclaimer.html</td>
  </tr>
  <tr>
    <td>Data Set Credit:</td>
    <td>U.S. Coast Guard Navigation Center, Bureau of Ocean Energy Management, NOAA Office for Coastal Management</td>
  </tr>
</tbody>
</table>

## Extents

<table>
  <caption>Extent Group 1 / Geographic Area 1</caption>
<tbody>
  <tr>
    <td>W° Bound:</td>
    <td>-168</td>
  </tr>
  <tr>
    <td>E° Bound:</td>
    <td>-60</td>
  </tr>
  <tr>
    <td>N° Bound:</td>
    <td>51.5</td>
  </tr>
  <tr>
    <td>S° Bound:</td>
    <td>15</td>
  </tr>
</tbody>
</table>

<table>
  <caption>Extent Group 1 / Time Frame 1</caption>
<tbody>
  <tr>
    <td>Time Frame Type:</td>
    <td>Range</td>
  </tr>
  <tr>
    <td>Start:</td>
    <td>2022-01-01</td>
  </tr>
  <tr>
    <td>End:</td>
    <td>2022-12-31</td>
  </tr>
</tbody>
</table>

## Spatial Information

<table>
  <caption>Coordinate Reference System</caption>
<tbody>
  <tr>
    <td>CRS Type:</td>
    <td>Geographic 2D</td>
  </tr>
  <tr>
    <td>EPSG Code:</td>
    <td>EPSG:4269</td>
  </tr>
  <tr>
    <td>EPSG Name:</td>
    <td>NAD83</td>
  </tr>
  <tr>
    <td>Datum Name:</td>
    <td>North American Datum 1983</td>
  </tr>
  <tr>
    <td>Ellipsoid:</td>
    <td>GRS 1980</td>
  </tr>
  <tr>
    <td>Semimajor Axis:</td>
    <td>6378137.0</td>
  </tr>
  <tr>
    <td>Flattening Ratio:</td>
    <td>298.257222101</td>
  </tr>
</tbody>
</table>

<table>
  <caption>Axis: Geodetic Latitude</caption>
<tbody>
  <tr>
    <td>Order:</td>
    <td>1</td>
  </tr>
  <tr>
    <td>Abbreviation:</td>
    <td>Lat</td>
  </tr>
  <tr>
    <td>Units:</td>
    <td>degree</td>
  </tr>
  <tr>
    <td>Orientation:</td>
    <td>north</td>
  </tr>
</tbody>
</table>

<table>
  <caption>Axis: Geodetic Latitude</caption>
<tbody>
  <tr>
    <td>Order:</td>
    <td>1</td>
  </tr>
  <tr>
    <td>Abbreviation:</td>
    <td>Lat</td>
  </tr>
  <tr>
    <td>Units:</td>
    <td>degree</td>
  </tr>
  <tr>
    <td>Orientation:</td>
    <td>north</td>
  </tr>
</tbody>
</table>

<table>
  <caption>Axis: Geodetic Longitude</caption>
<tbody>
  <tr>
    <td>Order:</td>
    <td>2</td>
  </tr>
  <tr>
    <td>Abbreviation:</td>
    <td>Lon</td>
  </tr>
  <tr>
    <td>Units:</td>
    <td>degree</td>
  </tr>
  <tr>
    <td>Orientation:</td>
    <td>east</td>
  </tr>
</tbody>
</table>

<table>
  <caption>Axis: Geodetic Longitude</caption>
<tbody>
  <tr>
    <td>Order:</td>
    <td>2</td>
  </tr>
  <tr>
    <td>Abbreviation:</td>
    <td>Lon</td>
  </tr>
  <tr>
    <td>Units:</td>
    <td>degree</td>
  </tr>
  <tr>
    <td>Orientation:</td>
    <td>east</td>
  </tr>
</tbody>
</table>

## Lineage

### Sources

<table>
  <caption>Nationwide Automatic Identification SystemCC ID: 1173408</caption>
<tbody>
  <tr>
    <td>Contact Role Type:</td>
    <td>Originator</td>
  </tr>
  <tr>
    <td>Contact Type:</td>
    <td>Organization</td>
  </tr>
  <tr>
    <td>Contact Name:</td>
    <td>U.S. Coast Guard Navigation Center</td>
  </tr>
  <tr>
    <td>Publish Date:</td>
    <td>2022-01-01</td>
  </tr>
  <tr>
    <td>Extent Type:</td>
    <td>Range</td>
  </tr>
  <tr>
    <td>Extent Start Date/Time:</td>
    <td>2022-01-01</td>
  </tr>
  <tr>
    <td>Extent End Date/Time:</td>
    <td>2022-09-30</td>
  </tr>
  <tr>
    <td>Citation URL:</td>
    <td><a href="https://www.navcen.uscg.gov/">https://www.navcen.uscg.gov/</a></td>
  </tr>
  <tr>
    <td>Source Contribution:</td>
    <td>Daily compressed log files containing original AIS messages in NMEA format for the months of January through March for the United States. Authoritative Vessel Identification Service (AVIS) Vessel Catalog.</td>
  </tr>
</tbody>
</table>

### Process Steps

<table>
  <caption>Process Step 1</caption>
<tbody>
  <tr>
    <td>Description:</td>
    <td>Filter the raw NMEA data to a one-minute sample rate and select a subset of fields using MarineCadastre.gov NMEA to SQL Server processing tools<br>Load filtered records to a SQL Server database using MarineCadastre.gov NMEA to SQL Server processing tools<br>Conduct quality and completeness check using logging results from the filter and loading process, and database record counts<br>Update the IMO, CallSign, VesselName, Length, Width, VesselType, and Draft from US Coast Guard AVIS<br>Added or updated the new vessel type code field to each record fragment that was found in the US Coast Guard AVIS<br>Export records from the SQL Server database to CSV files organized day of the year using MarineCadastre.gov Filter and Export utilities<br>Modify the format of the date and time values to a UTC string format during export<br>Modify the format of the IMO vessel number to include the â€œIMOâ€ prefix during export<br>Trim white space from string attributes during export<br>Replaced comma punctuation marks with a semi-colon in the vessel name or call sign field if present to improve CSV formatting during export<br>Include a header record with descriptive text for each field during export<br>Write extracted AIS data to an ASCII CSV format file using MarineCadastre.gov Filter and Export utilities<br>Compress each ASCII CSV file</td>
  </tr>
  <tr>
    <td>Process Date/Time:</td>
    <td>2021-07-01 00:00:00</td>
  </tr>
  <tr>
    <td>Source:</td>
    <td>Nationwide Automatic Identification System</td>
  </tr>
</tbody>
</table>

## Catalog Details

<table>
  <caption>Catalog Details</caption>
<tbody>
  <tr>
    <td>Catalog Item ID:</td>
    <td>67336</td>
  </tr>
  <tr>
    <td>GUID:</td>
    <td>gov.noaa.nmfs.inport:67336</td>
  </tr>
  <tr>
    <td>Metadata Record Created By:</td>
    <td>Jesse Brass</td>
  </tr>
  <tr>
    <td>Metadata Record Created:</td>
    <td>2022-06-03 13:07+0000</td>
  </tr>
  <tr>
    <td>Metadata Record Last Modified By:</td>
    <td>Jesse Brass</td>
  </tr>
  <tr>
    <td>Metadata Record Last Modified:</td>
    <td>2023-02-06 19:17+0000</td>
  </tr>
  <tr>
    <td>Metadata Record Published:</td>
    <td>2022-06-03</td>
  </tr>
  <tr>
    <td>Owner Org:</td>
    <td>OCM</td>
  </tr>
  <tr>
    <td>Metadata Publication Status:</td>
    <td>Published Externally</td>
  </tr>
  <tr>
    <td>Do Not Publish?:</td>
    <td>N</td>
  </tr>
  <tr>
    <td>Metadata Last Review Date:</td>
    <td>2022-06-03</td>
  </tr>
  <tr>
    <td>Metadata Review Frequency:</td>
    <td>1 Year</td>
  </tr>
  <tr>
    <td>Metadata Next Review Date:</td>
    <td>2023-06-03</td>
  </tr>
</tbody>
</table>

# curl

```bash
for i in {01..30}; do \
curl -O https://coast.noaa.gov/htdata/CMSP/AISDataHandler/2022/AIS_2022_06_${i}.zip; \
unzip AIS_2022_06_${i}.zip; \
rm AIS_2022_06_${i}.zip;
done
```

# gsutil

```bash
for i in {01..30}; do \
gsutil cp AIS_2022_06_${i}.csv gs://jordanbell2357marinecadastre/; \
rm AIS_2022_06_${i}.csv; \
done
```

# Schema

[Specifying a schema](https://cloud.google.com/bigquery/docs/schemas)

`MarineCadastre_schema.json`

```json
[
  {
    "description": "Maritime Mobile Service Identity value",
    "mode": "REQUIRED",
    "name": "MMSI",
    "type": "STRING"
  },
  {
    "description": "Full UTC date and time",
    "mode": "REQUIRED",
    "name": "BaseDateTime",
    "type": "TIMESTAMP"
  },
  {
    "description": "decimal degrees. Latitude",
    "mode": "REQUIRED",
    "name": "LAT",
    "type": "FLOAT"
  },
  {
    "description": "decimal degrees. Longitude",
    "mode": "REQUIRED",
    "name": "LON",
    "type": "FLOAT"
  },
  {
    "description": "knots. Speed Over Ground",
    "mode": "REQUIRED",
    "name": "SOG",
    "type": "FLOAT"
  },
  {
    "description": "degrees. Course Over Ground",
    "mode": "REQUIRED",
    "name": "COG",
    "type": "FLOAT"
  },
  {
    "description": "degrees. True heading angle",
    "mode": "REQUIRED",
    "name": "Heading",
    "type": "FLOAT"
  },
  {
    "description": "Name as shown on the station radio license",
    "mode": "NULLABLE",
    "name": "VesselName",
    "type": "STRING"
  },
  {
    "description": "International Maritime Organization Vessel number",
    "mode": "NULLABLE",
    "name": "IMO",
    "type": "STRING"
  },
  {
    "description": "Call sign as assigned by FCC",
    "mode": "NULLABLE",
    "name": "CallSign",
    "type": "STRING"
  },
  {
    "description": "Vessel type as defined in NAIS specifications",
    "mode": "NULLABLE",
    "name": "VesselType",
    "type": "STRING"
  },
  {
    "description": "Navigation status as defined by the COLREGS",
    "mode": "NULLABLE",
    "name": "Status",
    "type": "STRING"
  },
  {
    "description": "Length of vessel (see NAIS specifications)",
    "mode": "NULLABLE",
    "name": "Length",
    "type": "FLOAT"
  },
  {
    "description": "Width of vessel (see NAIS specifications)",
    "mode": "NULLABLE",
    "name": "Width",
    "type": "FLOAT"
  },
  {
    "description": "Draft depth of vessel (see NAIS specifications)",
    "mode": "NULLABLE",
    "name": "Draft",
    "type": "FLOAT"
  },
  {
    "description": "Cargo type (see NAIS specification and codes)",
    "mode": "NULLABLE",
    "name": "Cargo",
    "type": "STRING"
  },
  {
    "description": "Class of AIS transceiver",
    "mode": "REQUIRED",
    "name": "TransceiverClass",
    "type": "STRING"
  }
]
```
 
[bq command-line tool reference](https://cloud.google.com/bigquery/docs/reference/bq-cli-reference)

# bq mk

```bash
bq mk --table --schema=MarineCadastre_schema.json uscg.nais
```

# bq show

```bash
bq show --schema --format=prettyjson ais-data-385301:uscg.nais
```

```bash
bq show --schema --format=prettyjson ais-data-385301:uscg.nais | diff MarineCadastre_schema.json -
```

# bq load

```bash
for i in {01..30}; do \
bq load \
--source_format=CSV \
--max_bad_records=200 \
--schema=MarineCadastre_schema.json \
uscg.nais \
gs://jordanbell2357marinecadastre/AIS_2022_06_${i}.csv; \
done
```

`max_bad_records=200` is chosen because `max_bad_records=100` fails. (That is, at least one daily CSV file has have more than
100 records not fitting the schema `MarineCadastre_schema.json`, but there is no daily CSV file with more than 200 records not fitting the schema.)

## bq query

```bash
bq query --use_legacy_sql=false 'SELECT COUNT(*) FROM ais-data-385301.uscg.nais;'
```

<pre>249325885</pre>

<pre>249 million 325 thousand 885 messages</pre>