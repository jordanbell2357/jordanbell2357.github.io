---
layout: post
title: Rec. ITU-R M.1371-5
---

[M.1371 : Technical characteristics for an automatic identification system using time division multiple access in the VHF maritime mobile frequency band (Rec. ITU-R M.1371-5) \| ITU](https://www.itu.int/rec/R-REC-M.1371-5-201402-I/en)

<table>
  <caption>Table 1: Class A shipborne mobile equipment reporting intervals</caption>
  <thead>
    <tr>
      <th>Ship’s dynamic conditions</th>
      <th>Nominal reporting interval</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Ship at anchor or moored and not moving faster than 3 knots</td>
      <td>3 min</td>
    </tr>
    <tr>
      <td>Ship at anchor or moored and moving faster than 3 knots</td>
      <td>10 s</td>
    </tr>
    <tr>
      <td>Ship 0-14 knots</td>
      <td>10 s</td>
    </tr>
    <tr>
      <td>Ship 0-14 knots and changing course</td>
      <td>3 1/3 s</td>
    </tr>
    <tr>
      <td>Ship 14-23 knots</td>
      <td>6 s</td>
    </tr>
    <tr>
      <td>Ship 14-23 knots and changing course</td>
      <td>2 s</td>
    </tr>
    <tr>
      <td>Ship > 23 knots</td>
      <td>2 s</td>
    </tr>
    <tr>
      <td>Ship > 23 knots and changing course</td>
      <td>2 s</td>
    </tr>
  </tbody>
</table>

<table>
  <caption>Table 2: Reporting intervals for equipment other than Class A shipborne mobile equipment</caption>
  <thead>
    <tr>
      <th>Platform’s condition</th>
      <th>Nominal reporting interval</th>
      <th>Increased reporting interval</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Class B "SO" shipborne mobile equipment not moving faster than 2 knots</td>
      <td>3 min</td>
      <td>3 min</td>
    </tr>
    <tr>
      <td>Class B "SO" shipborne mobile equipment moving 2-14 knots</td>
      <td>30 s</td>
      <td>30 s</td>
    </tr>
    <tr>
      <td>Class B "SO" shipborne mobile equipment moving 14-23 knots</td>
      <td>15 s</td>
      <td>30 s</td>
    </tr>
    <tr>
      <td>Class B "SO" shipborne mobile equipment moving >23 knots</td>
      <td>5 s</td>
      <td>15 s</td>
    </tr>
    <tr>
      <td>Class B "CS" shipborne mobile equipment not moving faster than 2 knots</td>
      <td>3 min</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Class B "CS" shipborne mobile equipment moving faster than 2 knots</td>
      <td>30 s</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Search and rescue aircraft (airborne mobile equipment)</td>
      <td>10 s</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Aids to navigation</td>
      <td>3 min</td>
      <td>-</td>
    </tr>
    <tr>
      <td>AIS base station</td>
      <td>10 s</td>
      <td>-</td>
    </tr>
  </tbody>
</table>


<table>
  <caption>Table 48</caption>
  <tr>
    <th>Parameter</th>
    <th>Number of bits</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>Message ID</td>
    <td>6</td>
    <td>Identifier for this Message 1, 2 or 3</td>
  </tr>
  <tr>
    <td>Repeat indicator</td>
    <td>2</td>
    <td>Used by the repeater to indicate how many times a message has been repeated. See § 4.6.1, Annex 2; 0-3; 0 = default; 3 = do not repeat any more</td>
  </tr>
  <tr>
    <td>User ID</td>
    <td>30</td>
    <td>Unique identifier such as MMSI number</td>
  </tr>
  <tr>
    <td>Navigational status</td>
    <td>4</td>
    <td>0 = under way using engine, 1 = at anchor, 2 = not under command, 3 = restricted maneuverability, 4 = constrained by her draught, 5 = moored, 6 = aground, 7 = engaged in fishing, 8 = under way sailing, 9 = reserved for future amendment of navigational status for ships carrying DG, HS, or MP, or IMO hazard or pollutant category C, high speed craft (HSC), 10 = reserved for future amendment of navigational status for ships carrying dangerous goods (DG), harmful substances (HS) or marine pollutants (MP), or IMO hazard or pollutant category A, wing in ground (WIG); 11 = power-driven vessel towing astern (regional use), 12 = power-driven vessel pushing ahead or towing alongside (regional use); 13 = reserved for future use, 14 = AIS-SART (active), MOB-AIS, EPIRB-AIS 15 = undefined = default (also used by AIS-SART, MOB-AIS and EPIRB-AIS under test)</td>
  </tr>
  <tr>
    <td>Rate of turn ROTAIS</td>
    <td>8</td>
    <td>0 to +126 = turning right at up to 708° per min or higher 0 to –126 = turning left at up to 708° per min or higher Values between 0 and 708° per min coded by ROTAIS = 4.733 SQRT(ROTsensor) degrees per min where ROTsensor is the Rate of Turn as input by an external Rate of Turn Indicator (TI). ROTAIS is rounded to the nearest integer value. +127 = turning right at more than 5° per 30 s (No TI available) –127 = turning left at more than 5° per 30 s (No TI available) –128 (80 hex) indicates no turn information available (default). ROT data should not be derived from COG information.</td>
  </tr>
  <tr>
    <td>SOG</td>
    <td>10</td>
    <td>Speed over ground in 1/10 knot steps (0-102.2 knots) 1 023 = not available, 1 022 = 102.2 knots or higher</td>
  </tr>
  <tr>
    <td>Position accuracy</td>
    <td>1</td>
    <td>The position accuracy (PA) flag should be determined in accordance with Table 50 1 = high (≤ 10 m) 0 = low (>10 m) 0 = default</td>
  </tr>
  <tr>
    <td>Longitude</td>
    <td>28</td>
    <td>Longitude in 1/10 000 min (±180°, East = positive (as per 2’s complement), West = negative (as per 2’s complement). 181 = (6791AC0h) = not available = default)</td>
  </tr>
  <tr>
    <td>Latitude</td>
    <td>27</td>
    <td>Latitude in 1/10 000 min (±90°, North = positive (as per 2’s complement), South = negative (as per 2’s complement). 91° (3412140h) = not available = default)</td>
  </tr>
  <tr>
    <td>COG</td>
    <td>12</td>
    <td>Course over ground in 1/10 = (0-3 599). 3 600 (E10h) = not available = default. 3 601-4 095 should not be used</td>
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
    <td>Special manoeuvre indicator</td>
    <td>2</td>
    <td>0 = not available = default 1 = not engaged in special manoeuvre 2 = engaged in special manoeuvre (i.e. regional passing arrangement on Inland Waterway)</td>
  </tr>
  <tr>
    <td>Spare</td>
    <td>3</td>
    <td>Not used. Should be set to zero. Reserved for future use.</td>
  </tr>
  <tr>
    <td>RAIM-flag</td>
    <td>1</td>
    <td>Receiver autonomous integrity monitoring (RAIM) flag of electronic position fixing device; 0 = RAIM not in use = default; 1 = RAIM in use. See Table 50</td>
  </tr>
  <tr>
    <td>Communication state</td>
    <td>19</td>
    <td>See Table 49</td>
  </tr>
  <tr>
    <td>Number of bits</td>
    <td>168</td>
    <td></td>
  </tr>
</table>



<table>
 <caption>Table 48: Navigational status</caption>
<thead>
  <tr>
    <th>Navigation Status:</th>
    <th>Description:</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>0</td>
    <td>Under way using engine</td>
  </tr>
  <tr>
    <td>1</td>
    <td>At anchor</td>
  </tr>
  <tr>
    <td>2</td>
    <td>Not under command</td>
  </tr>
  <tr>
    <td>3</td>
    <td>Restricted maneuverability</td>
  </tr>
  <tr>
    <td>4</td>
    <td>Constrained by her draught</td>
  </tr>
  <tr>
    <td>5</td>
    <td>Moored</td>
  </tr>
  <tr>
    <td>6</td>
    <td>Aground</td>
  </tr>
  <tr>
    <td>7</td>
    <td>Engaged in fishing</td>
  </tr>
  <tr>
    <td>8</td>
    <td>Under way sailing</td>
  </tr>
  <tr>
    <td>9</td>
    <td>Reserved for future amendment of navigational status for ships carrying DG, HS, or MP, or IMO hazard or pollutant category C, high-speed craft (HSC)</td>
  </tr>
  <tr>
    <td>10</td>
    <td>Reserved for future amendment of navigational status for ships carrying dangerous goods (DG), harmful substances (HS) or marine pollutants (MP), or IMO hazard or pollutant category A, wing in ground (WIG)</td>
  </tr>
  <tr>
    <td>11</td>
    <td>Power-driven vessel towing astern (regional use)</td>
  </tr>
  <tr>
    <td>12</td>
    <td>Power-driven vessel pushing ahead or towing alongside (regional use)</td>
  </tr>
  <tr>
    <td>13</td>
    <td>Reserved for future use</td>
  </tr>
  <tr>
    <td>14</td>
    <td>AIS-SART (active), MOB-AIS, EPIRB-AIS</td>
  </tr>
  <tr>
    <td>15</td>
    <td>Undefined = default (also used by AIS-SART, MOB-AIS, and EPIRB-AIS under test)</td>
  </tr>
</tbody>
</table>




<table>
  <caption>Table 53</caption>
  <tr>
    <th>Identifier No.</th>
    <th>Special craft</th>
  </tr>
  <tr>
    <td>50</td>
    <td>Pilot vessel</td>
  </tr>
  <tr>
    <td>51</td>
    <td>Search and rescue vessels</td>
  </tr>
  <tr>
    <td>52</td>
    <td>Tugs</td>
  </tr>
  <tr>
    <td>53</td>
    <td>Port tenders</td>
  </tr>
  <tr>
    <td>54</td>
    <td>Vessels with anti-pollution facilities or equipment</td>
  </tr>
  <tr>
    <td>55</td>
    <td>Law enforcement vessels</td>
  </tr>
  <tr>
    <td>56</td>
    <td>Spare – for assignments to local vessels</td>
  </tr>
  <tr>
    <td>57</td>
    <td>Spare – for assignments to local vessels</td>
  </tr>
  <tr>
    <td>58</td>
    <td>Medical transports (as defined in the 1949 Geneva Conventions and Additional Protocols)</td>
  </tr>
  <tr>
    <td>59</td>
    <td>Ships and aircraft of States not parties to an armed conflict</td>
  </tr>
</table>


<table>
  <caption>Table 53 - Other ships</caption>
  <tr>
    <th>First digit(1)</th>
    <th>Second digit(1)</th>
    <th>First digit(1)</th>
    <th>Second digit(1)</th>
  </tr>
  <tr>
    <td>1 – Reserved for future use</td>
    <td>0 – All ships of this type</td>
    <td>–</td>
    <td>0 – Fishing</td>
  </tr>
  <tr>
    <td>2 – WIG</td>
    <td>1 – Carrying DG, HS, or MP, IMO hazard or pollutant category X(2)</td>
    <td>–</td>
    <td>1 – Towing</td>
  </tr>
  <tr>
    <td>3 – See right column</td>
    <td>2 – Carrying DG, HS, or MP, IMO hazard or pollutant category Y(2)</td>
    <td>3 – Vessel</td>
    <td>2 – Towing and length of the tow exceeds 200 m or breadth exceeds 25 m</td>
  </tr>
  <tr>
    <td>4 – HSC</td>
    <td>3 – Carrying DG, HS, or MP, IMO hazard or pollutant category Z(2)</td>
    <td>–</td>
    <td>3 – Engaged in dredging or underwater operations</td>
  </tr>
  <tr>
    <td>5 – See above</td>
    <td>4 – Carrying DG, HS, or MP, IMO hazard or pollutant category OS(2)</td>
    <td>–</td>
    <td>4 – Engaged in diving operations</td>
  </tr>
  <tr>
    <td>5 – Reserved for future use</td>
    <td>–</td>
    <td>5 – Engaged in military operations</td>
    <td>6 – Passenger ships</td>
  </tr>
  <tr>
    <td>6 – Reserved for future use</td>
    <td>–</td>
    <td>6 – Sailing</td>
    <td>7 – Cargo ships</td>
  </tr>
  <tr>
    <td>7 – Reserved for future use</td>
    <td>–</td>
    <td>7 – Pleasure craft</td>
    <td>8 – Tanker(s)</td>
  </tr>
  <tr>
    <td>8 – Reserved for future use</td>
    <td>–</td>
    <td>8 – Reserved for future use</td>
    <td>9 – Other types of ship</td>
  </tr>
  <tr>
    <td>9 – No additional information</td>
    <td>–</td>
    <td>9 – Reserved for future use</td>
    <td></td>
  </tr>
</table>
