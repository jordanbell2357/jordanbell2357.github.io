---
layout: default
title: Learning content
permalink: /topics/learning-content/
---

<h1>{{ page.title }}</h1>

<ul class="spaced_list">
  {% for post in site.posts %}
    {% if post.topic == 'learning-content' %}
      <li>
        {{ post.date | date_to_long_string }} <a href="{{ post.url }}">{{ post.title }} \({{ post.math }}\)</a>
      </li>
    {% endif %}
  {% endfor %}
</ul>
