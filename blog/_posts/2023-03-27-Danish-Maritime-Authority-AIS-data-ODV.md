---
layout: post
title: Danish Maritime Authority (DMA) AIS data using Ocean Data View
---

<https://dma.dk/safety-at-sea/navigational-information/download-data>

<http://web.ais.dk/aisdata/>

`!_README_information_CSV_files.rtf	`

<table>
<tbody>
  <tr>
    <td>1.</td>
    <td>Timestamp</td>
    <td>Timestamp from the AIS basestation, format: 31/12/2015 23:59:59</td>
  </tr>
  <tr>
    <td>2.</td>
    <td>Type of mobile</td>
    <td>Describes what type of target this message is received from (class A AIS Vessel, Class B AIS vessel, etc)</td>
  </tr>
  <tr>
    <td>3.</td>
    <td>MMSI</td>
    <td>MMSI number of vessel</td>
  </tr>
  <tr>
    <td>4.</td>
    <td>Latitude</td>
    <td>Latitude of message report (e.g. 57,8794)</td>
  </tr>
  <tr>
    <td>5.</td>
    <td>Longitude</td>
    <td>Longitude of message report (e.g. 17,9125)</td>
  </tr>
  <tr>
    <td>6.</td>
    <td>Navigational status</td>
    <td>Navigational status from AIS message if available, e.g.: 'Engaged in fishing', 'Under way using engine', mv.</td>
  </tr>
  <tr>
    <td>7.</td>
    <td>ROT</td>
    <td>Rot of turn from AIS message if available</td>
  </tr>
  <tr>
    <td>8.</td>
    <td>SOG</td>
    <td>Speed over ground from AIS message if available</td>
  </tr>
  <tr>
    <td>9.</td>
    <td>COG</td>
    <td>Course over ground from AIS message if available</td>
  </tr>
  <tr>
    <td>10.</td>
    <td>Heading</td>
    <td>Heading from AIS message if available</td>
  </tr>
  <tr>
    <td>11.</td>
    <td>IMO</td>
    <td>IMO number of the vessel</td>
  </tr>
  <tr>
    <td>12.</td>
    <td>Callsign</td>
    <td>Callsign of the vessel</td>
  </tr>
  <tr>
    <td>13.</td>
    <td>Name</td>
    <td>Name of the vessel</td>
  </tr>
  <tr>
    <td>14.</td>
    <td>Ship type</td>
    <td>Describes the AIS ship type of this vessel</td>
  </tr>
  <tr>
    <td>15.</td>
    <td>Cargo type</td>
    <td>Type of cargo from the AIS message</td>
  </tr>
  <tr>
    <td>16.</td>
    <td>Width</td>
    <td>Width of the vessel</td>
  </tr>
  <tr>
    <td>17.</td>
    <td>Length</td>
    <td>Lenght of the vessel</td>
  </tr>
  <tr>
    <td>18.</td>
    <td>Type of position fixing device</td>
    <td>Type of positional fixing device from the AIS message</td>
  </tr>
  <tr>
    <td>19.</td>
    <td>Draught</td>
    <td>Draugth field from AIS message</td>
  </tr>
  <tr>
    <td>20.</td>
    <td>Destination</td>
    <td>Destination from AIS message</td>
  </tr>
  <tr>
    <td>21.</td>
    <td>ETA</td>
    <td>Estimated Time of Arrival, if available</td>
  </tr>
  <tr>
    <td>22.</td>
    <td>Data source type</td>
    <td>Data source type, e.g. AIS</td>
  </tr>
  <tr>
    <td>23.</td>
    <td>Size A</td>
    <td>Length from GPS to the bow</td>
  </tr>
  <tr>
    <td>24.</td>
    <td>Size B</td>
    <td>Length from GPS to the stern</td>
  </tr>
  <tr>
    <td>25.</td>
    <td>Size C</td>
    <td>Length from GPS to starboard side</td>
  </tr>
  <tr>
    <td>26.</td>
    <td>Size D</td>
    <td>Length from GPS to port side</td>
  </tr>
