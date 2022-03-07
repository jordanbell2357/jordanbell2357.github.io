---
layout: page
title: Content
permalink: /content/
---

- [Examples](#examples)
- [WebQuiz](#webquiz)
- [Desmos](#desmos)
- [GeoGebra](#geogebra)

# Examples {#examples}

<table>
{% for example in site.examples %}
  <tr>
    <td><a href="{{ example.url }}">{{ example.title}}</a></td>
  </tr>
{% endfor %}
</table>

# WebQuiz {#webquiz}

1. [Systems of linear equations](https://jordanbell.info/WebQuiz/wq1.html)

2. [Systems of linear equations](https://jordanbell.info/WebQuiz/wq2.html)

3. [Systems of linear equations](https://jordanbell.info/WebQuiz/wq3.html)

# Desmos {#desmos}

1. [Standard form, factored form, and vertex form](https://www.desmos.com/calculator/zrpmztunq0)

1. [Riemann sums example #1](https://www.desmos.com/calculator/cbhiymlls7)

2. [Riemann sums example #2](https://www.desmos.com/calculator/abk5szfm0h)

3. [Riemann sums example #3](https://www.desmos.com/calculator/ryrp6oip6q)

4. [Riemann sums example #4](https://www.desmos.com/calculator/gntgmzpxwm)

# GeoGebra {#geogebra}

<table>
{% for exercise in site.geogebra %}
  <tr>
    <td><a href="{{ exercise.url }}">{{ exercise.title}}</a></td>
  </tr>
{% endfor %}
</table>


