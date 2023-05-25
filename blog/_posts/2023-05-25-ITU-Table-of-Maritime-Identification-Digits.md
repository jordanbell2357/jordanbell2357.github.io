---
layout: post
title: "ITU Table of Maritime Identification Digits"
topic: datasets
---

[ITU GLobal Administration Data System (GLAD)](https://www.itu.int/en/ITU-R/terrestrial/fmd/Pages/glad.aspx)

[Table of Maritime Identification Digits \| ITU](https://www.itu.int/en/ITU-R/terrestrial/fmd/Pages/mid.aspx)

`MaritimeIdentificationDigits-010734db-920d-4123-9280-a96784e0a892.xlsx`

We convert to `MaritimeIdentificationDigits.csv`

`head MaritimeIdentificationDigits.csv`

```csv
Digit,Allocated to
201,Albania (Republic of)
202,Andorra (Principality of)
203,Austria
204,Portugal - Azores
205,Belgium
206,Belarus (Republic of)
207,Bulgaria (Republic of)
208,Vatican City State
209,Cyprus (Republic of)
```

`databricks fs cp MaritimeIdentificationDigits.csv dbfs:/FileStore/tables` [^1]

[^1]: [Databricks CLI](https://docs.databricks.com/dev-tools/cli/index.html)

<iframe src="https://docs.google.com/spreadsheets/d/e/2PACX-1vSoz4rQDDWlWBjwkF683S5s00do-ccRmFAm3-dt_7MlHBm4AH1sn6mAy7_cVf5OLwXlaQjw8A9OAyxM/pubhtml?gid=1584142566&amp;single=true&amp;widget=true&amp;headers=false" width="100%" height="600"></iframe>