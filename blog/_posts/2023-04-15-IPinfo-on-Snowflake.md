---
layout: post
title: IPinfo on Snowflake and using API token with curl
---

[IPinfo Free IP Geolocation Sample](https://app.snowflake.com/marketplace/listing/GZSTZ3VDMEH/ipinfo-ipinfo-free-ip-geolocation-sample?available=available)

![IPinfo Free IP Geolocation Sample](/images/IPinfo/IPinfo-IPinfo-Free-IP-Geolocation-Sample.png)

> Our IP geolocation data provides a response that includes every IP’s latitude and longitude coordinates, region, country, postal/ZIP code, and city. Using our IP address geolocation data, customers can resolve their web traffic to meaningful locations as specific as a street address. IPinfo builds and maintains its own proprietary IP geolocation database, which can be used to generate various forms of geographic information for your IP traffic.
>
> IPinfo Snowflake Documentation: https://ipinfo.io/developers/integrations#snowflake
>
> Included Cities and Regions:
>
> This demo database, designed for Snowflake exploration and learning purposes, provides the complete IP address information for the following cities:
>
> - Denver, Colorado, US
> - Kenosha, Wisconsin, US
> - Sheboygan, Wisconsin, US
> - Gdańsk, Pomerania, PL
> - Warsaw, Mazovia, PL
> - Puducherry, Puducherry, IN
> - Madrid, Madrid, ES
> - Funafuti, Funafuti, TV
> - Nairobi, Nairobi, KE
> - Shanghai, Shanghai, CN

Shanghai Shipping Exchange <samp>en.sse.net.cn</samp>

```bash
host en.sse.net.cn
```

```
en.sse.net.cn has address 117.184.142.41
```

Snowflake: IPinfo Free IP Geolocation Sample - Usage Example

![IPinfo Free IP Geolocation Sample - Usage Example](/images/IPinfo/IPinfo-Free-IP-Geolocation-Sample-Usage-Example-Snowflake.png)

```sql
SELECT CITY, COUNTRY, LAT, LNG
FROM IPINFO_FREE_IP_GEOLOCATION_SAMPLE.demo.location
WHERE IPINFO_FREE_IP_GEOLOCATION_SAMPLE.public.TO_INT('117.184.142.41') BETWEEN start_ip_int AND end_ip_int;
```

```
CITY,COUNTRY,LAT,LNG
Shanghai,CN,31.22222,121.45806
```

```bash
host google.com
```

```
google.com has address 142.251.41.46
```

Snowflake: IPinfo Free IP Geolocation Sample - Usage Example

```sql
SELECT *
FROM demo.location
WHERE TO_INT('142.251.41.46') BETWEEN start_ip_int AND end_ip_int;
```

<samp>Query produced no results</samp>

We use an API token for [IPinfo.io](https://ipinfo.io/).

Denoting by `${token}` the value of the variable `token`,

```bash
curl "ipinfo.io/142.251.41.46?token=${token}"
```

```json
{
  "ip": "142.251.41.46",
  "hostname": "yyz12s08-in-f14.1e100.net",
  "city": "Toronto",
  "region": "Ontario",
  "country": "CA",
  "loc": "43.7001,-79.4163",
  "org": "AS15169 Google LLC",
  "postal": "M5A",
  "timezone": "America/Toronto"
}
```

```bash
host pku.edu.cn
```

```
pku.edu.cn has address 162.105.131.160
```

```bash
curl "ipinfo.io/162.105.131.160?token=${token}"
```

```json
{
  "ip": "162.105.131.160",
  "city": "Beijing",
  "region": "Beijing",
  "country": "CN",
  "loc": "39.9075,116.3972",
  "org": "AS24349 CERNET2 IX at Peking University",
  "timezone": "Asia/Shanghai"
}
```