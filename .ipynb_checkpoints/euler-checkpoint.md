---
layout: page
title: Euler
permalink: /euler/
---

## Euler, *The Elements of Algebra*

{% for chapter in site.euler %}
1. [{{chapter.title}}]({{ chapter.url }})
{% endfor %}