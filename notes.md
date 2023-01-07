---
layout: page
title: Notes
permalink: /notes/
---

<ul class="spaced_list">
  {% for post in site.notes %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a> {{ post.date | date_to_long_string }}
    </li>
  {% endfor %}
</ul>