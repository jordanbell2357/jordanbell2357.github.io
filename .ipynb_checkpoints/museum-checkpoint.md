---
layout: page
title: Museum
permalink: /museum/
---

Excerpts from classic writings on the history and philosophy of education. Original text and selected English translations, with complete bibliographic data. For each quotation, multiple English translations are given - to have a robust sense of what a paragraph in a foreign language means while not knowing or nearly not knowing the language.

This collection developed from my readings in intellectual history, interest in translation, and as an exploration displaying Greek, Chinese, Arabic and Hebrew texts.

There is probably material here that could be added to Wikiquote. 

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