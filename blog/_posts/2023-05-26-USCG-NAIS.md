---
layout: post
title: USCG Nationwide Automatic Identification System (NAIS)
topic: readings
---

{% include toc %}

# U.S. Coast Guard Acquisition Directorate

[Nationwide Automatic Identification System \| U.S. Coast Guard Acquisition Directorate](https://www.dcms.uscg.mil/Our-Organization/Assistant-Commandant-for-Acquisitions-CG-9/Programs/C4ISR-Programs/nais/)

> The Nationwide Automatic Identification System (NAIS) has enhanced the Coast Guard’s maritime domain awareness (MDA) of vessels operating in or approaching the nation’s waterways, ports and infrastructure. The system was based on the Automatic Identification System which was sanctioned by the International Maritime Organization as a global standard for ship-to-ship, ship-to-shore, and shore-to-ship communication. Permanent NAIS systems have been installed at 134 sites across 37 sectors. On a daily basis, NAIS receives approximately 120 million messages and provides data feeds to over 80 Coast Guard and other government agency systems. NAIS transitioned to sustainment in August 2018; two contracts are in place to provide corrective maintenance as well as engineering support services for information assurance, system administration, grooming processes and detailed troubleshooting requirements.
>
> NAIS contributes to a the concept of maritime domain awareness, which is a joint Coast Guard and U.S. Navy term for the effective understanding of anything associated with the global maritime domain that could impact the security, safety, economy or environment of the United States. By providing accurate information on vessel traffic to and from U.S. ports, NAIS helps to build a foundation of data that the government can use to develop effective maritime homeland security strategies.
>
> **Features**  
> - Land, sea and space-based AIS radio frequency infrastructure capable of receiving and transmitting information from and to AIS-equipped vessels in U.S. coastal zones, waterways and ports
> - Integrated AIS data storage, processing and networking infrastructure

[Coast Guard celebrates NAIS full operational capability milestone. Aug. 22, 2018 \| United States Coast Guard Acquisition Directorate](https://www.dcms.uscg.mil/Our-Organization/Assistant-Commandant-for-Acquisitions-CG-9/Newsroom/Latest-Acquisition-News/Article/1609227/coast-guard-celebrates-nais-full-operational-capability-milestone/)

> The Coast Guard’s Nationwide Automatic Identification System (NAIS) achieved full operational capability (FOC) on May 24, 2018.
>
> Jewuan Davis, program manager for the NAIS program (CG-9332), explained that FOC was achieved when the capability had been “deployed and accepted at the 58 critical ports and 11 waterways identified in the NAIS Operational Requirements document.” Currently, permanent transceiver systems are deployed and fully operational at 134 total regional sites, providing operational coverage of the 58 critical ports and 11 waterways. On a daily basis, NAIS receives an average of over 264 million vessel messages and provides data feeds to over 80 Coast Guard and other government agency systems worldwide.
>
> The milestone was recognized during a ceremony at Coast Guard Headquarters on July 26, 2018. In attendance were Rear Adm. Michael Ryan (CG-7), Rear Adm. Michael Johnston (CG-93) and Rear Adm. Michael Haycock (CG-9). During the ceremony, the flag officers shared real stories of how NAIS was used to enhance maritime domain awareness (MDA) across the Coast Guard.
>
> The NAIS acquisition stemmed from the Maritime Transportation Security Act of 2002 which directed requirements to establish a system of effective maritime domain awareness and security for every port act of 2006. MDA is defined as the effective understanding of anything associated with the maritime domain that could impact the security, safety, economy or environment. “The Coast Guard is the lead federal agency for maritime security, maritime safety, maritime mobility, national defense in U.S. coastal waters and protection of natural resources in U.S. coastal waters,” said Davis, “NAIS is critical to the Coast Guard’s ability to fulfill its responsibilities in those areas.”
>
> NAIS enables the Coast Guard to maintain MDA by providing a comprehensive view of the nation’s waters. As a result, decision makers are better positioned to respond to safety and security risks; improve the safety of vessels and ports through collision avoidance; and strengthen national security through the detection, identification, and classification of potential threats from offshore.
>
> The NAIS program started in 2004. Reflecting on the process 14 years later, Davis said, “A lot of detailed planning, interagency coordination, and hard work was invested into the successful completion of this milestone and full delivery of this capability to the Coast Guard’s operational users.” There are many contributors to thank for the success including the entire NAIS Program Management Office team and previous program managers and team members who put hard work and diligence into the early stages of developing NAIS. Davis extends a special thanks to the Office of Command, Control, Communications, Computer and Sensors Capabilities (CG-761); Sustainment Manager (CG-681); NAIS product line team at Command, Control, and Communications Engineering Center and all operational users for “helping us continually improve and refine the tool into the critical asset it is today.”
>
> The next major milestone for the NAIS acquisition program will be the completion of acquisition decision event 4, acquisition gate review and transition of management responsibility for NAIS from acquisitions to the sustainment community, scheduled to occur in the fourth quarter of fiscal year 2018. After that point, the sustainment community will assume responsibility for the continued maintenance of NAIS and managing technical refreshes of the capability to keep the system up to date.

# U.S. Coast Guard Navigation Center (NAVCEN)

[U.S. Coast Guard Navigation Center (NAVCEN)](https://www.navcen.uscg.gov/)

## Vessel Information Verification Service (VIVS)

[Vessel Information Verification Service (VIVS)](https://navcen.uscg.gov/ais-vivs-home)

## Class A AIS Reports

[Class A AIS Position Report (Messages 1, 2, and 3) \| NAVCEN](https://navcen.uscg.gov/ais-class-a-reports)

> A Class A AIS unit broadcasts the following information every 2 to 10 seconds while underway, and every 3 minutes while at anchor at a power level of 12.5 watts.

<table>
<thead>
  <tr>
    <th>Parameter</th>
    <th>Bits</th>
    <th>Description</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Message ID</td>
    <td>6</td>
    <td>Identifier for this message 1, 2 or 3</td>
  </tr>
  <tr>
    <td>Repeat indicator</td>
    <td>2</td>
    <td>Used by the repeater to indicate how many times a message has been repeated. See Section 4.6.1, Annex 2; 0-3; 0 = default; 3 = do not repeat any more.</td>
  </tr>
  <tr>
    <td>User ID</td>
    <td>30</td>
    <td>MMSI number</td>
  </tr>
  <tr>
    <td>Navigational status</td>
    <td>4</td>
    <td>0 = under way using engine, 1 = at anchor, 2 = not under command, 3 = restricted maneuverability, 4 = constrained by her draught, 5 = moored, 6 = aground, 7 = engaged in fishing, 8 = under way sailing, 9 = reserved for future amendment of navigational status for ships carrying DG, HS, or MP, or IMO hazard or pollutant category C, high speed craft (HSC), 10 = reserved for future amendment of navigational status for ships carrying dangerous goods (DG), harmful substances (HS) or marine pollutants (MP), or IMO hazard or pollutant category A, wing in ground (WIG); 11 = power-driven vessel towing astern (regional use); 12 = power-driven vessel pushing ahead or towing alongside (regional use);<br>13 = reserved for future use,<br>14 = AIS-SART (active), MOB-AIS, EPIRB-AIS<br>15 = undefined = default (also used by AIS-SART, MOB-AIS and EPIRB-AIS under test)</td>
  </tr>
  <tr>
    <td>Rate of turn<br>ROT<sub>AIS</sub></td>
    <td>8</td>
    <td>0 to +126 = turning right at up to 708 deg per min or higher<br>0 to -126 = turning left at up to 708 deg per min or higher Values between 0 and 708 deg per min coded by ROT<sub>AIS</sub> = 4.733 SQRT(ROT<sub>sensor</sub>) degrees per min where ROT<sub>sensor</sub> is the Rate of Turn as input by an external Rate of Turn Indicator (TI). ROT<sub>AIS</sub> is rounded to the nearest integer value.<br>+127 = turning right at more than 5 deg per 30 s (No TI available)<br>-127 = turning left at more than 5 deg per 30 s (No TI available)<br>-128 (80 hex) indicates no turn information available (default).<br>ROT data should not be derived from COG information.</td>
  </tr>
  <tr>
    <td>SOG</td>
    <td>10</td>
    <td>Speed over ground in 1/10 knot steps (0-102.2 knots)<br>1 023 = not available, 1 022 = 102.2 knots or higher</td>
  </tr>
  <tr>
    <td>Position accuracy</td>
    <td>1</td>
    <td>The position accuracy (PA) flag should be determined in accordance with the table below:<br>1 = high (&lt;= 10 m)<br>0 = low (&gt; 10 m)<br>0 = default</td>
  </tr>
  <tr>
    <td>Longitude</td>
    <td>28</td>
    <td>Longitude in 1/10 000 min (+/-180 deg, East = positive (as per 2's complement), West = negative (as per 2's complement).<br>181= (6791AC0h) = not available = default)</td>
  </tr>
  <tr>
    <td>Latitude</td>
    <td>27</td>
    <td>Latitude in 1/10 000 min (+/-90 deg, North = positive (as per 2's complement), South = negative (as per 2's complement). 91deg (3412140h) = not available = default)</td>
  </tr>
  <tr>
    <td>COG</td>
    <td>12</td>
    <td>Course over ground in 1/10 = (0-3599). 3600 (E10h) = not available = default. 3 601-4 095 should not be used</td>
  </tr>
  <tr>
    <td>True heading</td>
    <td>9</td>
    <td>Degrees (0-359) (511 indicates not available = default)</td>
  </tr>
  <tr>
    <td>Time stamp</td>
    <td>6</td>
    <td>UTC second when the report was generated by the electronic position system (EPFS) (0-59, or 60 if time stamp is not available, which should also be the default value, or 61 if positioning system is in manual input mode, or 62 if electronic position fixing system operates in estimated (dead reckoning) mode, or 63 if the positioning system is inoperative)</td>
  </tr>
  <tr>
    <td>special maneuvre indicator</td>
    <td>2</td>
    <td>0 = not available = default<br>1 = not engaged in special maneuver<br>2 = engaged in special maneuver<br>(i.e.: regional passing arrangement on Inland Waterway)</td>
  </tr>
  <tr>
    <td>Spare</td>
    <td>3</td>
    <td>Not used. Should be set to zero. Reserved for future use.</td>
  </tr>
  <tr>
    <td>RAIM-flag</td>
    <td>1</td>
    <td>Receiver autonomous integrity monitoring (RAIM) flag of electronic position fixing device; 0 = RAIM not in use = default; 1 = RAIM in use. See Table</td>
  </tr>
  <tr>
    <td>Communication state (see below)</td>
    <td>19</td>
    <td>See Rec. ITU-R M.1371-5 Table 49</td>
  </tr>
  <tr>
    <td>Number of bits</td>
    <td>168</td>
    <td> </td>
  </tr>
</tbody>
</table>

> Communications State (19 bit field): The Communications State in Class A AIS Position Report messages is used in planning for the next transmission in order to avoiding mutual interference. It is inherent to the self organizing time division multiple access (SOTDMA) process. This information, along with the 6 bit time stamp information identified above, can also provide information on the existence of radio interference or other anomalies affecting reception of GPS signals in the local area.

## USCG AIS Encoding Guide v.25

[USCG AIS Encoding Guide v.25](https://www.navcen.uscg.gov/sites/default/files/pdf/AIS/AISGuide.pdf)

> This Guide is intended to assist in the
> proper encoding of an Automatic
> Identification System (AIS) used in
> U.S. navigable waters

### Static data

> **Static Data**…should be encoded at installation and reflect the
vessel’s official radio license or documentation

> **Maritime Mobile Service Identity (MMSI)** must reflect the MMSI assigned to the vessel by the FCC or one of its agents.
>
> **Vessel Names** that exceed the AIS’s 20 character limit should be shortened
> (not truncated) to 15 character-spaces, followed by an underscore \{\_\},
> thence the last 4 characters-spaces of the vessel name, e.g. GRAND JOLLY
> ROGER OF THE SEA to GRAND JOLLY OF \_ SEA, THE GRAND JOLLY ROGER to THE
> GRAND JOLLY_OGER. Names should not include vessel type precursors, e.g.
> F/V, M/V, MV, OSV, P/V, REC, S/V, T/B; except public vessels, e.g. CG, CBP, USN,
> LAPD, NYFD, WSF. Undocumented vessels should reflect the vessel’s state
> registration number−vice name̶−preceded by ‘US#’, e.g. US#AZ1234YZ.
>
> **Call-sign** must reflect the call-sign assigned to the vessel by
the FCC; absent an assignment, leave blank.
>
> **IMO Number** must reflect the assigned 7-digit IMO number.
> Use leading zeroes (not trailing zeroes) to fill the parameter,
> e.g. 0001234567. U.S. vessels without an IMO assignment
> should (if your AIS is 10-digit capable) input their U.S. official
> number preceded by ‘10000’, e.g. 1001234567, 1000123456.
>
> **Type of positioning source** must reflect the
> actual positioning system in use; i.e. interfaced
> to the AIS or the internal AIS EPFS.
>
> **Type of vessel (and cargo)** should reflect the
> appropriate Ship Type listed in the Table; but,
> not its cargo type.
>
> **Antenna Position \| Dimensions (ABCD values)**
> must be encoded in meters, not feet, and reflect
> the overall dimensions of the vessel, ABDC
> values expressed as the distance fore (A), aft
> (B), to port (C), and to starboard (D) to the
> positioning-system antenna used by AIS; the
> intersection of the two white lines in the
> diagram. Improper calibration or encoding could
> navigation safety.

### Voyage Related Data

> **Voyage Related Data**…should be encoded as needed
and kept accurate and up to date
>
> **Navigation Status** must always be up-to-date, i.e. at anchor,
> underway, engaged in fishing, etc. Vessels engaged in towing,
> if capable, should use Navigation Status ‘11’ when towing
> astern or ‘12’ when pushing ahead or alongside.
>
> Remember to change update your status when at anchor
or moored, which reduces AIS reporting rates to every 3
minutes; thus mitigates network congestion and
improves overall AIS efficiency and range.
>
> **Static Draft** must be encoded in meters, not feet, and reflect
> the vessel’s actual or maximum draft.
>
> **People on Board (POB)**, although some legacy AIS devices
allow for POB reporting it is not required.
>
> **Estimated Time of Arrival (ETA)** must be encoded in
> Universal Time Coordinated (UTC), not local time; and, reflect
> the ETA to your destination or voyage departure time, if
> moored or anchored. Not applicable to vessels on unknown
> or variable schedules (e.g. workboats).

# U.S. Army Corps of Engineers (USACE)

[U.S. Army Corps of Engineers (USACE)](https://www.usace.army.mil/)

[U.S. Army Engineer Research and Development Center (ERDC)](https://www.erdc.usace.army.mil/)

[AIS 101. 10 May 2021. Brian Tetreault. Coastal and Hydraulics Laboratory. Engineer Research and Development Center](https://cirp.usace.army.mil/techtransfer/workshops/Shoaling2021/AIS101_20210507.pdf)

[AIS 101. 09 January 2019. Brian Tetreault. Coastal and Hydraulics Laboratory. Engineer Research and Development Center](https://cirp.usace.army.mil/techtransfer/workshops/AIS2019/files/Day2_AIS101_Tetreault.pdf)