---
layout: page
title: Examples
permalink: /examples/
---

- [Examples](#examples)
- [GeoGebra](#geogebra)
- [Desmos](#desmos)
- [WebQuiz](#webquiz)

# Examples {#examples}

<ul>
{% for example in site.examples %}
  <li><a href="{{ example.url }}">{{ example.title}} {{ example.math}}</a></li>
{% endfor %}
</ul>

# GeoGebra {#geogebra}

<ul>
{% for exercise in site.geogebra %}
    <li><a href="{{ exercise.url }}">{{ exercise.title}}</a></li>
{% endfor %}
</ul>

# Desmos {#desmos}

1. [Standard form, factored form, and vertex form](https://www.desmos.com/calculator/zrpmztunq0)

1. [Riemann sums example #1](https://www.desmos.com/calculator/cbhiymlls7)

2. [Riemann sums example #2](https://www.desmos.com/calculator/abk5szfm0h)

3. [Riemann sums example #3](https://www.desmos.com/calculator/ryrp6oip6q)

4. [Riemann sums example #4](https://www.desmos.com/calculator/gntgmzpxwm)

# WebQuiz {#webquiz}

1. [Systems of linear equations](https://jordanbell.info/WebQuiz/wq1.html)

2. [Systems of linear equations](https://jordanbell.info/WebQuiz/wq2.html)

3. [Systems of linear equations](https://jordanbell.info/WebQuiz/wq3.html)