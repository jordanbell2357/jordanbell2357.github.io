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
cat Google-3600A | tr -d ['\[','\]'] | tr '=' ' ' | awk -F " " '{ printf("%d, %d, %s, %.2f\n", NR, $8, $1, $12) }' > Google_A.csv
```

```bash
cat GTT-3600A | tr -d ['\[','\]'] | tr '=' ' ' | awk -F " " '{ printf("%d, %d, %s, %.2f\n", NR, $8, $1, $12) }' > GTT_A.csv
```

```bash
cat Tata-3600A | tr -d ['\[','\]'] | tr '=' ' ' | awk -F " " '{ printf("%d, %d, %s, %.2f\n", NR, $8, $1, $12) }' > Tata_A.csv
```

```bash
cat Verizon-3600A | tr -d ['\[','\]'] | tr '=' ' ' | awk -F " " '{ printf("%d, %d, %s, %.2f\n", NR, $8, $1, $12) }' > Verizon_A.csv
```

A, B, C for each