</tbody>
</table>


```
2.6G    aisdk-2023-02-15.csv
1.6G    aisdk-2023-02-22.csv
1.8G    aisdk-2023-03-01.csv
1.5G    aisdk-2023-03-08.csv
1.6G    aisdk-2023-03-15.csv
1.7G    aisdk-2023-03-18.csv
```

```bash
head aisdk-2023-02-15.csv
```

```
# Timestamp,Type of mobile,MMSI,Latitude,Longitude,Navigational status,ROT,SOG,COG,Heading,IMO,Callsign,Name,Ship type,Cargo type,Width,Length,Type of position fixing device,Draught,Destination,ETA,Data source type,A,B,C,D
15/02/2023 00:00:00,Class A,219063000,57.1152,8.33121,Under way using engine,0.0,6.4,216.9,217,Unknown,,,Undefined,,,,Undefined,,,,AIS,,,,
15/02/2023 00:00:00,Class A,220228000,55.4732,8.42364,Engaged in fishing,0.0,0.0,136.7,332,Unknown,,,Undefined,,,,Undefined,,,,AIS,,,,
15/02/2023 00:00:00,Base Station,2190064,56.7166,11.5191,Unknown value,,,,,Unknown,,,Undefined,,,,GPS,,,,AIS,,,,
15/02/2023 00:00:00,Class A,220228000,55.4732,8.42364,Engaged in fishing,0.0,0.0,136.7,332,Unknown,,,Undefined,,,,Undefined,,,,AIS,,,,
15/02/2023 00:00:00,Class A,220304000,56.7157,11.5125,Engaged in fishing,0.0,0.0,271.8,289,Unknown,,,Undefined,,,,Undefined,,,,AIS,,,,
15/02/2023 00:00:00,Class A,355378000,55.4983,5.41641,Under way using engine,0.0,11.9,17.6,15,Unknown,,,Undefined,,,,Undefined,,,,AIS,,,,
15/02/2023 00:00:00,Class A,220304000,56.7157,11.5125,Engaged in fishing,0.0,0.0,271.8,289,Unknown,,,Undefined,,,,Undefined,,,,AIS,,,,
15/02/2023 00:00:00,Base Station,2194006,55.5389,5.0334,Unknown value,,,,,Unknown,,,Undefined,,,,Surveyed,,,,AIS,,,,
15/02/2023 00:00:00,Class A,219002857,55.6791,12.5935,Under way using engine,0.0,0.0,270.3,297,Unknown,,,Undefined,,,,Undefined,,,,AIS,,,,
```

`aisdk-2023-02-15`

![aisdk-2023-02-15 Canvas](/images/DanishMaritimeAuthority/aisdk-2023-02-15-canvas.png)

![aisdk-2023-02-15 X/Y Distribution](/images/DanishMaritimeAuthority/aisdk-2023-02-15-X_Y.png)

`aisdk-2023-02-22`

![aisdk-2023-02-22 Canvas](/images/DanishMaritimeAuthority/aisdk-2023-02-22-canvas.png)

![aisdk-2023-02-22 X/Y Distribution](/images/DanishMaritimeAuthority/aisdk-2023-02-22-X_Y.png)

`aisdk-2023-03-01`

![aisdk-2023-03-01 Canvas](/images/DanishMaritimeAuthority/aisdk-2023-03-01-canvas.png)

![aisdk-2023-03-01 X/Y Distribution](/images/DanishMaritimeAuthority/aisdk-2023-03-01-X_Y.png)

`aisdk-2023-03-08`

![aisdk-2023-03-08 Canvas](/images/DanishMaritimeAuthority/aisdk-2023-03-08-canvas.png)

![aisdk-2023-03-08 X/Y Distribution](/images/DanishMaritimeAuthority/aisdk-2023-03-08-X_Y.png)