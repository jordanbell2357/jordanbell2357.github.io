---
layout: post
title: Standard deviation of returns
topic: finance
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

Standard deviation of weekly returns of TSE:H is 0.025332

Annualized standard deviation of TSE:H is

$$
\sigma_{\textrm{TSE:H}}= 0.025332 \cdot \sqrt{52} = 0.182675
$$

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

Standard deviation of weekly returns of OSPTX is 0.022458

Annualized standard deviation of OSPTX is

$$
\sigma_{\textrm{OSPTX}}= 0.022458 \cdot \sqrt{52} = 0.161945
$$

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

Standard deviation of weekly returns of INDEXSP is 0.032259

Annualized standard deviation of INDEXSP is

$$
\sigma_{\textrm{INDEXSP}}= 0.032259 \cdot \sqrt{52} = 0.232624
$$

Correlation of weekly returns of TSE:H and OSPTX is

$$
\rho_{\textrm{TSE:H,OSPTX}} = 0.315180.
$$

Correlation of weekly returns of TSE:H and INDEXSP is

$$
\rho_{\textrm{TSE:H,INDEXSP}} = 0.339743.
$$

Using OSPTX as the market,

$$
\beta_{\textrm{TSE:H};\textrm{OSPTX}} = \dfrac{\sigma_{\textrm{TSE:H}} \cdot \rho_{\textrm{TSE:H,OSPTX}}}{\sigma_{\textrm{OSPTX}}} = 0.355525
$$

Using INDEXSP as the market,

$$
\beta_{\textrm{TSE:H};\textrm{INDEXSP}} = \dfrac{\sigma_{\textrm{TSE:H}} \cdot \rho_{\textrm{TSE:H,INDEXSP}}}{\sigma_{\textrm{INDEXSP}}} = 0.266793
$$


  
[^1] [^2] [^3]

[^1]: [Data Files \| Jekyll](https://jekyllrb.com/docs/datafiles/)

[^2]: [Tabulate CSV Data \| Jekyll](https://jekyllrb.com/tutorials/csv-to-table/)

[^3]: [Data files in Jekyll \| CloudCannon](https://cloudcannon.com/community/learn/jekyll-tutorial/introduction-to-jekyll-data-files/)