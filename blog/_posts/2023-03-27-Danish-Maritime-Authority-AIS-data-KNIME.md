---
layout: post
title: Danish Maritime Authority (DMA) AIS data and KNIME and ODV
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
1.5G    aisdk-2023-03-08.csv
1.6G    aisdk-2023-03-15.csv
1.7G    aisdk-2023-03-18.csv
```

```bash
head aisdk-2023-03-18.csv
```

```
# Timestamp,Type of mobile,MMSI,Latitude,Longitude,Navigational status,ROT,SOG,COG,Heading,IMO,Callsign,Name,Ship type,Cargo type,Width,Length,Type of position fixing device,Draught,Destination,ETA,Data source type,A,B,C,D
18/03/2023 00:00:00,Base Station,2190064,56.7166,11.519,Unknown value,,,,,Unknown,,,Undefined,,,,GPS,,,,AIS,,,,
18/03/2023 00:00:00,Class A,352002266,55.4921,14.7525,Under way using engine,0.7,12.5,241.8,241,Unknown,,,Undefined,,,,Undefined,,,,AIS,,,,
18/03/2023 00:00:00,Class A,211551940,54.6926,8.57745,Under way using engine,0.0,0.0,269.3,92,Unknown,,,Undefined,,,,Undefined,,,,AIS,,,,
18/03/2023 00:00:00,Class A,219030190,57.5203,8.34178,Under way using engine,0.0,8.7,151.4,160,Unknown,,,Undefined,,,,Undefined,,,,AIS,,,,
18/03/2023 00:00:00,Class A,255619000,54.8512,13.2935,Under way using engine,0.0,10.7,69.4,67,Unknown,,,Undefined,,,,Undefined,,,,AIS,,,,
18/03/2023 00:00:00,Class A,219554000,57.969,11.2706,Under way using engine,0.0,16.6,348.9,349,Unknown,,,Undefined,,,,Undefined,,,,AIS,,,,
18/03/2023 00:00:00,Class A,219472000,91,0,Unknown value,,,,,9686429,OWMI2,GUARDVESSEL ADVANCER,Other,,8,23,GPS,1.9,GUARD VESSEL FEMARN,11/03/2023 21:00:00,AIS,16,7,5,3
18/03/2023 00:00:00,Class A,219007401,57.123,8.59783,Under way using engine,0.0,0.0,229.1,243,Unknown,,,Undefined,,,,Undefined,,,,AIS,,,,
18/03/2023 00:00:00,Class A,241580000,57.7565,10.992,Constrained by her draught,0.0,12.5,319.6,316,Unknown,,,Undefined,,,,Undefined,,,,AIS,,,,
```

