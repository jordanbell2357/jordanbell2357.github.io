---
layout: post
title: Loading data from CSV and TSV in Jekyll
---

<https://jekyllrb.com/tutorials/csv-to-table/>

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