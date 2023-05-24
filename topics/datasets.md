---
layout: default
title: Datasets
permalink: /topics/datasets/
---

<h1>{{ page.title }}</h1>

<ul class="spaced_list">
  {% for post in site.posts %}
    {% if post.topics contains 'datasets' %}
      <li>
        {{ post.date | date_to_long_string }} <a href="{{ post.url }}">{{ post.title }}</a>
      </li>
    {% endif %}
  {% endfor %}
</ul>