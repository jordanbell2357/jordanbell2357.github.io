---
layout: page
title: Posts
permalink: /posts/
---

<ul>
{% for post in site.posts %}
  <li>
    <a href="{{ post.url }}">{{ post.title, post.date}}</a>
  </li>
{% endfor %}
</ul>