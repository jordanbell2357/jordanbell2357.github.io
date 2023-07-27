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

```bash
hdfs dfs -cat /user/hive/warehouse/census2021.db/ada/98-401-X2021012_English_CSV_data.csv | head
```

```csv
CENSUS_YEAR,DGUID,ALT_GEO_CODE,GEO_LEVEL,GEO_NAME,TNR_SF,TNR_LF,DATA_QUALITY_FLAG,CHARACTERISTIC_ID,CHARACTERISTIC_NAME,CHARACTERISTIC_NOTE,C1_COUNT_TOTAL,SYMBOL,C2_COUNT_MEN+,SYMBOL,C3_COUNT_WOMEN+,SYMBOL,C10_RATE_TOTAL,SYMBOL,C11_RATE_MEN+,SYMBOL,C12_RATE_WOMEN+,SYMBOL
2021,"2021S051610010001","10010001","Aggregate dissemination area","10010001",3.1,4.6,"00000",1,"Population, 2021",1,8881,"",,"...",,"...",,"...",,"...",,"..."
2021,"2021S051610010001","10010001","Aggregate dissemination area","10010001",3.1,4.6,"00000",2,"Population, 2016",1,9334,"",,"...",,"...",,"...",,"...",,"..."
2021,"2021S051610010001","10010001","Aggregate dissemination area","10010001",3.1,4.6,"00000",3,"Population percentage change, 2016 to 2021",,-4.9,"",,"...",,"...",-4.9,"",,"...",,"..."
2021,"2021S051610010001","10010001","Aggregate dissemination area","10010001",3.1,4.6,"00000",4,"Total private dwellings",2,5737,"",,"...",,"...",,"...",,"...",,"..."
2021,"2021S051610010001","10010001","Aggregate dissemination area","10010001",3.1,4.6,"00000",5,"Private dwellings occupied by usual residents",3,4121,"",,"...",,"...",,"...",,"...",,"..."
```

