# Network Time Protocol (NTP), RFC RFC 5905

Port 123

## ncat

<https://seriot.ch/projects/tiny_ntp_client.html>

```console
ubuntu@LAPTOP-JBell:~$ date -d@$((0x`printf c%47s|nc -uw1 ntp.metas.ch 123|xxd -s40 -l4 -p`-64#23GDW0))
Sat Oct 18 02:38:13 EDT 2025
```

```console
ubuntu@LAPTOP-JBell:~$ date -d@$((0x`printf c%47s|nc -uw1 ntp.nict.jp 123|xxd -s40 -l4 -p`-64#23GDW0))
Sat Oct 18 02:39:16 EDT 2025
```

## ntpdate

<https://www.ntp.org/documentation/4.2.8-series/ntpdate/>

```console
ubuntu@LAPTOP-JBell:~$ ntpdate -q pool.ntp.org
server 198.181.199.86, stratum 1, offset +0.686866, delay 0.05246
server 216.232.132.102, stratum 1, offset +0.702794, delay 0.08055
server 23.133.168.244, stratum 4, offset +0.708619, delay 0.05632
server 216.6.2.70, stratum 2, offset +0.723617, delay 0.03767
18 Oct 01:54:42 ntpdate[83681]: step time server 198.181.199.86 offset +0.686866 sec
```

```console
ubuntu@LAPTOP-JBell:~$ ntpdate -q tick.usno.navy.mil
server 192.5.41.40, stratum 1, offset +1.669070, delay 0.09024
18 Oct 02:27:48 ntpdate[92129]: step time server 192.5.41.40 offset +1.669070 sec
```

```console
ubuntu@LAPTOP-JBell:~$ ntpdate -q time.nrc.ca
server 132.246.11.227, stratum 2, offset +1.131365, delay 0.03700
server 132.246.11.229, stratum 2, offset +1.132102, delay 0.03690
server 132.246.11.237, stratum 2, offset +1.131960, delay 0.03650
server 132.246.11.238, stratum 2, offset +1.132422, delay 0.03534
18 Oct 02:45:11 ntpdate[96272]: step time server 132.246.11.238 offset +1.132422 sec
```

## ntpq

<https://www.ntp.org/documentation/4.2.8-series/ntpq/>

```console
ubuntu@LAPTOP-JBell:~$ ntpq -p
     remote           refid      st t when poll reach   delay   offset  jitter
==============================================================================
 0.ubuntu.pool.n .POOL.          16 p    -   64    0    0.000   +0.000   0.000
 1.ubuntu.pool.n .POOL.          16 p    -   64    0    0.000   +0.000   0.000
 2.ubuntu.pool.n .POOL.          16 p    -   64    0    0.000   +0.000   0.000
 3.ubuntu.pool.n .POOL.          16 p    -   64    0    0.000   +0.000   0.000
 ntp.ubuntu.com  .POOL.          16 p    -   64    0    0.000   +0.000   0.000
 muug.ca         132.163.97.1     2 u    4   64    3   26.111  +1186.8 480.811
 172-97-210-214. .GPS.            1 u    3   64    3    9.934  +1184.4 480.641
+ntp3.torix.ca   .PTP0.           1 u    6   64    3    4.294  +1184.4 483.347
 64.ip-54-39-23. 206.108.0.132    2 u    6   64    3   11.172  +1183.9 483.177
 zero.gotroot.ca 192.80.172.163   3 u    5   64    3   55.050  +1184.4 481.203
 ntp1.yyz.ca.hoj 69.180.17.124    2 u    5   64    3    4.273  +1184.3 481.340
*vps-yyz1.orlean 206.126.112.212  2 u    6   64    3    3.265  +1183.8 483.339
+drax.kayaks.hun 206.108.0.131    2 u    6   64    3   11.078  +1184.5 483.343
+linuxgeneration 70.51.80.145     2 u    6   64    3    3.291  +1184.8 483.367
 time.cloudflare 10.17.8.4        3 u    5   64    3    3.654  +1184.3 481.399
 hub.coreserv.ne 70.51.80.145     2 u    6   64    3    4.198  +1184.5 483.167
 167.160.187.12  167.160.187.179  3 u    3   64    3    3.676  +1183.7 480.698
 archer.fsck.ca  15.254.136.119   2 u   12   64    1   14.009  +1291.4   0.000
 23.133.168.245  162.159.200.1    4 u    6   64    3   31.095  +1181.5 483.216
 23.133.168.247  162.159.200.1    4 u    5   64    3   33.009  +1180.7 481.262
 23.133.168.244  162.159.200.123  4 u    4   64    3   30.932  +1179.9 480.883
```

