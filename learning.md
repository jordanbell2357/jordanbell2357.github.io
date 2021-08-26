---
layout: page
title: Quotes
permalink: /quotes/
---

### Excerpts on learning

{% assign posts = site.posts | filter_posts: "tags", "include 'maxims'" %}

<ul>
  {% for post in posts %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a>
    </li>
  {% endfor %}
</ul>