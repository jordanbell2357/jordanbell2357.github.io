---
layout: post
title: BarentsWatch AIS API and curl
---

[Application registration and authentication](https://developer.barentswatch.no/docs/appreg/)

[My page \| BarentsWatch](https://www.barentswatch.no/minside/)

[BarentsWatch AIS Live OpenAPI Documentation](https://live.ais.barentswatch.no/index.html)


# API token

```bash
client_id= #client_id
client_secret= #client_secret
```

```bash
curl -X POST --header "Content-Type: application/x-www-form-urlencoded" \
-d "client_id=$client_id&scope=ais&client_secret=$client_secret&grant_type=client_credentials" \
https://id.barentswatch.no/connect/token > token.json
```

Valid for 3600 seconds (1 hour).

```bash
access_token=$(jq -r '.access_token' token.json)
```

```bash
echo $access_token
```

```
eyJhbGciOiJSUzI1NiIsImtpZCI6IjBCM0I1NEUyRkQ5OUZCQkY5NzVERDMxNDBDREQ4OEI1QzA5RkFDRjNSUzI1NiIsIng1dCI6IkN6dFU0djJaLTctWFhkTVVETjJJdGNDZnJQTSIsInR5cCI6ImF0K2p3dCJ9.eyJpc3MiOiJodHRwczovL2lkLmJhcmVudHN3YXRjaC5ubyIsIm5iZiI6MTY4MjAzNTU2OCwiaWF0IjoxNjgyMDM1NTY4LCJleHAiOjE2ODIwMzkxNjgsImF1ZCI6ImFpcyIsInNjb3BlIjpbImFpcyJdLCJjbGllbnRfaWQiOiJqb3JkYW4uYmVsbEBnbWFpbC5jb206am9yZGFuYmVsbDIzNTcifQ.hLX6xs3-r0b5dK0Lkxtg8wK4_UfOI5JUsukH6mnWx7EetecniYAEbQr5q2eLJtbCKqPF7Az7M-Y0MAh9Bwv0XB6KbA66sPyFTnniGj_uRLOoMoTWUZVsDIC1iuF0HFGTLptU9N7mJU_0bcLlsDA1soDSnjrMD-Gq9UetDkTQ2yFhnOtv5VbTWQcaimelglIJS5CPhQVcfQS6BS0vlCrsgyKDm1ook7-FpCbAQlmT9UiG0HLGBUYPOfxYWktFfpBzoIPc2vkrR-UdVSE6Xac_tV-ortxedTf4lp3cOIB_ikZ9mdbH_EzPZcxGcsbLQatfllc96GUXkITJyHh7dRmwrc6cFhMasmxPb0Rn7kkzf1S2Y8sjKO092SOUYSgjCBpUQIUg0n1UyngyZBiTEnKFPkMGr2UWmKOeFqMZpyeCCO1Q9hoZODKTt0UoXhdZUYbB5wMfilyGBvGEnYiqTcTfsiq66HpG33dfVfZI-8TilVwd3wXvLQvaakFhrDuQk4nCBtUsZW-5oPW5O9iScXbduL9GZIt2Zts8FQSX05is73bBjfy37Gz-8U2MmhJFJiEL5azf-aMf92ql54o3h2ZoF6GMXZOsIAB2WvE6cWaFG9flCw2Dz_SwuT3NXolIPH0NKOqsZ_Hv0YkZUKfMcrvevvttUDQW2vWYr0M-AeKfPzI
```

# curl and jq

[curl](https://everything.curl.dev/)

[jq](https://devdocs.io/jq/)

## live.ais.barentswatch.no/v1/combined

10 minutes (600 seconds):

```bash
curl --location --request GET 'https://live.ais.barentswatch.no/v1/combined' \
--header "Authorization: Bearer $access_token" --max-time 600 > AIS_2023_04_20_lines.json
```

```bash
jq --slurp '.' AIS_2023_04_20_lines.json > AIS_2023_04_20.json
```

```bash
jq '.[0]' AIS_2023_04_20.json
```

```json
{
  "courseOverGround": 188.4,
  "latitude": 58.417612,
  "longitude": 1.840345,
  "name": "ESVAGT BERGEN",
  "rateOfTurn": 5,
  "shipType": 51,
  "speedOverGround": 0.6,
  "trueHeading": 268,
  "mmsi": 220632000,
  "msgtime": "2023-04-21T01:40:34.8259595+00:00"
}
```

![Visualizing AIS_2023_04_20.json using kepler.gl](/images/BarentsWatch/keplergl_AIS_2023_04_20.png)

## live.ais.barentswatch.no/v1/latest/combined

All latest positions:

```bash
curl --location --request GET 'https://live.ais.barentswatch.no/v1/latest/combined' \
--header "Authorization: Bearer $access_token" > AIS_2023_04_20.json
```

```bash
jq '.[0]' latest_2023-04-20-UTC-01-38.json
```

```json
{
  "courseOverGround": 289,
  "latitude": 62.796623,
  "longitude": 6.904042,
  "name": "RESCUE UNE AMUNDSEN",
  "rateOfTurn": 0,
  "shipType": 51,
  "speedOverGround": 0,
  "trueHeading": 95,
  "mmsi": 257918900,
  "msgtime": "2023-04-21T01:38:11+00:00"
}
```

![Visualizing latest_2023-04-20-UTC-01-38.json using kepler.gl](/images/BarentsWatch/keplergl_latest_2023-04-20-UTC-01-38.png)


# shipType

[Type of ship/cargo \| BarentsWatch Developer](https://developer.barentswatch.no/docs/AIS/aisshiptype)

<table>
<thead>
  <tr>
    <th>Type Code</th>
    <th>Description</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>0</td>
    <td>Not available (default)</td>
  </tr>
  <tr>
    <td>1-19</td>
    <td>Reserved for future use</td>
  </tr>
  <tr>
    <td>20</td>
    <td>Wing in ground (WIG), all ships of this type</td>
  </tr>
  <tr>
    <td>21</td>
    <td>Wing in ground (WIG), Hazardous category A</td>
  </tr>
  <tr>
    <td>22</td>
    <td>Wing in ground (WIG), Hazardous category B</td>
  </tr>
  <tr>
    <td>23</td>
    <td>Wing in ground (WIG), Hazardous category C</td>
  </tr>
  <tr>
    <td>24</td>
    <td>Wing in ground (WIG), Hazardous category D</td>
  </tr>
  <tr>
    <td>25</td>
    <td>Wing in ground (WIG), Reserved for future use</td>
  </tr>
  <tr>
    <td>26</td>
    <td>Wing in ground (WIG), Reserved for future use</td>
  </tr>
  <tr>
    <td>27</td>
    <td>Wing in ground (WIG), Reserved for future use</td>
  </tr>
  <tr>
    <td>28</td>
    <td>Wing in ground (WIG), Reserved for future use</td>
  </tr>
  <tr>
    <td>29</td>
    <td>Wing in ground (WIG), Reserved for future use</td>
  </tr>
  <tr>
    <td>30</td>
    <td>Fishing</td>
  </tr>
  <tr>
    <td>31</td>
    <td>Towing</td>
  </tr>
  <tr>
    <td>32</td>
    <td>Towing: length exceeds 200m or breadth exceeds 25m</td>
  </tr>
  <tr>
    <td>33</td>
    <td>Dredging or underwater ops</td>
  </tr>
  <tr>
    <td>34</td>
    <td>Diving ops</td>
  </tr>
  <tr>
    <td>35</td>
    <td>Military ops</td>
  </tr>
  <tr>
    <td>36</td>
    <td>Sailing</td>
  </tr>
  <tr>
    <td>37</td>
    <td>Pleasure Craft</td>
  </tr>
  <tr>
    <td>38</td>
    <td>Reserved</td>
  </tr>
  <tr>
    <td>39</td>
    <td>Reserved</td>
  </tr>
  <tr>
    <td>40</td>
    <td>High speed craft (HSC), all ships of this type</td>
  </tr>
  <tr>
    <td>41</td>
    <td>High speed craft (HSC), Hazardous category A</td>
  </tr>
  <tr>
    <td>42</td>
    <td>High speed craft (HSC), Hazardous category B</td>
  </tr>
  <tr>
    <td>43</td>
    <td>High speed craft (HSC), Hazardous category C</td>
  </tr>
  <tr>
    <td>44</td>
    <td>High speed craft (HSC), Hazardous category D</td>
  </tr>
  <tr>
    <td>45</td>
    <td>High speed craft (HSC), Reserved for future use</td>
  </tr>
  <tr>
    <td>46</td>
    <td>High speed craft (HSC), Reserved for future use</td>
  </tr>
  <tr>
    <td>47</td>
    <td>High speed craft (HSC), Reserved for future use</td>
  </tr>
  <tr>
    <td>48</td>
    <td>High speed craft (HSC), Reserved for future use</td>
  </tr>
  <tr>
    <td>49</td>
    <td>High speed craft (HSC), No additional information</td>
  </tr>
  <tr>
    <td>50</td>
    <td>Pilot Vessel</td>
  </tr>
  <tr>
    <td>51</td>
    <td>Search and Rescue vessel</td>
  </tr>
  <tr>
    <td>52</td>
    <td>Tug</td>
  </tr>
  <tr>
    <td>53</td>
    <td>Port Tender</td>
  </tr>
  <tr>
    <td>54</td>
    <td>Anti-pollution equipment</td>
  </tr>
  <tr>
    <td>55</td>
    <td>Law Enforcement</td>
  </tr>
  <tr>
    <td>56</td>
    <td>Spare - Local Vessel</td>
  </tr>
  <tr>
    <td>57</td>
    <td>Spare - Local Vessel</td>
  </tr>
  <tr>
    <td>58</td>
    <td>Medical Transport</td>
  </tr>
  <tr>
    <td>59</td>
    <td>Noncombatant ship according to RR Resolution No. 18</td>
  </tr>
  <tr>
    <td>60</td>
    <td>Passenger, all ships of this type</td>
  </tr>
  <tr>
    <td>61</td>
    <td>Passenger, Hazardous category A</td>
  </tr>
  <tr>
    <td>62</td>
    <td>Passenger, Hazardous category B</td>
  </tr>
  <tr>
    <td>63</td>
    <td>Passenger, Hazardous category C</td>
  </tr>
  <tr>
    <td>64</td>
    <td>Passenger, Hazardous category D</td>
  </tr>
  <tr>
    <td>65</td>
    <td>Passenger, Reserved for future use</td>
  </tr>
  <tr>
    <td>66</td>
    <td>Passenger, Reserved for future use</td>
  </tr>
  <tr>
    <td>67</td>
    <td>Passenger, Reserved for future use</td>
  </tr>
  <tr>
    <td>68</td>
    <td>Passenger, Reserved for future use</td>
  </tr>
  <tr>
    <td>69</td>
    <td>Passenger, No additional information</td>
  </tr>
  <tr>
    <td>70</td>
    <td>Cargo, all ships of this type</td>
  </tr>
  <tr>
    <td>71</td>
    <td>Cargo, Hazardous category A</td>
  </tr>
  <tr>
    <td>72</td>
    <td>Cargo, Hazardous category B</td>
  </tr>
  <tr>
    <td>73</td>
    <td>Cargo, Hazardous category C</td>
  </tr>
  <tr>
    <td>74</td>
    <td>Cargo, Hazardous category D</td>
  </tr>
  <tr>
    <td>75</td>
    <td>Cargo, Reserved for future use</td>
  </tr>
  <tr>
    <td>76</td>
    <td>Cargo, Reserved for future use</td>
  </tr>
  <tr>
    <td>77</td>
    <td>Cargo, Reserved for future use</td>
  </tr>
  <tr>
    <td>78</td>
    <td>Cargo, Reserved for future use</td>
  </tr>
  <tr>
    <td>79</td>
    <td>Cargo, No additional information</td>
  </tr>
  <tr>
    <td>80</td>
    <td>Tanker, all ships of this type</td>
  </tr>
  <tr>
    <td>81</td>
    <td>Tanker, Hazardous category A</td>
  </tr>
  <tr>
    <td>82</td>
    <td>Tanker, Hazardous category B</td>
  </tr>
  <tr>
    <td>83</td>
    <td>Tanker, Hazardous category C</td>
  </tr>
  <tr>
    <td>84</td>
    <td>Tanker, Hazardous category D</td>
  </tr>
  <tr>
    <td>85</td>
    <td>Tanker, Reserved for future use</td>
  </tr>
  <tr>
    <td>86</td>
    <td>Tanker, Reserved for future use</td>
  </tr>
  <tr>
    <td>87</td>
    <td>Tanker, Reserved for future use</td>
  </tr>
  <tr>
    <td>88</td>
    <td>Tanker, Reserved for future use</td>
  </tr>
  <tr>
    <td>89</td>
    <td>Tanker, No additional information</td>
  </tr>
  <tr>
    <td>90</td>
    <td>Other Type, all ships of this type</td>
  </tr>
  <tr>
    <td>91</td>
    <td>Other Type, Hazardous category A</td>
  </tr>
  <tr>
    <td>92</td>
    <td>Other Type, Hazardous category B</td>
  </tr>
  <tr>
    <td>93</td>
    <td>Other Type, Hazardous category C</td>
  </tr>
  <tr>
    <td>94</td>
    <td>Other Type, Hazardous category D</td>
  </tr>
  <tr>
    <td>95</td>
    <td>Other Type, Reserved for future use</td>
  </tr>
  <tr>
    <td>96</td>
    <td>Other Type, Reserved for future use</td>
  </tr>
  <tr>
    <td>97</td>
    <td>Other Type, Reserved for future use</td>
  </tr>
  <tr>
    <td>98</td>
    <td>Other Type, Reserved for future use</td>
  </tr>
  <tr>
    <td>99</td>
    <td>Other Type, no additional information</td>
  </tr>
</tbody>
</table>