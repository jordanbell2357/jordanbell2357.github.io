---
layout: post
title: BarentsWatch AIS API using nc, gpsd and jq
---

We follow [Streaming ETL and Analytics on Confluent with Maritime AIS Data. Robin Moffatt. June 1, 2021](https://www.confluent.io/blog/streaming-etl-and-analytics-for-real-time-location-tracking/)

# gpsd

[gpsd](https://gpsd.gitlab.io/gpsd/AIVDM.html#_ais_payload_interpretation)

# jq

[jq](https://devdocs.io/jq/)

# nc

[nc(1) - OpenBSD manual pages](https://man.openbsd.org/nc.1)

[Ncat Users' Guide \| Nmap](https://nmap.org/ncat/guide/index.html)

```bash
timeout 1s nc 153.44.253.27 5631 > nc_1s
```

```
\s:2573345,c:1682294942*00\!BSVDM,1,1,,B,13mo2<?P05Pm<5rU<oBFGgv62@28,0*04
\s:2573238,c:1682294943*0A\!BSVDM,1,1,,B,H3m8KH0dpn0PUA8400000000000,2*11
\s:2573315,c:1682294943*04\!BSVDM,1,1,,B,33mD6a5000PSIMdT7Af8oUH60En:,0*3D
\s:2573335,c:1682294943*06\!BSVDM,1,1,,A,B3m:0KP008:2pF96iUcQ3wQQnD`b,0*59
\s:2573455,c:1682294943*07\!BSVDM,1,1,,A,39NWvhQ0011?ebjW;KiJ:TOl0000,0*78
\s:2573010,c:1682294943*02\!BSVDM,1,1,,A,33m;7@50P0PHDnvRSn7G4V662DhJ,0*16
\s:2573135,c:1682294943*04\!BSVDM,1,1,,B,13n3l5?P00PTiSdQAPOv4?v62@2D,0*39
\s:2573535,c:1682294943*00\!BSVDM,1,1,,A,33n05650001Ffv2Wmn255Q660DP:,0*1B
\s:2573565,c:1682294943*05\!BSVDM,1,1,,A,13mQ>O70001e0v0`MqKut9d800RC,0*37
\s:2573345,c:1682294942*00\!BSVDM,2,1,6,B,53m>jk800000hOCK?81LThhTd0000000000000160`942t00000000000000,0*48
\s:2573345,c:1682294942*00\!BSVDM,2,2,6,B,00000000000,2*38
\s:2573305,c:1682294943*05\!BSVDM,2,1,7,B,53mTON82F9nThHMV220MDpp5:0h4pMH62222220N50R786mc;D0@C1DmCQ88,0*03
\s:2573305,c:1682294943*05\!BSVDM,2,2,7,B,88888888880,2*39
\s:2573225,c:1682294944*01\!BSVDM,2,1,8,B,53mBCJ81gcR0aP5<0008:0hTI@E800000000000l0pc5759@07Tm0EPCQiDP,0*7F
\s:2573225,c:1682294944*01\!BSVDM,2,2,8,B,00000000000,2*36
\s:2573545,c:1682294944*00\!BSVDM,1,1,,A,13n53M00001P2kN`4iFPqJL60@2F,0*00
\s:2573145,c:1682294944*04\!BSVDM,2,1,5,B,53n7B282>=S4hIE:220DpE8MV1=L4r222222221J315:95;DN>jCTl2DQD`8,0*2E
\s:2573145,c:1682294944*04\!BSVDM,2,2,5,B,88888888880,2*3B
!BSVDM,1,1,,B,13o4Wl00000J:blQi8IsgWJP0@9P,0*19
\s:2573315,c:1682294944*03\!BSVDM,1,1,,A,H3n21e04pMHTd00000000000000,2*0F
\s:2573593,c:1682294944*0B\!BSVDM,1,1,,A,B>1VPd@04pSm8E:4Mcu8Cwv0RJGT,0*73
```

```bash
timeout 1s ncat 153.44.253.27 5631 > ncat_1s
```

```
\s:2573243,c:1682303750*05\!BSVDM,1,1,,B,B3m9g5P0005avA`dR3kQ3wq1jD2J,0*45
\s:2573235,c:1682303750*04\!BSVDM,1,1,,A,13nEo`70000Gp7HRHTT8HJWT0HMg,0*17
\s:2573243,c:1682303750*05\!BSVDM,1,1,,B,33LG5b5000PG2q8RlawrL4oV0Der,0*71
\s:2573577,c:1682303750*05\!BSVDM,1,1,,A,13m:KdPvP1Qt`f@`TGA:EUQR28Mi,0*54
\s:2573405,c:1682303750*01\!BSVDM,1,1,,A,B=4UfNh000=ilw9E4`bu;wq43P06,0*4D
\s:2573415,c:1682303750*00\!BSVDM,1,1,,A,H3n?jf0pu8@iU<0000000000000,2*66
\s:2573405,c:1682303750*01\!BSVDM,1,1,,A,13mBPd00000pqnTUbMjshD5R00Sf,0*30
\s:2573135,c:1682303750*07\!BSVDM,1,1,,B,13`eGl@02:PVMIHQ?lPQwAaP8D0A,0*2B
\s:2573455,c:1682303750*04\!BSVDM,1,1,,A,13n3U5?w@0Q;aBBW?J61vlKT00SS,0*13
\s:2573235,c:1682303750*04\!BSVDM,2,1,4,A,53nVqN42E@bhhAHR220huH59B1HTdTpN2222221618C654rdR01RDj1PDSDs,0*39
\s:2573235,c:1682303750*04\!BSVDM,2,2,4,A,vLNL=e=Mp80,2*61
!BSVDM,1,1,3,A,13n?OWgP00Q7NWtdhj6q;?wT2@Mp,0*32
\s:2573235,c:1682303751*05\!BSVDM,1,1,,A,13o0`A00?wPH1abRTEbf46CV04B<,0*0B
\s:2573450,c:1682303750*01\!BSVDM,1,1,,A,13m8oiW000PtQGPVuOd<nWmT0L0U,0*46
\s:2573535,c:1682303751*02\!BSVDM,1,1,,A,13M4c`001`1FS7NWmEL8:FKT08Mr,0*14
\s:2573515,c:1682303751*00\!BSVDM,1,1,,B,33m7ve51P01;gTDWG`71CwwR0E;:,0*7F
\s:2573305,c:1682303751*07\!BSVDM,1,1,,A,13oGr<0P000GQl@SMM=N4?wT0@Mu,0*71
\s:2573315,c:1682303751*06\!BSVDM,1,1,,B,13m8WGP000PU6CVT>I8@iVeR04B<,0*14
\s:2573105,c:1682303751*05\!B2VDM,1,1,0,A,13n3=LP000Pj8S@Qp<?WnQKN04B<,0*04
\s:2573315,c:1682303751*06\!BSVDM,2,1,3,A,53mdKB42<it0h@8:2208Tu=@5:222222222222167H73;4rdR08888888888,0*68
\s:2573315,c:1682303751*06\!BSVDM,2,2,3,A,88888888880,2*3E
\s:2573445,c:1682303751*04\!BSVDM,1,1,,B,13m=Q:2P00Q2entW2rfBiwwT28N0,0*01
\s:2573584,c:1682303751*08\!BSVDM,1,1,,A,13mQ<R7001QeIg\`\`\`AU0I8eD04B<,0*1D
```

```bash
cat nc_1s | gpsdecode > nc_gpsd_1s
```

```bash
head -n 1 nc_gpsd_1s
```

```json
{"class":"AIS","device":"stdin","type":1,"repeat":0,"mmsi":257802800,"scaled":true,"status":15,"status_text":"Not defined","turn":"nan","speed":0.5,"accuracy":true,"lon":11.619302,"lat":65.013455,"course":163.0,"heading":511,"second":3,"maneuver":0,"raim":true,"radio":65672}
```

```bash
jq --slurp '.' nc_gpsd_1s > nc_gpsd_jq_1s.json
```

```bash
jq '.[0]' nc_gpsd_jq_1s.json
```

```json
{
  "class": "AIS",
  "device": "stdin",
  "type": 1,
  "repeat": 0,
  "mmsi": 257802800,
  "scaled": true,
  "status": 15,
  "status_text": "Not defined",
  "turn": "nan",
  "speed": 0.5,
  "accuracy": true,
  "lon": 11.619302,
  "lat": 65.013455,
  "course": 163,
  "heading": 511,
  "second": 3,
  "maneuver": 0,
  "raim": true,
  "radio": 65672
}
```

---

```bash
timeout 60s nc 153.44.253.27 5631 > nc_60s
```

```bash
cat nc_60s | gpsdecode > nc_gpsd_60s
```

```bash
head -n 1 nc_gpsd_60s
```

```json
{"class":"AIS","device":"stdin","type":1,"repeat":0,"mmsi":259707000,"scaled":true,"status":0,"status_text":"Under way using engine","turn":0,"speed":2.3,"accuracy":false,"lon":19.028200,"lat":69.694137,"course":215.6,"heading":220,"second":1,"maneuver":0,"raim":false,"radio":49235}
```

```bash
jq --slurp '.' nc_gpsd_60s > nc_gpsd_jq_60s.json
```

```bash
jq '.[0]' nc_gpsd_jq_60s.json
```

```json
{
  "class": "AIS",
  "device": "stdin",
  "type": 1,
  "repeat": 0,
  "mmsi": 259707000,
  "scaled": true,
  "status": 0,
  "status_text": "Under way using engine",
  "turn": 0,
  "speed": 2.3,
  "accuracy": false,
  "lon": 19.0282,
  "lat": 69.694137,
  "course": 215.6,
  "heading": 220,
  "second": 1,
  "maneuver": 0,
  "raim": false,
  "radio": 49235
}
```

---

```bash
timeout 3600s nc 153.44.253.27 5631 > nc_3600s
```

```bash
cat nc_3600s | gpsdecode > nc_gpsd_3600s
```

```bash
head -n 1 nc_gpsd_3600s
```

```json
{"class":"AIS","device":"stdin","type":1,"repeat":0,"mmsi":257027750,"scaled":true,"status":0,"status_text":"Under way using engine","turn":0,"speed":0.0,"accuracy":false,"lon":11.220803,"lat":64.838193,"course":360.0,"heading":347,"second":40,"maneuver":0,"raim":false,"radio":49214}
```

```bash
wc -l nc_gpsd_3600s
```

```
114202 nc_gpsd_3600s
```

```bash
jq --slurp '.' nc_gpsd_3600s > nc_gpsd_jq_3600s.json
```

```bash
jq '.[0]' nc_gpsd_jq_3600s.json
```

```json
{
  "class": "AIS",
  "device": "stdin",
  "type": 1,
  "repeat": 0,
  "mmsi": 257027750,
  "scaled": true,
  "status": 0,
  "status_text": "Under way using engine",
  "turn": 0,
  "speed": 0,
  "accuracy": false,
  "lon": 11.220803,
  "lat": 64.838193,
  "course": 360,
  "heading": 347,
  "second": 40,
  "maneuver": 0,
  "raim": false,
  "radio": 49214
}
```