---
layout: post
title: RANDOM.ORG API
topic: python
---

<https://api.random.org/>

<https://api.random.org/json-rpc/4/basic>

```python3
from urllib.request import urlopen, Request
import json
import random

API_KEY = "<API Key>"
BLOB_BYTE_SIZE = 64
BLOB_COUNT = 5
BLOB_FORMAT = "hex"

request_id = random.randint(1, 65000)

base_url = "https://api.random.org/json-rpc/4/invoke"

payload_dict =  {
    "jsonrpc": "2.0",
    "method": "generateBlobs",
    "params": {
        "apiKey": API_KEY,
        "n": BLOB_COUNT,
        "size": BLOB_BYTE_SIZE,
        "format": BLOB_FORMAT
    },
    "id": request_id
    }

headers_dict = { "Content-Type": "application/json" }

payload_bytes = json.dumps(payload_dict).encode("utf-8")

request = Request(base_url, headers=headers_dict, data=payload_bytes)

with urlopen(request, timeout=10) as response:
    response_bytes = response.read()
    response_dict = json.loads(response_bytes)
    assert request_id == response_dict["id"], "Response id does not match request id"
    result_dict = response_dict["result"]
    random_bytes_list = result_dict["random"]["data"]
    for random_bytes in random_bytes_list:
        print(random_bytes)
```

```
(python_random) ubuntu@LAPTOP-JBell:~/python_random$ python random_bytes.py 
5e1ac4df32bca557
730f67a5993d6fac
6af85c61c68a2032
ac391dbc8750313b
2a870d1458e89531
```
