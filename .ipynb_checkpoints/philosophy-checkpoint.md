---
layout: page
title: Philosophy
permalink: /philosophy/
---

# Excerpts from classic writings on the philosophy of education

Quotations on education with original text and selected English translations. For each quotation, multiple English translations are given. 

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