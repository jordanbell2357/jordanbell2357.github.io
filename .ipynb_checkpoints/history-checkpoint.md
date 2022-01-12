---
layout: page
title: History
permalink: /history/
---

# Excerpts from classic writings on the history and philosophy of education

Quotations on education with original text and selected English translations, with complete bibliographic data. For each quotation, multiple English translations are given - to have a robust sense of what a paragraph in a foreign language means without knowing that language.

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