---
layout: post
title: Python https server
topic: cli
---

<https://piware.de/2011/01/creating-an-https-server-in-python/>

```python
from http.server import HTTPServer, SimpleHTTPRequestHandler
import ssl

HOST_NAME = "localhost"
PORT = 4443

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile='req.pem', keyfile='key.pem')
context.check_hostname = False

with HTTPServer((HOST_NAME, PORT), SimpleHTTPRequestHandler) as httpd:
    httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
    httpd.serve_forever()
```


<https://www.digitalocean.com/community/tutorials/python-simplehttpserver-http-server>

```python
import http.server
import socketserver
import ssl

PORT = 55000
HANDLER = http.server.SimpleHTTPRequestHandler

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile='req.pem', keyfile='key.pem')
context.check_hostname = False

with socketserver.TCPServer(("", PORT), HANDLER) as httpd:
    httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
    
    print(f"Serving securely on https://localhost:{PORT}")
    # Start the server
    httpd.serve_forever()
```
