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

[The Pontryagin dual of Q](/latex/notes/QPontryaginDual/Q-Pontryagin/Q-Pontryagin.html)