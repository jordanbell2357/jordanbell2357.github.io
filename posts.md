---
layout: page
title: Posts
permalink: /posts/
---

<ul>
{% for quote in site.posts %}
  <li>
    <a href="{{ post.url }}">{{ post.title}}</a>
  </li>
{% endfor %}
</ul>