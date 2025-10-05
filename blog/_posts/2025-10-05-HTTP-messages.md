---
layout: post
title: HTTP messages
topic: cli
---

[HTTP messages | MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Messages)

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

[HTTP - The Hard Way with Netcat by Arpit Bhayani](https://arpitbhayani.me/blogs/making-http-requests-using-netcat/)

[How to make a webserver with netcat (nc)](https://jameshfisher.com/2018/12/31/how-to-make-a-webserver-with-netcat-nc/)
