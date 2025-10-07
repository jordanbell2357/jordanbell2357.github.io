---
layout: post
title: Python and TLS/SSL
topic: cli
---

We first remark that it is possible to use an unverified context, which is an SSL context that disables certificate verification.

[Python's urllib.request for HTTP Requests - Real Python](https://realpython.com/urllib-request/)

```python
import ssl
from urllib.request import urlopen

unverified_context = ssl._create_unverified_context()
urlopen("https://expired.badssl.com/", context=unverified_context)
```

We make a self signed certificate [openssl-req](https://docs.openssl.org/master/man1/openssl-req/).

```console
ubuntu@LAPTOP-JBell:~$ openssl req -x509 -newkey rsa:2048 -keyout key.pem -out req.pem
.......+......+...+....+......+..+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*............+.+...+.........+...+.....+...+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*........+.+..+.......+..+...+.+.....+.+...........+.............+............+..+.......+.....+...+.......+...+........+.......+.....................+............+.....+....+..............+.+.....+....+..+...+....+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
......+...+..........+..+....+....................+.+......+.................+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*.+..............+....+.....+.......+...........+.......+..+....+..+....+.........+.....+.......+..+...............+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*.+..........+......+..+...............+......+.+.....+....+.....+.......+..+.+.........+.....+.+......+......+...+.....+.......+...+......+.........+......+..................+..+.+..............+......+.............+.....+.+........+......+....+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Enter PEM pass phrase:
Verifying - Enter PEM pass phrase:
-----
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) [AU]:CA
State or Province Name (full name) [Some-State]:Ontario
Locality Name (eg, city) []:Toronto
Organization Name (eg, company) [Internet Widgits Pty Ltd]:jordanbell.info
Organizational Unit Name (eg, section) []:
Common Name (e.g. server FQDN or YOUR name) []:Jordan Bell
Email Address []:
```

In one terminal we run [openssl-s_server](https://docs.openssl.org/master/man1/openssl-s_server/)

```console
ubuntu@LAPTOP-JBell:~$ openssl s_server -accept 60100 -key key.pem -cert req.pem
Enter pass phrase for key.pem:
Using default temp DH parameters
ACCEPT
```

Then in another terminal we run [openssl-s_client](https://docs.openssl.org/master/man1/openssl-s_client/).
Using the option `-verifyCAfile req.pem`, we avoid the warning caused by the
server using a self-signed certificate.

```console
ubuntu@LAPTOP-JBell:~/real_python$ openssl s_client -verifyCAfile req.pem -connect 127.0.0.1:60100
CONNECTED(00000003)
Can't use SSL_get_servername
depth=0 C = CA, ST = Ontario, L = Toronto, O = jordanbell.info, CN = Jordan Bell
verify return:1
---
Certificate chain
 0 s:C = CA, ST = Ontario, L = Toronto, O = jordanbell.info, CN = Jordan Bell
   i:C = CA, ST = Ontario, L = Toronto, O = jordanbell.info, CN = Jordan Bell
   a:PKEY: rsaEncryption, 2048 (bit); sigalg: RSA-SHA256
   v:NotBefore: Oct  6 01:31:34 2025 GMT; NotAfter: Nov  5 01:31:34 2025 GMT
---
Server certificate
-----BEGIN CERTIFICATE-----
MIIDozCCAougAwIBAgIUNLFlOFPtYK1/56bRG7uB+LYAMFMwDQYJKoZIhvcNAQEL
BQAwYTELMAkGA1UEBhMCQ0ExEDAOBgNVBAgMB09udGFyaW8xEDAOBgNVBAcMB1Rv
cm9udG8xGDAWBgNVBAoMD2pvcmRhbmJlbGwuaW5mbzEUMBIGA1UEAwwLSm9yZGFu
IEJlbGwwHhcNMjUxMDA2MDEzMTM0WhcNMjUxMTA1MDEzMTM0WjBhMQswCQYDVQQG
EwJDQTEQMA4GA1UECAwHT250YXJpbzEQMA4GA1UEBwwHVG9yb250bzEYMBYGA1UE
CgwPam9yZGFuYmVsbC5pbmZvMRQwEgYDVQQDDAtKb3JkYW4gQmVsbDCCASIwDQYJ
KoZIhvcNAQEBBQADggEPADCCAQoCggEBAJd1DQTtfMJUX1IkdTJRKNO/Iju2ljrq
Y7zBBGnrVhy5dgND1ydaIMVIR/tAmz/GnNwk8BIx1SnfRtTxWUaZ5U3OwjhCRFVr
4t3apx8sW5qUcHKcVwurGMLDyoZrJRA1Cba+XUkTnZTqnMoOlXVF4g/1ewytTfNU
Qvo+cCXIIHT6mRu3pZZKKKur/BDW5/DRHeeHIyJHGWulmQcxm0xWJfZ5LY5/svHS
LQnfXK3HpBUmtyJzIfFZhpPa7xsJaiJWgNXOBUALGbh2gCOlIDC0lmK+2YXYqenv
JICHvdPajgL6JaCaFoUL9ykSOrWXOlcer2zPCppkbC37hVfZ1fgZ/AkCAwEAAaNT
MFEwHQYDVR0OBBYEFCH7NIMbDzq1HfCfPQd66iWmUVPTMB8GA1UdIwQYMBaAFCH7
NIMbDzq1HfCfPQd66iWmUVPTMA8GA1UdEwEB/wQFMAMBAf8wDQYJKoZIhvcNAQEL
BQADggEBAIJuQDpHBiHdoiHO6+jNxyRpehXC6KjYOy2ek3751W82anhcgoPDWyzJ
kKs6vSMdtKeo6hI/G/IyBi4A2OGNveDcQBj8cem3RSGKiTtrBTslTK1koEIF/klW
SEri1qSwTUq5ioLt6kOv/5GDYQtvCTHr/m7UuBDHXqzl8I20dVKY0bId3pXBPbRN
s2YT8FHSeEoj4sjiEEh15L9PEuvMXPE4sD8xl+K4xmhltZvQSphrOG9epPhW8ouy
mI3A/fkGXPTZo8ctTw4+2qb48CdU/tuDaPoDcXp47tbMHC7xFNzAbtydbSSpwkM0
6zVym5SSc9hOlC4Zihht4lFzQ7ThwOk=
-----END CERTIFICATE-----
subject=C = CA, ST = Ontario, L = Toronto, O = jordanbell.info, CN = Jordan Bell
issuer=C = CA, ST = Ontario, L = Toronto, O = jordanbell.info, CN = Jordan Bell
---
No client certificate CA names sent
Peer signing digest: SHA256
Peer signature type: RSA-PSS
Server Temp Key: X25519, 253 bits
---
SSL handshake has read 1491 bytes and written 373 bytes
Verification: OK
---
New, TLSv1.3, Cipher is TLS_AES_256_GCM_SHA384
Server public key is 2048 bit
Secure Renegotiation IS NOT supported
Compression: NONE
Expansion: NONE
No ALPN negotiated
Early data was not sent
Verify return code: 0 (ok)
---
---
Post-Handshake New Session Ticket arrived:
SSL-Session:
    Protocol  : TLSv1.3
    Cipher    : TLS_AES_256_GCM_SHA384
    Session-ID: 6785434F96B01E7B4B6BA7B81DB25F8F3B4BDAFFD7D1EC52923A692BBC9E30AE
    Session-ID-ctx:
    Resumption PSK: 08C7DEA3D642C7059EC87E68689337B7586810EE35D2C6D876FE7582383A93F4B0B278730D1CC8906AF55BB1FD3B674C
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 7200 (seconds)
    TLS session ticket:
    0000 - 91 93 9f f8 90 05 af 77-ff 5a 6a c5 c3 58 c9 47   .......w.Zj..X.G
    0010 - 70 fb d2 cf 38 1d b3 f9-1e 2a ce 49 05 8c 2e 78   p...8....*.I...x
    0020 - a5 20 8d 44 eb e1 d6 6c-5e bc 61 44 4e a0 05 df   . .D...l^.aDN...
    0030 - 51 af 0d 7c 43 b6 3d 14-b9 85 93 3b 8c 4b a6 43   Q..|C.=....;.K.C
    0040 - ef 0a e5 6e 5a 29 ad f8-85 3d 8c 16 3e 17 71 43   ...nZ)...=..>.qC
    0050 - a0 88 5e bc e5 c6 5f 2e-ba 72 a8 62 d7 08 5b 22   ..^..._..r.b..["
    0060 - 29 16 ec 65 e9 01 67 f3-cc b9 c7 f6 9b 8d 0a 2e   )..e..g.........
    0070 - a4 8f b9 29 88 b8 bb 75-15 ee 0d 5f b3 80 c2 cc   ...)...u..._....
    0080 - 51 aa ee d2 67 3c 76 cf-1b 95 5f 66 ef ab 24 de   Q...g<v..._f..$.
    0090 - 6a 61 ee 93 3d 36 37 02-3d a1 59 06 b3 75 61 48   ja..=67.=.Y..uaH
    00a0 - 0c b7 3d 30 d8 ee ae a7-a8 03 89 e2 05 02 00 cc   ..=0............
    00b0 - e3 a1 72 dc cf 23 dd ac-f5 a8 5c 96 a2 54 66 ad   ..r..#....\..Tf.
    00c0 - ae 62 68 eb 08 03 3e 68-72 e1 bf 81 91 8a e5 03   .bh...>hr.......

    Start Time: 1759807449
    Timeout   : 7200 (sec)
    Verify return code: 0 (ok)
    Extended master secret: no
    Max Early Data: 0
---
read R BLOCK
---
Post-Handshake New Session Ticket arrived:
SSL-Session:
    Protocol  : TLSv1.3
    Cipher    : TLS_AES_256_GCM_SHA384
    Session-ID: E3204C42485E38CF56B5CC2B3577417FB3013E46DD534B633992B338CCD6BE4D
    Session-ID-ctx:
    Resumption PSK: 2BFB367CCBD0F6F88603E60ADD8EEC1FF960BB78B47BC5E5D96B558542B32ACA9819D6701E0FC2EFA807DDC96A24A535
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 7200 (seconds)
    TLS session ticket:
    0000 - 91 93 9f f8 90 05 af 77-ff 5a 6a c5 c3 58 c9 47   .......w.Zj..X.G
    0010 - 25 94 19 2a 6b 20 0d 37-81 63 d5 cc 57 f3 86 08   %..*k .7.c..W...
    0020 - 58 04 4f d4 fe 7b e9 a3-16 f7 0b 4a 2e 75 c2 e9   X.O..{.....J.u..
    0030 - 98 b6 b1 b6 56 3a 7c a7-8b 4e a2 cd e1 97 3f 73   ....V:|..N....?s
    0040 - 94 e9 de 2f b9 39 b6 e3-51 a6 18 16 2b 7c b2 6a   .../.9..Q...+|.j
    0050 - 98 0a b9 9a 02 fd cc 93-8b 51 f0 c1 f5 d8 1b 3e   .........Q.....>
    0060 - 15 77 27 31 f8 f3 58 4d-f7 61 aa 4c 6a cb 3b 11   .w'1..XM.a.Lj.;.
    0070 - 8b 35 16 13 c7 7a 23 26-94 01 6c a1 2a c2 74 7c   .5...z#&..l.*.t|
    0080 - 04 cc e4 1a 94 6b cc 15-e4 78 e2 4f 04 4e 10 d4   .....k...x.O.N..
    0090 - fc ac 69 df 56 69 19 6d-90 56 2a d1 3e ef 92 f1   ..i.Vi.m.V*.>...
    00a0 - 58 76 99 8e 60 f2 8b 68-a3 c7 e9 bc 49 dd a7 32   Xv..`..h....I..2
    00b0 - e5 45 f3 ff e9 6e 82 fa-08 b3 91 b1 b1 31 cd f3   .E...n.......1..
    00c0 - 06 bb 4e dc 5d 01 b3 5d-b7 63 11 9a 88 6a 9f 8c   ..N.]..].c...j..

    Start Time: 1759807449
    Timeout   : 7200 (sec)
    Verify return code: 0 (ok)
    Extended master secret: no
    Max Early Data: 0
---
read R BLOCK
```

cf. <https://www.liquidweb.com/blog/how-to-test-ssl-connection-using-openssl/>

[SSL - Ncat Users' Guide](https://nmap.org/ncat/guide/ncat-ssl.html)

```console
ubuntu@LAPTOP-JBell:~$ ncat -C --ssl httpbin.org 443
GET / HTTP/1.1
Host: httpbin.org
Content-Type: text/html

HTTP/1.1 200 OK
Date: Mon, 06 Oct 2025 01:56:27 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 9593
Connection: keep-alive
Server: gunicorn/19.9.0
Access-Control-Allow-Origin: *
Access-Control-Allow-Credentials: true

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>httpbin.org</title>
...
```
