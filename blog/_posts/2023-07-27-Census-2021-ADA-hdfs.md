---
layout: post
title: Ingesting Canada Census 2021 ADA level data into hdfs
---

<https://www12.statcan.gc.ca/census-recensement/2021/dp-pd/prof/details/download-telecharger/comp/GetFile.cfm?Lang=E&FILETYPE=CSV&GEONO=012>

```bash
curl -o 98-401-X2021012_eng_CSV.zip \
https://www12.statcan.gc.ca/census-recensement/2021/dp-pd/prof/details/download-telecharger/comp/GetFile.cfm?Lang=E&FILETYPE=CSV&GEONO=012
unzip 98-401-X2021012_eng_CSV.zip
hdfs dfs -mkdir /user/hive/warehouse/census2021.db
hdfs dfs -mkdir /user/hive/warehouse/census2021.db/ada
# hdfs dfs -mkdir -p /user/hive/warehouse/census2021.db/ada
hdfs dfs -put 98-401-X2021012_English_CSV_data.csv /user/hive/warehouse/census2021.db/ada/
```
