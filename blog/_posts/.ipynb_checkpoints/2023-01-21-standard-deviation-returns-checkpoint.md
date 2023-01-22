---
layout: post
title: Standard deviation of returns
---
  
{% assign table_rows = site.data.Hasbro2014 %}
  
<table>
  {% for row in table_rows %}
    {% if forloop.first %}
    <tr>
      {% for pair in row %}
        <th>{{ pair[0] }}</th>
      {% endfor %}
    </tr>
    {% endif %}
  {% endfor %}
</table>
