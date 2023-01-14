---
layout: post
title: Loading data from CSV and TSV in Jekyll
---

<table>
  {% for row in site.data.join.csv.cities %}
    {% if forloop.first %}
    <tr>
      {% for pair in row %}
        <th>{{ pair[0] }}</th>
      {% endfor %}
    </tr>
    {% endif %}

    {% tablerow pair in row %}
      {{ pair[1] }}
    {% endtablerow %}
  {% endfor %}
</table>

<div><object data="_data/join/cities.csv"></object></div>

---

<https://jekyllrb.com/tutorials/csv-to-table/>

[CloudCannon Data files in Jekyll](https://cloudcannon.com/community/learn/jekyll-tutorial/introduction-to-jekyll-data-files/)