---
layout: post
title: Introduction to APIs in Google
---

> APIs (Application Programming Interfaces) are software programs that give developers access to computing resources and data. Companies from many different fields offer publicly available APIs so that developers can integrate specialized tools, services, or libraries with their own applications and codebase.
>
> This lab will teach you about the architecture and basic functioning of APIs. This will be supplemented with hands-on practice, where you will configure and run Cloud Storage API methods in Google Cloud Shell. After taking this lab you will understand key principles of API communication, architecture, and authentication. You will also gain practical experience with APIs, which you can apply to future labs or projects.

> In this lab, you will learn about:
>
> - Google APIs
> - API architecture
> - HTTP protocol and methods
> - Endpoints
> - REST (Representational State Transfer) and RESTful APIs
> - JSON (JavaScript Object Notation)
> - API authentication services

> APIs that utilize the HTTP protocol use HTTP request methods (also known as "HTTP verbs") for transmitting client requests to servers. The most commonly used HTTP request methods are GET, POST, PUT, and DELETE.
>
> - The **GET** request method is used by a client to fetch data from a server. If the requested resource is found on the server, it will then be sent back to the client.
> - The **PUT** method replaces existing data or creates data if it does not exist. If you use PUT many times, it will have no effect — there will only be one copy of the dataset on the server.
> - The **POST** method is used primarily to create new resources. Using POST many times will add data in multiple places on the server. It is recommended to use PUT to update resources and POST to create new resources.
> - The **DELETE** method will remove data or resources specified by the client on a server.

> APIs use HTTP methods to interact with data or computing services hosted on a server. These methods are useless if there isn't a way to access specific resources with consistency. APIs utilize communication channels called endpoints so that clients can access the resources they need without complication or irregularity.

