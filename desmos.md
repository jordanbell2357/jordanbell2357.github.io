---
layout: page
title: Desmos
permalink: /desmos/
---

1. [Standard form, factored form, and vertex form](https://www.desmos.com/calculator/zrpmztunq0)

1. [Riemann sums for \\(x^{2}\sin(x)\\)](https://www.desmos.com/calculator/cbhiymlls7)

1. [Riemann sums for \\(\sin\big(\frac{x^{2}}{4}\big)\\)](https://www.desmos.com/calculator/abk5szfm0h)

1. [Riemann sums for \\(2^{x}\\)](https://www.desmos.com/calculator/ryrp6oip6q)

1. [Riemann sums for \\(\prod_{k=1}^K\vert \sin(kx)\vert \\)](https://www.desmos.com/calculator/gntgmzpxwm)

{% for post in site.desmos %}
1. [{{ post.title}} {{ post.math}}]({{ post.url }})
{% endfor %}