---
layout: page
title: Writing
permalink: /writing/
---

<ul class="spaced_list">
  {% for post in site.categories.writing %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a> {{ post.date | date_to_long_string }}
    </li>
  {% endfor %}
</ul>

<!--
https://learn.cloudcannon.com/jekyll/list-posts-in-a-category/
-->