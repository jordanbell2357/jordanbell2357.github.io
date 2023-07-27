---
layout: post
title: Ingesting Canada Census 2021 ADA level data into hdfs
---

<https://www12.statcan.gc.ca/census-recensement/2021/dp-pd/prof/details/download-telecharger/comp/GetFile.cfm?Lang=E&FILETYPE=CSV&GEONO=012>

```bash
curl -o 98-401-X2021012_eng_CSV.zip \
https://www12.statcan.gc.ca/census-recensement/2021/dp-pd/prof/details/download-telecharger/comp/GetFile.cfm?Lang=E&FILETYPE=CSV&GEONO=012
unzip 98-401-X2021012_eng_CSV.zip
```

```bash
head -n 2 98-401-X2021001_English_CSV_data.csv
```

```csv
CENSUS_YEAR,DGUID,ALT_GEO_CODE,GEO_LEVEL,GEO_NAME,TNR_SF,TNR_LF,DATA_QUALITY_FLAG,CHARACTERISTIC_ID,CHARACTERISTIC_NAME,CHARACTERISTIC_NOTE,C1_COUNT_TOTAL,SYMBOL,C2_COUNT_MEN+,SYMBOL,C3_COUNT_WOMEN+,SYMBOL,C10_RATE_TOTAL,SYMBOL,C11_RATE_MEN+,SYMBOL,C12_RATE_WOMEN+,SYMBOL
2021,"2021A000011124","01","Country","Canada",3.1,4.3,"20000",1,"Population, 2021",1,36991981,"",,"...",,"...",,"...",,"...",,"..."
```

```bash
cut -d',' -f2,3,4,5,9,10,12,14,16,18,20,22 98-401-X2021001_English_CSV_data.csv > census2021_ada.csv
head -n 2 census2021_ada.csv
```

```csv
DGUID,ALT_GEO_CODE,GEO_LEVEL,GEO_NAME,CHARACTERISTIC_ID,CHARACTERISTIC_NAME,C1_COUNT_TOTAL,C2_COUNT_MEN+,C3_COUNT_WOMEN+,C10_RATE_TOTAL,C11_RATE_MEN+,C12_RATE_WOMEN+
"2021A000011124","01","Country","Canada",1,"Population,1,"","...","...","...","..."
```

```bash
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

`load_census_data.sql`

```sql
-- load_census_data.sql

-- Create the external table
CREATE EXTERNAL TABLE IF NOT EXISTS census_data_2021 (
  CENSUS_YEAR INT,
  DGUID STRING,
  ALT_GEO_CODE INT,
  GEO_LEVEL STRING,
  GEO_NAME STRING,
  TNR_SF DOUBLE,
  TNR_LF DOUBLE,
  DATA_QUALITY_FLAG INT,
  CHARACTERISTIC_ID INT,
  CHARACTERISTIC_NAME STRING,
  CHARACTERISTIC_NOTE INT,
  C1_COUNT_TOTAL INT,
  SYMBOL STRING,
  C2_COUNT_MEN_PLUS DOUBLE,
  SYMBOL STRING,
  C3_COUNT_WOMEN_PLUS DOUBLE,
  SYMBOL STRING,
  C10_RATE_TOTAL DOUBLE,
  SYMBOL STRING,
  C11_RATE_MEN_PLUS DOUBLE,
  SYMBOL STRING,
  C12_RATE_WOMEN_PLUS DOUBLE,
  SYMBOL STRING
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE
LOCATION '/user/hive/warehouse/census2021.db/ada/';

-- Load data into the table
LOAD DATA INPATH '/user/hive/warehouse/census2021.db/ada/98-401-X2021001_English_CSV_data.csv' INTO TABLE census_data_2021;
```

```bash
beeline -u jdbc:hive2://localhost:10000 -f load_census_data.sql
```
