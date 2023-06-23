---
layout: post
title: BigQuery duplicate entries
topic: uscg-nais
---



<iframe src="https://docs.google.com/spreadsheets/d/e/2PACX-1vSl2M3TYzX_680dQLsTtoUjMmDFf14ZfPa6L9Xr7Ddj-67pT60qKCuClJjwqhrhOp6ij9H7qWX4FepN/pubhtml?gid=0&amp;single=true&amp;widget=true&amp;headers=false" width="100%" height="400"></iframe>

```sql
DELETE FROM `ais-data-385301.uscg.nais`
WHERE DATE(BaseDateTime) = '2022-01-23';
```

<iframe src="https://docs.google.com/spreadsheets/d/e/2PACX-1vSF0vY_ng_U__puWldyFqWhFygwLgSQUO2h72XL9UFuBAkTx9CpcKB6awf7z7XlYwR-m81BkGniIA_6/pubhtml?gid=0&amp;single=true&amp;widget=true&amp;headers=false" width="100%" height="400"></iframe>
