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

<p><img src="data:image/jpeg;base64,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"></p>
