---
layout: post
title: DHL Global Connectedness Index
---

[DHL Global Connectedness Index (GCI)](https://www.dhl.com/global-en/delivered/globalization/global-connectedness-index.html)

[DHL Global Connectedness Index \| NYU Stern](https://www.stern.nyu.edu/experience-stern/about/departments-centers-initiatives/centers-of-research/center-future-management/dhl-initiative-globalization/dhl-global-connectedness-index)

{% assign table_rows1 = site.data.GCI_Data %}

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

[^1]

[^1]: <https://www.convertcsv.com/transpose-csv.htm>