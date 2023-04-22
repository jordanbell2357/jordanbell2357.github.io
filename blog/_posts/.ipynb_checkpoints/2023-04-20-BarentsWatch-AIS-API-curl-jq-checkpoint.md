---
layout: post
title: BarentsWatch AIS API using curl and jq
---

[Application registration and authentication](https://developer.barentswatch.no/docs/appreg/)

[My page \| BarentsWatch](https://www.barentswatch.no/minside/)

[BarentsWatch AIS Live OpenAPI Documentation](https://live.ais.barentswatch.no/index.html)

# shipType

[Type of ship/cargo \| BarentsWatch Developer](https://developer.barentswatch.no/docs/AIS/aisshiptype)

# API token

```bash
client_id= #client_id
client_secret= #client_secret
```

```bash
curl -X POST --header "Content-Type: application/x-www-form-urlencoded" \
--data "client_id=$client_id&scope=ais&client_secret=$client_secret&grant_type=client_credentials" \
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

### April 20, 2023

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

### April 21, 2023

```bash
curl --location --request GET 'https://live.ais.barentswatch.no/v1/combined' \
--header "Authorization: Bearer $access_token" --max-time 600 > AIS_2023_04_21_lines.json
```

```bash
jq --slurp '.' AIS_2023_04_21_lines.json > AIS_2023_04_21.json
```

```bash
jq '.[0]' AIS_2023_04_21.json
```

```json
{
  "courseOverGround": 324,
  "latitude": 65.140352,
  "longitude": 7.13467,
  "name": "STRIL POSEIDON",
  "rateOfTurn": 0,
  "shipType": 51,
  "speedOverGround": 0.3,
  "trueHeading": 285,
  "mmsi": 258117000,
  "msgtime": "2023-04-21T22:29:52.6695296+00:00"
}
```

### April 22, 2023

```bash
curl --location --request GET 'https://live.ais.barentswatch.no/v1/combined' \
--header "Authorization: Bearer $access_token" --max-time 600 > AIS_2023_04_22_lines.json
```

```bash
jq --slurp '.' AIS_2023_04_22_lines.json > AIS_2023_04_22.json
```

```bash
jq '.[0]' AIS_2023_04_22.json
```

```json
{
  "courseOverGround": 11.4,
  "latitude": 63.797973,
  "longitude": 11.167988,
  "name": "YTTEROEY",
  "rateOfTurn": 0,
  "shipType": 90,
  "speedOverGround": 0,
  "trueHeading": 201,
  "mmsi": 258046000,
  "msgtime": "2023-04-22T16:35:35+00:00"
}
```

## live.ais.barentswatch.no/v1/latest/combined

### April 20, 2023

All latest positions:

```bash
curl --location --request GET 'https://live.ais.barentswatch.no/v1/latest/combined' \
--header "Authorization: Bearer $access_token" > latest_2023-04-20-UTC-01-38.json
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

### April 21, 2023

All latest positions:

```bash
curl --location --request GET 'https://live.ais.barentswatch.no/v1/latest/combined' \
--header "Authorization: Bearer $access_token" > latest_2023-04-21-UTC-11-25.json
```

```bash
jq '.[0]' latest_2023-04-21-UTC-11-25.json
```

```json
{
  "courseOverGround": 269.4,
  "latitude": 63.431932,
  "longitude": 10.375452,
  "name": "RESCUE UNE AMUNDSEN",
  "rateOfTurn": 0,
  "shipType": 51,
  "speedOverGround": 0,
  "trueHeading": 3,
  "mmsi": 257918900,
  "msgtime": "2023-04-21T23:26:01+00:00"
}
```

### April 22, 2023

All latest positions:

```bash
curl --location --request GET 'https://live.ais.barentswatch.no/v1/latest/combined' --header "Authorization: Bearer $access_token" > latest_2023-04-22-UTC-16-33.json
```

```bash
jq '.[0]' latest_2023-04-22-UTC-16-33.json
```

```json
{
  "courseOverGround": 251.9,
  "latitude": 63.431933,
  "longitude": 10.375468,
  "name": "RESCUE UNE AMUNDSEN",
  "rateOfTurn": 0,
  "shipType": 51,
  "speedOverGround": 0,
  "trueHeading": 7,
  "mmsi": 257918900,
  "msgtime": "2023-04-22T16:33:40+00:00"
}
```

# nc

We follow [Streaming ETL and Analytics on Confluent with Maritime AIS Data. Robin Moffatt. June 1, 2021](https://www.confluent.io/blog/streaming-etl-and-analytics-for-real-time-location-tracking/)

```bash
nc 153.44.253.27 5631
```

[gpsd](https://gpsd.gitlab.io/gpsd/AIVDM.html#_ais_payload_interpretation)