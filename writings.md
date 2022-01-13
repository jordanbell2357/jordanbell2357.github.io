---
layout: page
title: Writings
permalink: /writings/
---

{% for note in site.notes %}
  <li>
    <a href="{{ note.url }}">{{ note.title}}</a>
  </li>
{% endfor %}