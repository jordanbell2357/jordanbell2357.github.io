---
layout: page
title: Quotes
permalink: /quotes/
---

### Excerpts on learning

<ul>
  {% for post in site.posts | where: "categories", "maxims" %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a>
    </li>
  {% endfor %}
</ul>