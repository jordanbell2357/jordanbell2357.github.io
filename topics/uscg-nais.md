---
layout: default
title: U.S. Coast Guard Nationwide Automatic Identification System (NAIS)
permalink: /topics/uscg-nais/
---

<h1>{{ page.title }}</h1>

<ul class="spaced_list">
  {% for post in site.posts %}
    {% if post.topic == 'uscg-nais' %}
      <li>
        {{ post.date | date_to_long_string }} <a href="{{ post.url }}">{{ post.title }} \({{ post.math }}\)</a>
      </li>
    {% endif %}
  {% endfor %}
</ul>
