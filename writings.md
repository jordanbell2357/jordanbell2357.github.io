---
layout: page
title: Writings
permalink: /writings/
---

[Adeles](/latex/writings/adeles/adeles.html)

{% for writing in site.writings %}
  <li>
    <a href="{{ writing.url }}">{{ writing.title}}</a>
  </li>
{% endfor %}