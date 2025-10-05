---
layout: post
title: HTTP messages
topic: cli
---

[Sending a client request | MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Session#sending_a_client_request)

> Once the connection is established, the user-agent can send the request (a user-agent is typically a web browser, but can be anything else, a crawler, for example). A client request consists of text directives, separated by CRLF (carriage return, followed by line feed), divided into three blocks:
>
> 1. The first line contains a request method followed by its parameters:
> - the path of the document, as an absolute URL without the protocol or domain name
> - the HTTP protocol version
> 2. Subsequent lines represent an HTTP header, giving the server information about what type of data is appropriate (for example, what language, what MIME types), or other data altering its behavior (for example, not sending an answer if it is already cached). These HTTP headers form a block which ends with an empty line.
> 3. The final block is an optional data block, which may contain further data mainly used by the POST method.

[Structure of a server response](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Session#structure_of_a_server_response)

> After the connected agent has sent its request, the web server processes it, and ultimately returns a response. Similar to a client request, a server response is formed of text directives, separated by CRLF, though divided into three blocks:
>
> 1. The first line, the status line, consists of an acknowledgment of the HTTP version used, followed by a response status code (and its brief meaning in human-readable text).
> 2. Subsequent lines represent specific HTTP headers, giving the client information about the data sent (for example, type, data size, compression algorithm used, hints about caching). Similarly to the block of HTTP headers for a client request, these HTTP headers form a block ending with an empty line.
> 3. The final block is a data block, which contains the optional data.

[HTTP Messages | MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Messages)

> HTTP messages are the mechanism used to exchange data between a server and a client in the HTTP protocol. There are two types of messages:
> requests sent by the client to trigger an action on the server, and responses, the answer that the server sends in response to a request.

> Both requests and responses share a similar structure:
>
> 1. A start-line is a single line that describes the HTTP version along with the request method or the outcome of the request.
> 2. An optional set of HTTP headers containing metadata that describes the message. For example, a request for a resource might include the allowed formats of that resource, while the
> response might include headers to indicate the actual format returned.
> 4. An empty line indicating the metadata of the message is complete.
> 5. An optional body containing data associated with the message. This might be POST data to send to the server in a request, or some resource returned to the client in a response.
> Whether a message contains a body or not is determined by the start-line and HTTP headers.

[How to make a webserver with netcat (nc)](https://jameshfisher.com/2018/12/31/how-to-make-a-webserver-with-netcat-nc/)

```console
ubuntu@LAPTOP-JBell:~$ printf "GET / HTTP/1.1\r\nHost: developer.mozilla.org\r\n\r\n" | nc developer.mozilla.org 80
HTTP/1.1 301 Moved Permanently
Cache-Control: private
Location: https://developer.mozilla.org:443/
Content-Length: 0
Date: Sun, 05 Oct 2025 08:01:48 GMT
Content-Type: text/html; charset=UTF-8
```

```console
ubuntu@LAPTOP-JBell:~$ netcat developer.mozilla.org 80
GET /en-US/docs/Web/HTTP/Guides/Messages HTTP/1.1

HTTP/1.1 301 Moved Permanently
Cache-Control: private
Location: https://developer.mozilla.org:443/en-US/docs/Web/HTTP/Guides/Messages
Content-Length: 0
Date: Sun, 05 Oct 2025 14:47:29 GMT
Content-Type: text/html; charset=UTF-8
```


