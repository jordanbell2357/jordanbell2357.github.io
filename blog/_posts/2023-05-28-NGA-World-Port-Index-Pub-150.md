---
layout: post
title: NGA MSI World Port Index (Pub 150) (WPI)
---

[Maritime Safety Information (MSI) \| National Geospatial-Intelligence Agency (NGA)](https://msi.nga.mil/)

[World Port Index (Pub 150) (WPI)](https://msi.nga.mil/Publications/WPI)

> The World Port Index (Pub 150) contains the location and physical characteristics of, and the facilities and services offered by major ports and terminals world-wide. Entries are numbered geographically. In 2020, NGA undertook an effort to modernize the content and delivery of the World Port Index, resulting in additional and enhanced data fields, and a web application viewing platform. The modernization also implemented crowd-sourcing methods to validate and update the content.
>
> The csv file is the official version of the content, and the accompanying Explanation of Data Fields document contains additional information regarding the data fields. The complete WPI content is provided below and updated monthly.

`UpdatedPub150.csv`

Retrieved May 28, 2023.

[Explanation of Data Fields](https://msi.nga.mil/api/publications/download?key=16920959/SFH00000/WPI_Explanation_of_Data_Fields.pdf&type=view)

`WPI_Explanation_of_Data_Fields.pdf`

<div style="overflow-x:auto;">
  <table>
      {% for row in site.data.WorldPortIndex_dictionary %}
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