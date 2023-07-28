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
G,CHARACTERISTIC_ID,CHARACTERISTIC_NAME,CHARACTERISTIC_NOTE,C1_COUNT_TOTAL,SYMBOL,C2_COUNT_MEN+,SYMBOL,C3_COUNT_WOMEN+,SYMBOL,C10_RATE_TOTAL,SYMBOL,C11_RATE_MEN+,SYMBOL,C12_RATE_WOMEN+,SYMBOL
2021,"2021A000011124","01","Country","Canada",3.1,4.3,"20000",1,"Population, 2021",1,36991981,"",,"...",,"...",,"...",,"...",,"..."
```

```bash
awk 'BEGIN {FS = OFS = ","} {gsub(/"/, ""); for (i=1; i<=NF; i++) if ($i == ".." || $i == "E" || $i == "F" || $i == "r" || $i == "x" || $i == "rE") $i = ""; else if ($i == "...") $i = ""; print}' 98-401-X2021001_English_CSV_data.csv > step1.csv
```

```bash
head -n 2 step1.csv
```

```csv
CENSUS_YEAR,DGUID,ALT_GEO_CODE,GEO_LEVEL,GEO_NAME,TNR_SF,TNR_LF,DATA_QUALITY_FLAG,CHARACTERISTIC_ID,CHARACTERISTIC_NAME,CHARACTERISTIC_NOTE,C1_COUNT_TOTAL,SYMBOL,C2_COUNT_MEN+,SYMBOL,C3_COUNT_WOMEN+,SYMBOL,C10_RATE_TOTAL,SYMBOL,C11_RATE_MEN+,SYMBOL,C12_RATE_WOMEN+,SYMBOL
2021,2021A000011124,01,Country,Canada,3.1,4.3,20000,1,Population, 2021,1,36991981,,,,,,,,,,,...
```

```bash
cut -d',' -f2,3,4,5,9,10,12,16,18 step1.csv > census2021_ada.csv
```

```bash
head census2021_ada.csv
```

```csv
DGUID,ALT_GEO_CODE,GEO_LEVEL,GEO_NAME,CHARACTERISTIC_ID,CHARACTERISTIC_NAME,C1_COUNT_TOTAL,C3_COUNT_WOMEN+,C10_RATE_TOTAL
2021A000011124,01,Country,Canada,1,Population,1,,
2021A000011124,01,Country,Canada,2,Population,1,,
2021A000011124,01,Country,Canada,3,Population percentage change,,,
2021A000011124,01,Country,Canada,4,Total private dwellings,16284235,,
2021A000011124,01,Country,Canada,5,Private dwellings occupied by usual residents,14978941,,
2021A000011124,01,Country,Canada,6,Population density per square kilometre,4.2,,4.2
2021A000011124,01,Country,Canada,7,Land area in square kilometres,8788702.8,,
2021A000011124,01,Country,Canada,8,Total - Age groups of the population - 100% data,36991980,18765740,100
2021A000011124,01,Country,Canada,9,  0 to 14 years,6012795,2926285,16.3
```

```bash
beeline -u jdbc:hive2://localhost:10000 -e "CREATE DATABASE IF NOT EXISTS census2021;"
hdfs dfs -ls /user/hive/warehouse/census2021.db
```

```bash
beeline -u jdbc:hive2://localhost:10000/census2021 -e "CREATE TABLE ada (DGUID STRING, ALT_GEO_CODE STRING, GEO_LEVEL STRING, GEO_NAME STRING, CHARACTERISTIC_ID INT, CHARACTERISTIC_NAME STRING, C1_COUNT_TOTAL INT, RATE_TOTAL DOUBLE) ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' STORED AS TEXTFILE;"
hdfs dfs -ls /user/hive/warehouse/census2021.db/ada
```

```bash
hdfs dfs -put census2021_ada.csv /user/hive/warehouse/census2021.db/ada/
hdfs dfs -cat /user/hive/warehouse/census2021.db/ada/census2021_ada.csv | head
```

```csv
DGUID,ALT_GEO_CODE,GEO_LEVEL,GEO_NAME,CHARACTERISTIC_ID,CHARACTERISTIC_NAME,C1_COUNT_TOTAL,C3_COUNT_WOMEN+,C10_RATE_TOTAL
2021A000011124,01,Country,Canada,1,Population,1,,
2021A000011124,01,Country,Canada,2,Population,1,,
2021A000011124,01,Country,Canada,3,Population percentage change,,,
2021A000011124,01,Country,Canada,4,Total private dwellings,16284235,,
2021A000011124,01,Country,Canada,5,Private dwellings occupied by usual residents,14978941,,
2021A000011124,01,Country,Canada,6,Population density per square kilometre,4.2,,4.2
2021A000011124,01,Country,Canada,7,Land area in square kilometres,8788702.8,,
2021A000011124,01,Country,Canada,8,Total - Age groups of the population - 100% data,36991980,18765740,100
2021A000011124,01,Country,Canada,9,  0 to 14 years,6012795,2926285,16.3
```

```bash
beeline -u jdbc:hive2://localhost:10000/census2021 -e "LOAD DATA INPATH '/user/hive/warehouse/census2021.db/ada/census2021_ada.csv' INTO TABLE ada;"
beeline -u jdbc:hive2://localhost:10000/census2021 -e "SELECT * FROM ada LIMIT 10;"
```

```bash
hive -S -e "set hive.cli.print.header=true; set hive.resultset.use.unique.column.names=false; set hive.cli.print.row.delimiter='\n'; set hive.cli.print.header=false; SELECT * FROM census2021.ada LIMIT 10;" | sed '/WARN:/d; s/[[:space:]]\+/,/g' > output.csv
cat output.csv
```

```csv
DGUID,ALT_GEO_CODE,GEO_LEVEL,GEO_NAME,NULL,CHARACTERISTIC_NAME,NULL,NULL
2021A000011124,01,Country,Canada,1,Population,1,NULL
2021A000011124,01,Country,Canada,2,Population,1,NULL
2021A000011124,01,Country,Canada,3,Population,percentage,change,NULL,NULL
2021A000011124,01,Country,Canada,4,Total,private,dwellings,16284235,NULL
2021A000011124,01,Country,Canada,5,Private,dwellings,occupied,by,usual,residents,14978941,NULL
2021A000011124,01,Country,Canada,6,Population,density,per,square,kilometre,4,NULL
2021A000011124,01,Country,Canada,7,Land,area,in,square,kilometres,8788702,NULL
2021A000011124,01,Country,Canada,8,Total,-,Age,groups,of,the,population,-,100%,data,36991980,1.876574E7
2021A000011124,01,Country,Canada,9,0,to,14,years,6012795,2926285.0
```

