---
layout: page
title: Relational algebra
---

<https://dbis-uibk.github.io/relax/landing>

<https://db.grussell.org/ch5.html>



employee = 


<table>
<thead>
  <tr>
    <th>nr</th>
    <th>name</th>
    <th>salary</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>1</td>
    <td>John</td>
    <td>100</td>
  </tr>
  <tr>
    <td>5</td>
    <td>Sarah</td>
    <td>300</td>
  </tr>
  <tr>
    <td>7</td>
    <td>Tom</td>
    <td>100</td>
  </tr>
</tbody>
</table>

```sql
SELECT salary FROM employee
```

<table>
<thead>
  <tr>
    <th>salary</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>100</td>
  </tr>
  <tr>
    <td>300</td>
  </tr>
  <tr>
    <td>100</td>
  </tr>
</tbody>
</table>

$$\Pi_{\mathrm{salary}}(\mathrm{employee})$$

