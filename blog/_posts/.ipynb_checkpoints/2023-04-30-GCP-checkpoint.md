---
layout: post
title: GCP
---

[Discover object storage with the gsutil tool](https://cloud.google.com/storage/docs/discover-object-storage-gsutil)

We write out the steps for June 22, 2022.

```bash
curl -O https://coast.noaa.gov/htdata/CMSP/AISDataHandler/2022/AIS_2022_06_22.zip
unzip AIS_2022_06_22.zip
gsutil cp AIS_2022_06_22.csv gs://jordanbell2357marinecadastre/
rm AIS_2022_06_22.zip
rm AIS_2022_06_22.csv
```

