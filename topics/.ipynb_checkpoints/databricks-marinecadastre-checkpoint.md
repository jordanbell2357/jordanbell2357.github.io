---
layout: default
title: MarineCadastre.gov AIS data with Databricks
permalink: /topics/databricks-marinecadastre/
---

<h1>{{ page.title }}</h1>

<ul class="spaced_list">
  {% for post in site.posts %}
    {% if post.topic == 'databricks-marinecadastre' %}
      <li>
        {{ post.date | date_to_long_string }} <a href="{{ post.url }}">{{ post.title }}</a>
      </li>
    {% endif %}
  {% endfor %}
</ul>