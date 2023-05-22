---
layout: post
title: How big data enriches maritime research – a critical review of Automatic Identification System (AIS) data applications
---

Yang, D., Wu, L., Wang, S., Jia, H., & Li, K. X. (2019). *How big data enriches maritime research – a critical review of Automatic Identification System (AIS) data applications*. Transport Reviews **39**, no. 6, 755-773. doi: [10.1080/01441647.2019.1649315](https://doi.org/10.1080/01441647.2019.1649315)

> AIS was developed in the 1990s, with the primary goal of preventing ship collisions and
> enhancing navigation safety. Through the use of VHF, ships equipped with AIS can broadcast
> and receive messages to and from other ships or coastal authorities that are also
> equipped with AIS. The AIS enables ships and coastal authorities to communicate with
> one another over a long distance. The International Maritime Organization (IMO) requires
> all international voyage ships with a gross tonnage above 300, and all passenger ships, to
> be equipped with an AIS transmitter (IALA, 2004). In addition to the IMO, governments and
> other authorities in different nations enforce AIS applications in ships registered with them
> to improve safety and security.
>
> The AIS transceivers are of two types (Classes A and B), having different numbers of
> reported data fields and reporting frequencies. The information broadcast by a ship’s
> AIS transceiver (Class A) can be grouped into 11 data fields, which can be further classified
> into 3 types, namely, static information, dynamic information, and voyage-related information.
> Dynamic information is automatically transmitted by a Class A AIS transceiver
> every 2–10 s, depending on the ship’s speed while it is underway, and every 3 min
> while it is anchored. At the same time, a Class A AIS transceiver’s interval between
> broadcasting static and voyage-related information is 6 min, regardless of navigational status.
> Class B transponders transmit a reduced set of data when compared with Class A transponders,
> omitting the IMO number, draught, destination, ETA, rate of turn, and navigational status.
> The reporting intervals from Class B transponders are also sparser when
> compared with those of Class A transponders, being a minimum of 5 s. Table 2 provides
> a detailed classification and description of these data fields.

<table>
  <thead>
    <tr>
      <th>Table 2. Attributes of AIS data.</th>
    </tr>
    <tr>
      <th>Data field</th>
      <th>Type</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>AIS identity and location</td>
      <td>Static</td>
      <td>Maritime Mobile Service Identity (MMSI) and the location of the system’s antenna on board</td>
    </tr>
    <tr>
      <td>Ship identity</td>
      <td>Static</td>
      <td>Ship name, IMO number, type, and call sign of the ship</td>
    </tr>
    <tr>
      <td>Ship size</td>
      <td>Static</td>
      <td>Length and width of the ship</td>
    </tr>
    <tr>
      <td>Ship position</td>
      <td>Dynamic</td>
      <td>Latitude and longitude (up to 0.0001 min accuracy)</td>
    </tr>
    <tr>
      <td>Speed</td>
      <td>Dynamic</td>
      <td>Ranging from 0 knot to 102 knots (0.1 knot resolution)</td>
    </tr>
    <tr>
      <td>Rate of turn</td>
      <td>Dynamic</td>
      <td>Right or left (ranging from 0 to 720° per minute)</td>
    </tr>
    <tr>
      <td>Navigation direction</td>
      <td>Dynamic</td>
      <td>Shipping course, heading, and bearing of the ship</td>
    </tr>
    <tr>
      <td>Time stamp</td>
      <td>Dynamic</td>
      <td>Second field of the UTC time when the subject data packet was generated</td>
    </tr>
    <tr>
      <td>Navigation status</td>
      <td>Dynamic</td>
      <td>Includes “at anchor,” “under way using engine(s),” and “not under command”</td>
    </tr>
    <tr>
      <td>Destination and ETA</td>
      <td>Voyage-related</td>
      <td>Destination port and the estimated time of arrival of the ship</td>
    </tr>
    <tr>
      <td>Draught</td>
      <td>Voyage-related</td>
      <td>Ranges from 0.1 m to 25.5 m</td>
    </tr>
  </tbody>
</table>