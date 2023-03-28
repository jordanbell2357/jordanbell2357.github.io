---
layout: post
title: Danish Maritime Authority (DMA) AIS data and KNIME and ODV
---

<https://dma.dk/safety-at-sea/navigational-information/download-data>

<http://web.ais.dk/aisdata/>

`!_README_information_CSV_files.rtf	`

```
1.	Timestamp			Timestamp from the AIS basestation, format: 31/12/2015 23:59:59	
2.	Type of mobile			Describes what type of target this message is received from (class A AIS Vessel, Class B AIS vessel, etc)
3.	MMSI				MMSI number of vessel
4.	Latitude			Latitude of message report (e.g. 57,8794)
5.	Longitude			Longitude of message report (e.g. 17,9125)
6.	Navigational status		Navigational status from AIS message if available, e.g.: 'Engaged in fishing', 'Under way using engine', mv.
7.	ROT				Rot of turn from AIS message if available
8.	SOG				Speed over ground from AIS message if available
9.	COG				Course over ground from AIS message if available
10.	Heading			Heading from AIS message if available
11.	IMO				IMO number of the vessel
12.	Callsign				Callsign of the vessel 
13.	Name				Name of the vessel
14.	Ship type			Describes the AIS ship type of this vessel 
15.	Cargo type			Type of cargo from the AIS message 
16.	Width				Width of the vessel
17.	Length				Lenght of the vessel 
18.	Type of position fixing device	Type of positional fixing device from the AIS message 
19.	Draught			Draugth field from AIS message
20.	Destination			Destination from AIS message
21.	ETA				Estimated Time of Arrival, if available  
22.	Data source type		Data source type, e.g. AIS
23. Size A				Length from GPS to the bow
24. Size B				Length from GPS to the stern
25. Size C				Length from GPS to starboard side
26. Size D				Length from GPS to port side
```


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

