---
layout: post
title: NAVCEN How AIS Works
topic: readings
---

[United States Coast Guard Navigation Center (USCG NAVCEN)](https://navcen.uscg.gov/)

[How AIS Works \| NAVCEN](https://navcen.uscg.gov/how-ais-works)

> Each AIS system consists of one VHF transmitter, two VHF TDMA receivers, one VHF DSC receiver, and standard marine electronic communications links (IEC 61162/NMEA 0183) to shipboard display and sensor systems (AIS Schematic). Position and timing information is normally derived from an integral or external global navigation satellite system (e.g. GPS) receiver, including a medium frequency differential GNSS receiver for precise position in coastal and inland waters. Other information broadcast by the AIS, if available, is electronically obtained from shipboard equipment through standard marine data connections. Heading information and course and speed over ground would normally be provided by all AIS-equipped ships. Other information, such as rate of turn, angle of heel, pitch and roll, and destination and ETA could also be provided.
>
> AIS normally works in an autonomous and continuous mode, regardless of whether it is operating in the open seas or coastal or inland areas. Transmissions use 9.6 kb GMSK FM modulation over 25 or 12.5 kHz channels using HDLC packet protocols. Although only one radio channel is necessary, each station transmits and receives over two radio channels to avoid interference problems, and to allow channels to be shifted without communications loss from other ships. The system provides for automatic contention resolution between itself and other stations, and communications integrity is maintained even in overload situations.
>
> Each station determines its own transmission schedule (slot), based upon data link traffic history and knowledge of future actions by other stations. A position report from one AIS station fits into one of 2250 time slots established every 60 seconds. AIS stations continuously synchronize themselves to each other, to avoid overlap of slot transmissions. Slot selection by an AIS station is randomized within a defined interval, and tagged with a random timeout of between 0 and 8 frames. When a station changes its slot assignment, it pre-announces both the new location and the timeout for that location. In this way new stations, including those stations which suddenly come within radio range close to other vessels, will always be received by those vessels.
>
> 