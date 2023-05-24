---
layout: post
title: Google Cloud Platform and MarineCadastre.gov
topic: MarineCadastre
---

# MarineCadastre.gov

[Vessel Traffic Data](https://marinecadastre.gov/AIS/)

[National AIS at 1 Minute Intervals](https://marinecadastre.gov/data/)

[AIS Data for 2022](https://coast.noaa.gov/htdata/CMSP/AISDataHandler/2022/index.html)

`AIS_2022_01_01.zip`, `AIS_2022_01_02.zip`, ..., `AIS_2022_12_31.zip`

i.e. `AIS_2022_(0[1-9]|1[0-2])_(0[1-9]|[12][0-9]|3[01])\.zip`

[Nationwide Automatic Identification System 2022](https://www.fisheries.noaa.gov/inport/item/67336)

[Data Dictionary PDF](https://coast.noaa.gov/data/marinecadastre/ais/data-dictionary.pdf)

<table>
<thead>
  <tr>
    <th></th>
    <th>Name</th>
    <th>Description</th>
    <th>Example</th>
    <th>Units</th>
    <th>Resolution</th>
    <th>Type</th>
    <th>Size</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>1</td>
    <td>MMSI</td>
    <td>Maritime Mobile Service Identity value</td>
    <td>477220100</td>
    <td></td>
    <td></td>
    <td>Text</td>
    <td>8</td>
  </tr>
  <tr>
    <td>2</td>
    <td>BaseDateTime</td>
    <td>Full UTC date and time</td>
    <td>2017-02-01 20:05:07</td>
    <td></td>
    <td>YYYY-MM-DD:HH-MM-SS</td>
    <td>DateTime</td>
    <td></td>
  </tr>
  <tr>
    <td>3</td>
    <td>LAT</td>
    <td>Latitude</td>
    <td>42.35137</td>
    <td>decimal degrees</td>
    <td>XX.XXXXX</td>
    <td>Double</td>
    <td>8</td>
  </tr>
  <tr>
    <td>4</td>
    <td>LON</td>
    <td>Longitude</td>
    <td>-71.04182</td>
    <td>decimal degrees</td>
    <td>XXX.XXXXX</td>
    <td>Double</td>
    <td>8</td>
  </tr>
  <tr>
    <td>5</td>
    <td>SOG</td>
    <td>Speed Over Ground</td>
    <td>5.9</td>
    <td>knots</td>
    <td>XXX.X</td>
    <td>Float</td>
    <td>4</td>
  </tr>
  <tr>
    <td>6</td>
    <td>COG</td>
    <td>Course Over Ground</td>
    <td>47.5</td>
    <td>degrees</td>
    <td>XXX.X</td>
    <td>Float</td>
    <td>4</td>
  </tr>
  <tr>
    <td>7</td>
    <td>Heading</td>
    <td>True heading angle</td>
    <td>45.1</td>
    <td>degrees</td>
    <td>XXX.X</td>
    <td>Float</td>
    <td>4</td>
  </tr>
  <tr>
    <td>8</td>
    <td>VesselName</td>
    <td>Name as shown on the station radio license</td>
    <td>OOCL Malaysia</td>
    <td></td>
    <td></td>
    <td>Text</td>
    <td>32</td>
  </tr>
  <tr>
    <td>9</td>
    <td>IMO</td>
    <td>International Maritime Organization Vessel number</td>
    <td>IMO9627980</td>
    <td></td>
    <td></td>
    <td>Text</td>
    <td>16</td>
  </tr>
  <tr>
    <td>10</td>
    <td>CallSign</td>
    <td>Call sign as assigned by FCC</td>
    <td>VRME7</td>
    <td></td>
    <td></td>
    <td>Text</td>
    <td>8</td>
  </tr>
  <tr>
    <td>11</td>
    <td>VesselType</td>
    <td>Vessel type as defined in NAIS specifications</td>
    <td>70</td>
    <td></td>
    <td></td>
    <td>Integer</td>
    <td>short</td>
  </tr>
  <tr>
    <td>12</td>
    <td>Status</td>
    <td>Navigation status as defined by the COLREGS</td>
    <td>3</td>
    <td></td>
    <td></td>
    <td>Integer</td>
    <td>short</td>
  </tr>
  <tr>
    <td>13</td>
    <td>Length</td>
    <td>Length of vessel (see NAIS specifications)</td>
    <td>71</td>
    <td>meters</td>
    <td>XXX.X</td>
    <td>Float</td>
    <td>4</td>
  </tr>
  <tr>
    <td>14</td>
    <td>Width</td>
    <td>Width of vessel (see NAIS specifications)</td>
    <td>12</td>
    <td>meters</td>
    <td>XXX.X</td>
    <td>Float</td>
    <td>4</td>
  </tr>
  <tr>
    <td>15</td>
    <td>Draft</td>
    <td>Draft depth of vessel (see NAIS specifications)</td>
    <td>3.5</td>
    <td>meters</td>
    <td>XXX.X</td>
    <td>Float</td>
    <td>4</td>
  </tr>
  <tr>
    <td>16</td>
    <td>Cargo</td>
    <td>Cargo type (see NAIS specification and codes)</td>
    <td>70</td>
    <td></td>
    <td></td>
    <td>Text</td>
    <td>4</td>
  </tr>
  <tr>
    <td>17</td>
    <td>TransceiverClass</td>
    <td>Class of AIS transceiver</td>
    <td>A</td>
    <td></td>
    <td></td>
    <td>Text</td>
    <td>2</td>
  </tr>
</tbody>
</table>

[AIS Fundamentals \| Spire Maritime Documentation](https://documentation.spire.com/ais-fundamentals/ais-data-sources/satellite-ais/)

# Unix text processing

```bash
curl -O https://coast.noaa.gov/htdata/CMSP/AISDataHandler/2022/AIS_2022_06_20.zip
unzip AIS_2022_06_20.zip
```

```bash
head -n 5 AIS_2022_06_20.csv
```

```csv
MMSI,BaseDateTime,LAT,LON,SOG,COG,Heading,VesselName,IMO,CallSign,VesselType,Status,Length,Width,Draft,Cargo,TransceiverClass
538009563,2022-06-20T00:00:04,29.23668,-116.63519,20.4,149.9,152.0,DEL MONTE PRIDE,IMO9869693,V7A4893,70,0,192,30,7.6,70,A
367481660,2022-06-20T00:00:05,38.58858,-90.19843,0.0,360.0,511.0,MIRANDA PAIGE,IMO8976578,WDF7156,31,0,21,9,,31,A
303200000,2022-06-20T00:00:06,36.85888,-76.34542,0.0,213.9,337.0,TAURUS,IMO7819498,WDB6361,31,0,22,7,,32,A
368011450,2022-06-20T00:00:06,29.61732,-89.89189,6.1,297.8,511.0,KRISTIN,,WDJ7927,31,0,17,7,,31,A
```

```bash
tail -n 5 AIS_2022_06_20.csv
```

```csv
303533000,2022-06-20T23:17:52,13.46087,144.66438,0.4,266.0,511.0,HURAO,IMO9277230,WDL4585,52,15,29,9,4.0,52,A
303533000,2022-06-20T23:21:21,13.46088,144.66436,0.0,244.7,511.0,HURAO,IMO9277230,WDL4585,52,15,29,9,4.0,52,A
303533000,2022-06-20T23:37:22,13.45743,144.65525,7.8,260.7,511.0,HURAO,IMO9277230,WDL4585,52,15,29,9,4.0,52,A
303533000,2022-06-20T23:44:22,13.45513,144.64894,0.7,215.1,511.0,HURAO,IMO9277230,WDL4585,52,15,29,9,4.0,52,A
303533000,2022-06-20T23:53:42,13.45187,144.64068,0.2,290.2,511.0,HURAO,IMO9277230,WDL4585,52,15,29,9,4.0,52,A
```

# AWS S3

I started the cloud process using AWS S3. I then did it using Google Cloud Storage. I keep the documentation for AWS S3.

[Using high-level (s3) commands with the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-services-s3-commands.html)

The size of each zip file we download is around 300 MB and decompressed the csv file is around 900 MB. There is not enough
available space in my EC2 instance to do the following in EC2 Instance Connect.

Locally we run the following:

[Download to a file named by the URL](https://everything.curl.dev/usingcurl/downloads/url-named)

> This is the `-O` (uppercase letter o) option, or `--remote-name` for the long name version. The `-O` option selects the local file name to use by picking the file name part of the URL that you provide. This is important. You specify the URL and curl picks the name from this data. If the site redirects curl further (and if you tell curl to follow redirects), it does not change the file name curl will use for storing this.

```bash
for i in {21..27}; do \
curl -O https://coast.noaa.gov/htdata/CMSP/AISDataHandler/2022/AIS_2022_06_${i}.zip; \
unzip AIS_2022_06_${i}.zip; \
done
```

```bash
for i in {21..27}; do aws s3 cp AIS_2022_06_${i}.csv s3://jordanbell2357ais/; done
```

S3 bucket:

![S3 bucket](/images/AWS/jordanbell2357ais.jpeg)

# Google Cloud Storage

[Discover object storage with the gsutil tool](https://cloud.google.com/storage/docs/discover-object-storage-gsutil)

Using EC2 Instance Connect was not possible in my AWS configuration, because the size of each pair of zip file and csv file is
over 1 GB in each case. On the other hand, in my configuration of Google Cloud Platform, the 5 GB available space is enough to 
store one by one the zip file and csv file.

We write out the steps for June 21, 2022, in a general way.

```bash
i=21 # 01-31
curl -O https://coast.noaa.gov/htdata/CMSP/AISDataHandler/2022/AIS_2022_06_${i}.zip
unzip AIS_2022_06_${i}.zip
gsutil cp AIS_2022_06_${i}.csv gs://jordanbell2357marinecadastre/
rm AIS_2022_06_${i}.zip
rm AIS_2022_06_${i}.csv
```

Relevant Google Cloud Self-Paced Labs (GSP): Cloud Storage: Qwik Start - CLI/SDK (**GSP074**),
Ingesting Data Into The Cloud (**GSP194**), Ingesting New Datasets into BigQuery (**GSP 411**), Loading Your Own Data into BigQuery (**GSP865**).

We use `bq` now:

```bash
for i in {21..27}; do bq load --source_format=CSV --autodetect AIS_2022_06_21_to_27.AIS_2022_06_${i} gs://jordanbell2357marinecadastre/AIS_2022_06_${i}.csv; done
```

Now, to make sure we can do the same task multiple ways, we will do the above locally for June 20, 2022.

```bash
curl -O https://coast.noaa.gov/htdata/CMSP/AISDataHandler/2022/AIS_2022_06_20.zip
unzip AIS_2022_06_20.zip
```

If we now run

```bash
gsutil cp AIS_2022_06_20.csv gs://jordanbell2357/marinecadastre/
```

we get

```
ResumableUploadAbortException: 401 Anonymous caller does not have storage.objects.create access to the Google Cloud Storage object. Permission 'storage.objects.create' denied on resource (or it may not exist).
```

[Initializing the gcloud CLI](https://cloud.google.com/sdk/docs/initializing)

[Install gsutil](https://cloud.google.com/storage/docs/gsutil_install#deb)

We run

```bash
gcloud init
```

and then run

```bash
gsutil cp AIS_2022_06_20.csv gs://jordanbell2357/marinecadastre/
```

with success. Then

```bash
bq load --source_format=CSV --autodetect AIS_2022_06_21_to_27.AIS_2022_06_20 gs://jordanbell2357marinecadastre/AIS_2022_06_20.csv
```

with success. Now we clean up,

```bash
rm AIS_2022_06_20.zip
rm AIS_2022_06_20.csv
```

# BigQuery

[Query syntax \| BigQuery](https://cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax#union_example)

```sql
(SELECT MMSI,BaseDateTime,LAT,LON,SOG,COG,Heading,VesselType,Status,Length,Width FROM ais-data-385301.AIS_2022_06_21_to_27.AIS_2022_06_21)
UNION ALL
(SELECT MMSI,BaseDateTime,LAT,LON,SOG,COG,Heading,VesselType,Status,Length,Width FROM ais-data-385301.AIS_2022_06_21_to_27.AIS_2022_06_22)
UNION ALL
(SELECT MMSI,BaseDateTime,LAT,LON,SOG,COG,Heading,VesselType,Status,Length,Width FROM ais-data-385301.AIS_2022_06_21_to_27.AIS_2022_06_23)
UNION ALL
(SELECT MMSI,BaseDateTime,LAT,LON,SOG,COG,Heading,VesselType,Status,Length,Width FROM ais-data-385301.AIS_2022_06_21_to_27.AIS_2022_06_24)
UNION ALL
(SELECT MMSI,BaseDateTime,LAT,LON,SOG,COG,Heading,VesselType,Status,Length,Width FROM ais-data-385301.AIS_2022_06_21_to_27.AIS_2022_06_25)
UNION ALL
(SELECT MMSI,BaseDateTime,LAT,LON,SOG,COG,Heading,VesselType,Status,Length,Width FROM ais-data-385301.AIS_2022_06_21_to_27.AIS_2022_06_26)
UNION ALL
(SELECT MMSI,BaseDateTime,LAT,LON,SOG,COG,Heading,VesselType,Status,Length,Width FROM ais-data-385301.AIS_2022_06_21_to_27.AIS_2022_06_27)
```

We save the results to a BigQuery table, creating a new table we name `AIS_2022_06_21_to_27`
(`ais-data-385301.AIS_2022_06_21_to_27.AIS_2022_06_21_to_27`).

