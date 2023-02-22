---
layout: page
title: Examples
permalink: /examples/
---

- [Examples](#examples)
- [Desmos](#desmos)
- [Geogebra](#geogebra)
- [WebQuiz](#webquiz)

## Examples {#exmaples}

<ol class="spaced_list">
  {% for post in site.categories.examples %}
    <li>
      <a href="{{ post.url }}">{{ post.title }} \({{ post.math}}\)</a> {{ post.date | date_to_long_string }}
    </li>
  {% endfor %}
</ol>

## Desmos {#desmos}

<ol class="spaced_list">
  {% for post in site.categories.desmos %}
    <li>
      <a href="{{ post.url }}">{{ post.title }} \({{ post.math}}\)</a> {{ post.date | date_to_long_string }}
    </li>
  {% endfor %}
</ol>

## GeoGebra {#geogebra}

<ol class="spaced_list">
  {% for post in site.categories.geogebra %}
    <li>
      <a href="{{ post.url }}">{{ post.title }} \({{ post.math }}\)</a> {{ post.date | date_to_long_string }}
    </li>
  {% endfor %}
</ol>

## WebQuiz {#webquiz}

1. [Systems of linear equations](https://jordanbell.info/WebQuiz/wq1.html)

1. [Systems of linear equations](https://jordanbell.info/WebQuiz/wq2.html)

1. [Systems of linear equations](https://jordanbell.info/WebQuiz/wq3.html)