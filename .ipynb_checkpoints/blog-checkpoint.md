---
layout: page
title: Blog
permalink: /blog/
---

<ul class="spaced_list">
  {% for post in site.categories.blog %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a> {{ post.date | date_to_long_string }}
    </li>
  {% endfor %}
</ul>