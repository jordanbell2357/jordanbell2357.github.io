---
layout: post
title: "Including text in Jekyll using _includes and _data"
---

```{% include txt/cities.tsv %}```

<pre>
{% include txt/cities.tsv %}
</pre>

<table>
  {% for row in site.data.join.tsv.cities %}
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

<pre>
{% include txt/cities.csv %}
</pre>

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

---

[Includes \| Jekyll](https://jekyllrb.com/docs/includes/)

[Data Files \| Jekyll](https://jekyllrb.com/docs/datafiles/)

[Tabulate CSV Data \| Jekyll](https://jekyllrb.com/tutorials/csv-to-table/)

[Data files in Jekyll \| CloudCannon](https://cloudcannon.com/community/learn/jekyll-tutorial/introduction-to-jekyll-data-files/)