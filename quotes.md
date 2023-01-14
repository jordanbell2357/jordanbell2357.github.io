---
layout: page
title: Quotes
permalink: /quotes/
---

#### Museum

Excerpts from classic writings on the history and philosophy of education. Original text and selected English translations, with complete bibliographic data. For each quotation, multiple English translations are given - to have a robust sense of what a paragraph in a foreign language means while not knowing or nearly not knowing the language.

This collection developed from (i) my readings in intellectual history, (ii) my interest in translation, (iii) as an exploration displaying Greek, Chinese, Arabic and Hebrew texts, and
(iv), as an exploration of  text and image digitization projects.

Something that is a sentence in English may be part of a long paragraph in Latin. Furthermore, even beyond the paragraph unit, each quotation is given with substantial context - enough to get a sense of the work in which the quotation lives.

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
<ul>
{% for quote in site.quotes %}
  <li>
    <a href="{{ quote.url }}">{{ quote.title}}</a>
  </li>
{% endfor %}
</ul>