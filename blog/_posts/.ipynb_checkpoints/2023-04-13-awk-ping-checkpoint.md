---
layout: post
title: Using awk with ping
---

```bash
ping -D -c 3600 -i 1 google.com.com > Google-3600A
```

Manually delete first line from `Google-3600A`.

```bash
head -n 5 Google-3600A
```

```
[1672984648.605701] 64 bytes from yyz12s07-in-f14.1e100.net (142.251.32.78): icmp_seq=1 ttl=114 time=4.36 ms
[1672984649.607109] 64 bytes from yyz12s07-in-f14.1e100.net (142.251.32.78): icmp_seq=2 ttl=114 time=3.78 ms
[1672984650.608478] 64 bytes from yyz12s07-in-f14.1e100.net (142.251.32.78): icmp_seq=3 ttl=114 time=3.38 ms
[1672984651.611088] 64 bytes from yyz12s07-in-f14.1e100.net (142.251.32.78): icmp_seq=4 ttl=114 time=4.49 ms
[1672984652.611526] 64 bytes from yyz12s07-in-f14.1e100.net (142.251.32.78): icmp_seq=5 ttl=114 time=4.21 ms
```

```bash
awk '{ gsub(/[|]/,""); split($(NF-1), lt, "="); printf("%s, %.2f\n", $1, lt[2]); } ' Google-3600A > Google_A.dat
```

```bash
head -n 5 Google_A.dat
```

Unix Timestamp, Ping Time (ms)

```
[1672984648.605701], 4.36
[1672984649.607109], 3.78
[1672984650.608478], 3.38
[1672984651.611088], 4.49
[1672984652.611526], 4.21
```


<https://www.gnu.org/software/gawk/manual/html_node/Time-Functions.html>

<https://awk.js.org/>