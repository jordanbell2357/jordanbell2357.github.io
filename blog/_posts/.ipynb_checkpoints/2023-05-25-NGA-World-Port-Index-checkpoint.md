---
layout: post
title: National Geospatial-Intelligence Agency (NGA) World Port Index (Pub 150) (WPI)
topic: datasets
---

[National Geospatial-Intelligence Agency (NGA) Maritime Safety Information](https://msi.nga.mil/)

[World Port Index (Pub 150)](https://msi.nga.mil/Publications/WPI)

{% include databricks_iframe.html %}

![WPI](/images/NGA/WPI.png)

![df_reduced_north_america](/images/NGA/df_reduced_north_america.png)

![Kepler.gl](/images/NGA/keplergl-WPI.jpeg)

<div style="overflow:auto;">
  <table style="table-layout:fixed; width:100%;">
    <thead>
      <tr>
        {% for column in site.data.WorldPortIndex_dictionary[0] %}
          <th>{{ column[0] }}</th>
        {% endfor %}
      </tr>
    </thead>
    <tbody>
      {% for row in site.data.WorldPortIndex_dictionary %}
        <tr>
          {% for column in row %}
            <td>{{ column[1] }}</td>
          {% endfor %}
        </tr>
      {% endfor %}
    </tbody>
  </table>
</div>



<div style="overflow:auto;">
  <table style="table-layout:fixed; width:100%;">
    <thead>
      <tr>
        {% for pair in site.data.WorldPortIndex_dictionary[0] %}
          <th>{{ pair[0] }}</th>
        {% endfor %}
      </tr>
    </thead>
    <tbody>
      {% for row in site.data.MaritimeIdentificationDigits %}
        <tr>
          {% for pair in row %}
            <td>{{ pair[1] }}</td>
          {% endfor %}
        </tr>
      {% endfor %}
    </tbody>
  </table>
</div>