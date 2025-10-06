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

Then in another terminal we run [openssl-s_client](https://docs.openssl.org/master/man1/openssl-s_client/)

```console
ubuntu@LAPTOP-JBell:~$ openssl s_client -connect 127.0.0.1:60100
CONNECTED(00000003)

Can't use SSL_get_servername
depth=0 C = CA, ST = Ontario, L = Toronto, O = jordanbell.info, CN = Jordan Bell
verify error:num=18:self-signed certificate
verify return:1
depth=0 C = CA, ST = Ontario, L = Toronto, O = jordanbell.info, CN = Jordan Bell
verify return:1
---
Certificate chain
 0 s:C = CA, ST = Ontario, L = Toronto, O = jordanbell.info, CN = Jordan Bell
   i:C = CA, ST = Ontario, L = Toronto, O = jordanbell.info, CN = Jordan Bell
   a:PKEY: rsaEncryption, 2048 (bit); sigalg: RSA-SHA256
   v:NotBefore: Oct  6 01:31:34 2025 GMT; NotAfter: Nov  5 01:31:34 2025 GMT
---
...
---
read R BLOCK
```

Using the option `-verifyCAfile req.pem`, we avoid the error/warning caused by the
server using a self-signed certificate.

```console
ubuntu@LAPTOP-JBell:~$ openssl s_client -verifyCAfile req.pem -connect 127.0.0.1:60100
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

