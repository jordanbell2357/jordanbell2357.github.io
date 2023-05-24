---
layout: post
title: Elastic Maps Service
topic: maps
---

# Kibana Sample Data Flights

[Kibana Fundamentals \| Elastic](https://learn.elastic.co/)

[Kibana Fundamentals Lab Guide \| Elastic](https://www.elastic.co/pdf/kibana-fundamentals-additional-resources.pdf)

[How-to Series: Kibana \| Elastic](https://www.elastic.co/videos/training-how-to-series-stack)

```csv
timestamp,OriginCityName,DestCityName,Carrier,FlightDelayMin
"Apr 26, 2023 @ 11:58:20.000",Johannesburg,Sydney,"Kibana Airlines",255
"Apr 26, 2023 @ 11:53:34.000",Seoul,Hyderabad,"Kibana Airlines",360
"Apr 26, 2023 @ 11:50:34.000",Tokoname,Rome,"Logstash Airways",165
"Apr 26, 2023 @ 11:40:26.000",Bangor,"Jeju City","Logstash Airways",225
```

![Kibana Sample Data Flights](/images/Elastic/Kibana_Sample_Data_Flights.jpeg)

# Elastic Stack Geospatial

[Elastic Stack Geospatial](https://www.elastic.co/geospatial)

[Import geospatial data \| Kibana Guide](https://www.elastic.co/guide/en/kibana/current/import-geospatial-data.html)

# amychan331/json-to-geojson

We use [amychan331/json-to-geojson](https://github.com/amychan331/json-to-geojson) to convert `AIS_2023_04_20.json` to
`AIS_2023_04_20.geojson`. (See post on BarentsWatch AIS API.)

# Elastic Maps Service

Messages in `AIS_2023_04_20.geojson`:

![Points in AIS_2023_04_20.geojson](/images/Elastic/AIS_2023_04_20.jpeg)

Cluster map with hexagons, by message count:

![Cluster map with hexagons, by message count for AIS_2023_04_20.geojson](/images/Elastic/AIS_2023_04_20_cluster_hexagon.jpeg)

Applying filter `shipType : 80` (tankers):

![Filtering to tankers in AIS_2023_04_20.geojson](/images/Elastic/shipType_80.jpeg)

# FleetMon Cargo AIS Data sample

[Cargo AIS Data \| FleetMon](https://www.fleetmon.com/services/ais-data-shop/cargo/)

> The Sample Data Set contains all Cargo Container vessels over 100 meters with a time resolution of 6 hours on a single day (26.03.2020). The signal update frequency of the sample data is 6 hours. Furthermore, you receive the port calls of these container ships for the time period from 24.03.2020 00:00 until 28.03.2020 23:59 UTC.

> In addition to the vessel positions, you can purchase the port calls of these vessels. A port call is the period of time during which the ship has been in a port zone and has come to a standstill.

# Spire AIS sample

[Spire AIS sample](https://spire.com/maritime/get-started/)

```bash
head -n 5 2020-06-26_Container_6h.csv
```

```csv
"MMSI","TimePosition","Latitude","Longitude","Speed","Course","Heading","NavStatus","TimeVoyage","IMO","Name","Callsign","VesselType","Draught","TimeETA","Destination"
"548770200","2020-03-26T00:00:00.000Z","6.923483","122.00095","0.0","206.0","108","at anchor","2020-03-25T23:55:14.000Z","8914556","MV SPAN ASIA 27","DUA3500","Cargo ship","7.5","2020-03-26T02:00:00.000Z","ZAMBOANGA PH"
"271047045","2020-03-26T00:00:00.000Z","38.322865","24.790733","14.9","207.3","206","under way using engine","2020-03-25T23:53:12.000Z","9211157","KOSOVAK","TCA5645","Cargo ship","9.6","2020-03-27T14:00:00.000Z","MISURATA"
"563052500","2020-03-26T00:00:00.000Z","53.532768","9.907048","0.0","28.3","306","under way using engine","2020-03-25T23:57:30.000Z","9283198","MONTE OLIVIA","9V6839","Cargo ship","11.2","2020-03-25T07:00:00.000Z","BEANR DEHAM"
"525019101","2020-03-26T00:00:00.000Z","-5.931","106.914283","8.7","197.4",,"under way using engine","2020-03-25T23:59:58.000Z","9672387","MV UMBUL MAS","POYJ","Cargo ship","4.3","2020-03-26T13:00:00.000Z","JAKARTA"
```

```bash
tail -n 1 2020-06-26_Container_6h.csv
```

```csv
"565846000","2020-03-26T23:55:58.000Z","35.235837","129.840278","9.6","235.6","236","under way using engine","2020-03-26T07:26:23.000Z","9675810","TACOMA TRADER","9V2401","Cargo ship","7.0","2020-03-27T05:00:00.000Z","KRPUS"
```

We will also use [World Port Index (Pub 150) \| National Geospatial-Intelligence Agency (NGA)](https://msi.nga.mil/Publications/WPI)
to visualize ports on the map we are making.

```bash
head -n 1 UpdatedPub150.csv
```

```
World Port Index Number,Region Name,Main Port Name,Alternate Port Name,UN/LOCODE,Country Code,World Water Body,IHO S-130 Sea Area,Sailing Direction or Publication,Publication Link,Standard Nautical Chart,IHO S-57 Electronic Navigational Chart,IHO S-101 Electronic Navigational Chart,Digital Nautical Chart,Tidal Range (m),Entrance Width (m),Channel Depth (m),Anchorage Depth (m),Cargo Pier Depth (m),Oil Terminal Depth (m),Liquified Natural Gas Terminal Depth (m),Maximum Vessel Length (m),Maximum Vessel Beam (m),Maximum Vessel Draft (m),Offshore Maximum Vessel Length (m),Offshore Maximum Vessel Beam (m),Offshore Maximum Vessel Draft (m),Harbor Size,Harbor Type,Harbor Use,Shelter Afforded,Entrance Restriction - Tide,Entrance Restriction - Heavy Swell,Entrance Restriction - Ice,Entrance Restriction - Other,Overhead Limits,Underkeel Clearance Management System,Good Holding Ground,Turning Area,Port Security,Estimated Time of Arrival Message,Quarantine - Pratique,Quarantine - Sanitation,Quarantine - Other,Traffic Separation Scheme,Vessel Traffic Service,First Port of Entry,US Representative,Pilotage - Compulsory,Pilotage - Available,Pilotage - Local Assistance,Pilotage - Advisable,Tugs - Salvage,Tugs - Assistance,Communications - Telephone,Communications - Telefax,Communications - Radio,Communications - Radiotelephone,Communications - Airport,Communications - Rail,Search and Rescue,NAVAREA,Facilities - Wharves,Facilities - Anchorage,Facilities - Dangerous Cargo Anchorage,Facilities - Med Mooring,Facilities - Beach Mooring,Facilities - Ice Mooring,Facilities - Ro-Ro,Facilities - Solid Bulk,Facilities - Liquid Bulk,Facilities - Container,Facilities - Breakbulk,Facilities - Oil Terminal,Facilities - LNG Terminal,Facilities - Other,Medical Facilities,Garbage Disposal,Chemical Holding Tank Disposal,Degaussing,Dirty Ballast Disposal,Cranes - Fixed,Cranes - Mobile,Cranes - Floating,Cranes - Container,Lifts - 100+ Tons,Lifts - 50-100 Tons,Lifts - 25-49 Tons,Lifts - 0-24 Tons,Services - Longshoremen,Services - Electricity,Services - Steam,Services - Navigation Equipment,Services - Electrical Repair,Services - Ice Breaking,Services - Diving,Supplies - Provisions,Supplies - Potable Water,Supplies - Fuel Oil,Supplies - Diesel Oil,Supplies - Aviation Fuel,Supplies - Deck,Supplies - Engine,Repairs,Dry Dock,Railway,Latitude,Longitude
```

We create a layer from `2020-06-26_Container_6h.csv` and choose "Tracks (Create lines from points)". We create tracks according to
MMSI, order by timestamp.

Below we show the tracks created thus in the Indian Ocean:

![Indian Ocean ship tracks using FleetMon sample AIS data](/images/Elastic/FleetMon_sample_data_tracks.jpeg)

and the English Channel:

![English Channel ship tracks using FleetMon sample AIS data](/images/Elastic/FleetMon_sample_English_Channel.jpeg)