---
layout: post
title: USCG Nationwide Automatic Identification System (NAIS)
topic: readings
---

[Nationwide Automatic Identification System \| United States Coast Guard Acquisition Directorate](https://www.dcms.uscg.mil/Our-Organization/Assistant-Commandant-for-Acquisitions-CG-9/Programs/C4ISR-Programs/nais/)

> The Nationwide Automatic Identification System (NAIS) has enhanced the Coast Guard’s maritime domain awareness (MDA) of vessels operating in or approaching the nation’s waterways, ports and infrastructure. The system was based on the Automatic Identification System which was sanctioned by the International Maritime Organization as a global standard for ship-to-ship, ship-to-shore, and shore-to-ship communication. Permanent NAIS systems have been installed at 134 sites across 37 sectors. On a daily basis, NAIS receives approximately 120 million messages and provides data feeds to over 80 Coast Guard and other government agency systems. NAIS transitioned to sustainment in August 2018; two contracts are in place to provide corrective maintenance as well as engineering support services for information assurance, system administration, grooming processes and detailed troubleshooting requirements.
>
> NAIS contributes to a the concept of maritime domain awareness, which is a joint Coast Guard and U.S. Navy term for the effective understanding of anything associated with the global maritime domain that could impact the security, safety, economy or environment of the United States. By providing accurate information on vessel traffic to and from U.S. ports, NAIS helps to build a foundation of data that the government can use to develop effective maritime homeland security strategies.
>
> **Features**  
> - Land, sea and space-based AIS radio frequency infrastructure capable of receiving and transmitting information from and to AIS-equipped vessels in U.S. coastal zones, waterways and ports
> - Integrated AIS data storage, processing and networking infrastructure

[U.S. Coast Guard Navigation Center (NAVCEN)](https://www.navcen.uscg.gov/) [^1]

[^1]: [NAVCEN \| NIST](https://csrc.nist.gov/glossary/term/navcen)



[Class A Reports \| NAVCEN](https://navcen.uscg.gov/ais-class-a-reports)

[Maritime Mobile Service Identity \| NAVCEN](https://www.navcen.uscg.gov/maritime-mobile-service-identity)

MMSI Format
Maritime Identification Digits (MID)
MIDs are three digit identifiers ranging from 201 to 775 denoting the administration (country) or geographical area of the administration responsible for the ship station so identified. See the [ITU Table of Maritime Identification Digits](https://www.itu.int/en/ITU-R/terrestrial/fmd/Pages/mid.aspx).

Ships
All ship MMSIs use the format M1 I2D3X4X5X6X7X8X9 where in the first three digits represent the Maritime Identification Digits (MID) and X is any figure from 0 to 9. (Hint: Ships transmitting with an MMSI not starting with the digits 201-775 are likely doing so improperly, and may be subject to FCC or USCG enforcement action).

Groups of Ships (DSC only)
Group ship station call identities for calling simultaneously more than one ship use the format 01M2I3D4X5X6X7X8X9, where the first figure is zero and X is any figure from 0 to 9. The MID represents only the territory or geographical area of the administration assigning the group ship station call identity and does not prevent group calls to fleets containing more than one ship nationality.

No process currently exists to assign non-federal group ship station identities. However, users having an MMSI assigned by FCC license, all of which have a trailing zero, may create a group identity by inserting a zero before the identity and removing the trailing zero (e.g. a user having an MMSI of 366123450 is allowed to use the group identity 036612345).

The U.S. Coast Guard group ship station call identity is 036699999.

Coast Radio Stations (Base Stations)
All coast or base stations use the format 0102M3I4D5X6X7X8X9,where the digits 3, 4 and 5 represent the MID and X is any figure from 0 to 9. Groups of DSC coast radio stations use the same format.

The combination 0102M3I4D506070809 is used to address all 00MIDXXXX DSC stations within the administration. The combination 010293949506070809 is used to address all VHF DSC 00MIDXXXX stations worldwide. These two special combinations are not used in the United States.

The U.S. Coast Guard DSC group coast station identity is 003669999.

Search and Rescue Aircraft
AIS and DSC equipment used on search and rescue aircraft use the format 111213M4I5D6X7X8X9 where the digits 4, 5 and 6 represent the MID and X is any figure from 0 to 9. In the United States, these MMSIs are currently only used by the U.S. Coast Guard.

AIS Aids to Navigation (AtoN)
AIS used as an aid to navigation uses the format 9192M3I4D5X6X7X8X9 where the digits 3, 4 and 5 represent the MID and X is any figure from 0 to 9. In the United States, these MMSIs are reserved for the federal government.

Craft Associated with a Parent Ship
Stations used on craft associated with a parent ship, such as a launches, tenders, towed vessels, etc. may use the format 9182M3I4D5X6X7X8X9 where the digits 3, 4 and 5 represent the MID and X is any figure from 0 to 9. However, no provision currently exists for assigning these identities in the United States. Thus U.S. craft associated with a parent ship must obtain and use a ships MMSI specifically assigned by the FCC or one of their agents. AIS stations used on such vessels, in lieu of an official call-sign should enter “A” followed by the last 6 digits of the MMSI of the parent vessel onto their AIS Call Sign parameter.

AIS Search and Rescue Transmitter (SART)
AIS search and rescue transmitters (SART) use the format 917203X4X5Y6Y7Y8Y9, where the digits 4 and 5 are assigned by the International Association for Marine Electronics Companies (CIRM) and refer to the SART manufacturer, and digits 6, 7, 8 and 9 are sequential digits assigned by the manufacturer identifying the SART.

MOB (Man overboard) (RTCM SC119)
The MOB (Man overboard) device that transmits DSC and/or AIS should use an identity
917223X4X5Y6Y7Y8Y9,  (where xx = manufacturer ID 01 to 99 assigned by CIRM; yyyy = the sequence number 0000 to 9999. When reaching 9999 the manufacturer should restart the sequence numbering at 0000.The manufacturer ID xx = 00 is reserved for test purposes).   Combination DSC AIS devices will transmit one common user ID.

EPIRB-AIS (RTCM SC110)
The EPIRB-AIS should use an identity 917243X4X5Y6Y7Y8Y9,  (where xx = manufacturer ID 01 to 99; yyyy = the sequence number 0000 to 9999. When reaching 9999 the manufacturer should restart the sequence numbering at 0000.).

The user identity of the EPIRB-AIS indicates the identity of the homing device of the EPIRB-AIS, and not the MMSI of the ship.












[AUTOMATIC IDENTIFICATION SYSTEM USCG AIS Encoding Guide v.25](https://www.navcen.uscg.gov/sites/default/files/pdf/AIS/AISGuide.pdf)