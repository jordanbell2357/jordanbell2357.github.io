---
layout: page
title: Writings
permalink: /writings/
---

{% for writing in site.writings %}
  <li>
    <a href="{{ writing.url }}">{{ writing.title}}</a>
  </li>
{% endfor %}