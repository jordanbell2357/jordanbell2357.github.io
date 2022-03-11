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

{% for example in site.examples %}
1. [{{ example.title}} {{ example.math}}]({{ example.url }})
{% endfor %}

# GeoGebra {#geogebra}

{% for exercise in site.geogebra %}
1. [{{ exercise.title}}]({{ exercise.url }})
{% endfor %}

# Desmos {#desmos}

1. [Standard form, factored form, and vertex form](https://www.desmos.com/calculator/zrpmztunq0)

1. [Riemann sums for \\(x^{2}\sin(x)\\)](https://www.desmos.com/calculator/cbhiymlls7)

1. [Riemann sums for \\(\sin\big(\frac{x^{2}}{4}\big)\\)](https://www.desmos.com/calculator/abk5szfm0h)

1. [Riemann sums for \\(2^{x}\\)](https://www.desmos.com/calculator/ryrp6oip6q)

1. [Riemann sums for \\(\prod\\)](https://www.desmos.com/calculator/gntgmzpxwm)

# WebQuiz {#webquiz}

1. [Systems of linear equations](https://jordanbell.info/WebQuiz/wq1.html)

1. [Systems of linear equations](https://jordanbell.info/WebQuiz/wq2.html)

1. [Systems of linear equations](https://jordanbell.info/WebQuiz/wq3.html)