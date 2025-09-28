---
layout: post
title: Python smtplib, email and b64 libraries
topic: cli
---

We modify <https://realpython.com/python-send-email/>.

We need to use a local SMTP server because the `smtpd` library was removed in Python 3.12.

```bash
sudo apt install mailutils
```

First we use plain text.

```python3
import smtplib

port = 25
smtp_server = "localhost"
sender_email = "ubuntu@localhost"
receiver_email = "ubuntu@localhost"
message = """\
Subject: The subject line
The message body.

More of the message body."""

with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.ehlo()  # Can be omitted
    server.sendmail(sender_email, receiver_email, message)
```

Reading the email with `mail`:

```
Return-Path: <ubuntu@localhost>
X-Original-To: ubuntu@localhost
Delivered-To: ubuntu@localhost
Received: from LAPTOP-JBell.localdomain (localhost [127.0.0.1])
        by LAPTOP-JBell.localdomain (Postfix) with ESMTP id 66E72233EC
        for <ubuntu@localhost>; Sun, 28 Sep 2025 00:35:55 -0400 (EDT)
Subject: The subject line
Message-Id: <20250928043555.66E72233EC@LAPTOP-JBell.localdomain>
Date: Sun, 28 Sep 2025 00:35:55 -0400 (EDT)
From: ubuntu@localhost
X-UID: 6
Status: O

The message body.

More of the message body.
```

Using MIME:

```python3
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

port = 25
smtp_server = "localhost"
sender_email = "ubuntu@localhost"
receiver_email = "ubuntu@localhost"

message = MIMEMultipart("alternative")
message["Subject"] = "MIME test"
message["From"] = sender_email
message["To"] = receiver_email

# Create the plain-text and HTML version of your message
text = """\
Hi,
How are you?
Real Python has many great tutorials:
www.realpython.com"""

html = """\
<html>
  <body>
    <p>Hi,<br>
       How are you?<br>
       <a href="http://www.realpython.com">Real Python</a> 
       has many great tutorials.
    </p>
  </body>
</html>
"""

# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)
message.attach(part2)

# Send email
with smtplib.SMTP(smtp_server, port) as server:
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )
```

Viewing email using [Alpine](https://alpineapp.email/) (`sudo apt install alpine`):

<img width="945" height="465" alt="image" src="https://github.com/user-attachments/assets/c7fbdf7a-75a8-4c66-855a-4c7d1dcfd45c" />

Sending an email with an attachment:

```python3
import email
import smtplib

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

port = 25
smtp_server = "localhost"
sender_email = "ubuntu@localhost"
receiver_email = "ubuntu@localhost"
subject = "An email with attachment from Python"
body = "This is an email with attachment sent from Python"

# Create a multipart message and set headers
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message["Bcc"] = receiver_email  # Recommended for mass emails

# Add body to email
message.attach(MIMEText(body, "plain"))

filename = "document.pdf"  # In same directory as script

# Open PDF file in binary mode
with open(filename, "rb") as attachment:
    # Add file as application/octet-stream
    # Email client can usually download this automatically as attachment
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

# Encode file in ASCII characters to send by email    
encoders.encode_base64(part)

# Add header as key/value pair to attachment part
part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)

# Add attachment to message and convert message to string
message.attach(part)
text = message.as_string()

# Send email
with smtplib.SMTP(smtp_server, port) as server:
    server.sendmail(sender_email, receiver_email, text)
```

Viewing the email in Alpine:

<img width="933" height="201" alt="image" src="https://github.com/user-attachments/assets/6a631181-6507-4148-a3ba-edacb7086800" />

And an embedded image using `b64`. (See <https://stackoverflow.com/questions/57829797/how-to-embed-a-base64-image-into-html-email-via-python-3-5>)

```python3
import smtplib
import base64
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

port = 25
smtp_server = "localhost"
sender_email = "ubuntu@localhost"
receiver_email = "ubuntu@localhost"

data = open('image.png', 'rb').read() # read bytes from file
data_base64 = base64.b64encode(data)  # encode to base64 (bytes)
data_base64 = data_base64.decode()    # convert bytes to string

message = MIMEMultipart("alternative")
message["Subject"] = "Embedded image test"
message["From"] = sender_email
message["To"] = receiver_email

# Create the plain-text and HTML version of your message
text = """\
Hi,
How are you?
Real Python has many great tutorials:
www.realpython.com"""

html = f"""\
<html>
  <body>
    <p>Image test.</p>
    <p><img src="data:image/jpeg;base64,{data_base64}"></p>
  </body>
</html>
"""

# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)
message.attach(part2)

# Send email
with smtplib.SMTP(smtp_server, port) as server:
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )
```

The body of this email is the following HTML:

```html
<html>
  <body>
    <p>Image test.</p>
    <p><img src="data:image/jpeg;base64,iVBOR...SuQmCC"></p>
  </body>
</html>
```

which renders as

<img width="661" height="678" alt="image" src="https://github.com/user-attachments/assets/a4843cfe-f6ed-4097-be88-c482e107dcc8" />

