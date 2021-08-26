---
layout: page
title: Quotes
permalink: /quotes/
---

### Excerpts on learning

<ul>
  {% assign posts = site.posts | where_exp: "item", "item.tags contains 'maxims'" %}
  {% for post in posts %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a>
    </li>
  {% endfor %}
</ul>