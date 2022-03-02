---
layout: page
title: Visualizations
permalink: /visualizations/
---

<table>
{% for visualization in site.visualizations %}
  <tr>
    <td><a href="{{ visualization.url }}">{{ visualization.title}}</a></td>
  </tr>
{% endfor %}
</table>
