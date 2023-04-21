---
layout: post
title: BarentsWatch AIS API and curl
---


https://www.barentswatch.no/en/articles/open-data-via-barentswatch/

https://developer.barentswatch.no/docs/appreg/

https://www.barentswatch.no/minside/

https://live.ais.barentswatch.no/index.html

https://www.confluent.io/blog/streaming-etl-and-analytics-for-real-time-location-tracking/

https://www.confluent.io/blog/streaming-data-with-confluent-and-ksqldb-for-new-use-cases-with-ais/

https://gpsd.gitlab.io/gpsd/AIVDM.html#_ais_payload_interpretation

```bash
curl -X POST --header "Content-Type: application/x-www-form-urlencoded" \
-d "client_id=$client_id&scope=ais&client_secret=$client_secret&grant_type=client_credentials" \
https://id.barentswatch.no/connect/token > token.json
```

```bash
access_token=$(jq -r '.access_token' token.json)
```

```bash
echo $access_token
```

```
eyJhbGciOiJSUzI1NiIsImtpZCI6IjBCM0I1NEUyRkQ5OUZCQkY5NzVERDMxNDBDREQ4OEI1QzA5RkFDRjNSUzI1NiIsIng1dCI6IkN6dFU0djJaLTctWFhkTVVETjJJdGNDZnJQTSIsInR5cCI6ImF0K2p3dCJ9.eyJpc3MiOiJodHRwczovL2lkLmJhcmVudHN3YXRjaC5ubyIsIm5iZiI6MTY4MjAzNTU2OCwiaWF0IjoxNjgyMDM1NTY4LCJleHAiOjE2ODIwMzkxNjgsImF1ZCI6ImFpcyIsInNjb3BlIjpbImFpcyJdLCJjbGllbnRfaWQiOiJqb3JkYW4uYmVsbEBnbWFpbC5jb206am9yZGFuYmVsbDIzNTcifQ.hLX6xs3-r0b5dK0Lkxtg8wK4_UfOI5JUsukH6mnWx7EetecniYAEbQr5q2eLJtbCKqPF7Az7M-Y0MAh9Bwv0XB6KbA66sPyFTnniGj_uRLOoMoTWUZVsDIC1iuF0HFGTLptU9N7mJU_0bcLlsDA1soDSnjrMD-Gq9UetDkTQ2yFhnOtv5VbTWQcaimelglIJS5CPhQVcfQS6BS0vlCrsgyKDm1ook7-FpCbAQlmT9UiG0HLGBUYPOfxYWktFfpBzoIPc2vkrR-UdVSE6Xac_tV-ortxedTf4lp3cOIB_ikZ9mdbH_EzPZcxGcsbLQatfllc96GUXkITJyHh7dRmwrc6cFhMasmxPb0Rn7kkzf1S2Y8sjKO092SOUYSgjCBpUQIUg0n1UyngyZBiTEnKFPkMGr2UWmKOeFqMZpyeCCO1Q9hoZODKTt0UoXhdZUYbB5wMfilyGBvGEnYiqTcTfsiq66HpG33dfVfZI-8TilVwd3wXvLQvaakFhrDuQk4nCBtUsZW-5oPW5O9iScXbduL9GZIt2Zts8FQSX05is73bBjfy37Gz-8U2MmhJFJiEL5azf-aMf92ql54o3h2ZoF6GMXZOsIAB2WvE6cWaFG9flCw2Dz_SwuT3NXolIPH0NKOqsZ_Hv0YkZUKfMcrvevvttUDQW2vWYr0M-AeKfPzI
```

```
curl --location --request GET 'https://live.ais.barentswatch.no/v1/combined?modelType=Full&modelFormat=Geojson' \
--header "Authorization: Bearer $access_token" --max-time 60 > 2023-04-20_A.geojson
```