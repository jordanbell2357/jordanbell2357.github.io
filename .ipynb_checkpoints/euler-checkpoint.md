---
layout: page
title: Euler
permalink: /euler/
---

## Euler, *The Elements of Algebra*

{% for chapter in site.euler %}
- [{{chapter.title}}]({{ chapter.url }})
{% endfor %}