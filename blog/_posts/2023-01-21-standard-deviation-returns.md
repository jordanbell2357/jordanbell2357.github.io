---
layout: post
title: Standard deviation of returns
---

{% assign table_rows = site.data.TSE_H %}

  <table class="fixed_header">
      {% for row in table_rows %}
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
  
[^1] [^2] [^3]

[^1]: [Data Files \| Jekyll](https://jekyllrb.com/docs/datafiles/)

[^2]: [Tabulate CSV Data \| Jekyll](https://jekyllrb.com/tutorials/csv-to-table/)

[^3]: [Data files in Jekyll \| CloudCannon](https://cloudcannon.com/community/learn/jekyll-tutorial/introduction-to-jekyll-data-files/)