```console
ubuntu@LAPTOP-JBell:~$ ntpq -c 'rv 0 clock'
clock=ec9dc60d.3aafe7be  Sat, Oct 18 2025  3:53:49.229
ubuntu@LAPTOP-JBell:~$ ntpq
ntpq> rv 0
associd=0 status=c018 leap_alarm, sync_unspec, 1 event, no_sys_peer,
version="ntpd 4.2.8p15@1.3728-o Wed Feb 16 17:13:02 UTC 2022 (1)",
processor="x86_64", system="Linux/6.6.87.2-microsoft-standard-WSL2",
leap=11, stratum=16, precision=-25, rootdelay=0.000, rootdisp=1.215,
refid=STEP, reftime=(no time),
clock=ec9dc61b.54821fad  Sat, Oct 18 2025  3:54:03.330, peer=0, tc=6,
mintc=3, offset=+0.000000, frequency=-37.708, sys_jitter=0.000030,
clk_jitter=0.000, clk_wander=117.489, tai=37, leapsec=201701010000,
expire=202512280000
```



## sntp

```console
ubuntu@LAPTOP-JBell:~$ sntp -K /dev/null time.apple.com
sntp 4.2.8p15@1.3728-o Wed Feb 16 17:13:02 UTC 2022 (1)
2025-10-18 02:53:22.082645 (+0500) +1.151036 +/- 0.767510 time.apple.com 17.253.2.37 s1 no-leap
```

```console
ubuntu@LAPTOP-JBell:~$ sntp -K /dev/null time.aws.com
sntp 4.2.8p15@1.3728-o Wed Feb 16 17:13:02 UTC 2022 (1)
2025-10-18 02:46:39.467061 (+0500) +1.15384 +/- 0.769407 time.aws.com 3.86.4.106 s4 no-leap
```

# DAYTIME Protocol, RFC 867

Port 13

## /dev/tcp/

<https://tldp.org/LDP/abs/html/devref1.html>

```console
ubuntu@LAPTOP-JBell:~$ cat </dev/tcp/time.nist.gov/13

60966 25-10-18 06:49:19 16 0 0 724.2 UTC(NIST) *
```

## ncat

```console
ubuntu@LAPTOP-JBell:~$ ncat time.nist.gov 13

60966 25-10-18 07:09:27 16 0 0 621.4 UTC(NIST) *
```

# TIME Protocol, RFC 868 Time Protocol

Port 37

<https://tf.nist.gov/tf-cgi/servers.cgi>

> We will continue to support the "TIME" protocol that uses tcp port 37 for the forseeable future. However, this protocol is very expensive in terms of network bandwidth,
> since it uses the complete tcp machinery to transmit only 32 bits of data. Users are *strongly* encouraged to upgrade to the network time protocol (NTP), which is both
> more accurate and more robust.

## rdate

```console
ubuntu@LAPTOP-JBell:~$ rdate -p time.nist.gov
Sat Oct 18 02:14:08 EDT 2025
```

# REST API

<https://worldtimeapi.org/pages/examples>

```console
ubuntu@LAPTOP-JBell:~$ curl -s "http://worldtimeapi.org/api/timezone/America/Toronto" | jq '.'
{
  "utc_offset": "-04:00",
  "timezone": "America/Toronto",
  "day_of_week": 6,
  "day_of_year": 291,
  "datetime": "2025-10-18T03:29:31.163051-04:00",
  "utc_datetime": "2025-10-18T07:29:31.163051+00:00",
  "unixtime": 1760772571,
  "raw_offset": -18000,
  "week_number": 42,
  "dst": true,
  "abbreviation": "EDT",
  "dst_offset": 3600,
  "dst_from": "2025-03-09T07:00:00+00:00",
  "dst_until": "2025-11-02T06:00:00+00:00",
  "client_ip": "70.55.4.185"
}
ubuntu@LAPTOP-JBell:~$ curl -s "http://worldtimeapi.org/api/timezone/America/Toronto" | jq '.datetime'
"2025-10-18T03:29:43.672238-04:00"
```
