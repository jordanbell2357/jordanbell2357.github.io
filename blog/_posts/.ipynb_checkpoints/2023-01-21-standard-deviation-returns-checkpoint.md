---
layout: post
title: Standard deviation of returns
---

`GOOGLEFINANCE("TSE:H","price",DATE(2022,1,1),DATE(2022,12,31),"WEEKLY")`

{% assign table_rows1 = site.data.TSE_H %}

<div style="overflow-x:auto;">
  <table>
      {% for row in table_rows1 %}
          {% if forloop.first %}
              <tr>
                  {% for pair in row %}
                      <th>
                          {{ pair[0] }}
                      </th>
                  {% endfor %}
              </tr>
          {% endif %}

          {% tablerow pair in row %}
              {{ pair[1] }}
          {% endtablerow %}
      {% endfor %}
  </table>
</div>

`GOOGLEFINANCE("OSPTX","price",DATE(2022,1,1),DATE(2022,12,31),"WEEKLY")`

{% assign table_rows2 = site.data.OSPTX %}

<div style="overflow-x:auto;">
  <table>
      {% for row in table_rows2 %}
          {% if forloop.first %}
              <tr>
                  {% for pair in row %}
                      <th>
                          {{ pair[0] }}
                      </th>
                  {% endfor %}
              </tr>
          {% endif %}

          {% tablerow pair in row %}
              {{ pair[1] }}
          {% endtablerow %}
      {% endfor %}
  </table>
</div>

`GOOGLEFINANCE("INDEXSP:.INX","price",DATE(2022,1,1),DATE(2022,12,31),"WEEKLY")`

{% assign table_rows3 = site.data.INDEXSP %}

<div style="overflow-x:auto;">
  <table>
      {% for row in table_rows3 %}
          {% if forloop.first %}
              <tr>
                  {% for pair in row %}
                      <th>
                          {{ pair[0] }}
                      </th>
                  {% endfor %}
              </tr>
          {% endif %}

          {% tablerow pair in row %}
              {{ pair[1] }}
          {% endtablerow %}
      {% endfor %}
  </table>
</div>


  
[^1] [^2] [^3]

[^1]: [Data Files \| Jekyll](https://jekyllrb.com/docs/datafiles/)

[^2]: [Tabulate CSV Data \| Jekyll](https://jekyllrb.com/tutorials/csv-to-table/)

[^3]: [Data files in Jekyll \| CloudCannon](https://cloudcannon.com/community/learn/jekyll-tutorial/introduction-to-jekyll-data-files/)