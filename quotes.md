---
layout: page
title: Quotes
permalink: /quotes/
---

### Excerpts on learning

<!--
<ul>
  {% for post in site.posts %}
    {% if post.category == 'quotes' %}
      <li>
        <a href="{{ post.url }}">{{ post.title }}</a>
      &ensp; {{ post.date | date: '%B %d, %Y'}}
      </li>
    {% endif %}
  {% endfor %}
</ul>
-->

{% for quote in site.quotes %}
  <li>
    <a href="{{ quote.url }}">{{ quote.title}}</a>
  </li>
{% endfor %}