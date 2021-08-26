---
layout: page
title: Quotes
permalink: /quotes/
---

### Excerpts on learning

{%- assign date_format = site.minima.date_format | default: "%b %-d, %Y" -%}

<ul>
  {% for post in site.posts %}
    {% if post.category == 'quotes' %}
      <li>
        <a href="{{ post.url }}">{{ post.title }}</a>
        <span class="post-meta">{{ post.date | date: date_format }}</span>
      </li>
    {% endif %}
  {% endfor %}
</ul>
