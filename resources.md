---
layout: page
title: Resources
permalink: /exercise-resources/
---

- [CK-12](#ck12)

## CK-12 {#ck12}

<table>
{% for exercise in site.ck12 %}
  <tr>
    <td><a href="{{ exercise.url }}">{{ exercise.title}}</a></td>
  </tr>
{% endfor %}
</table>