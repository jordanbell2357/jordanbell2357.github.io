---
layout: page
title: Visualizations
permalink: /visualizations/
---

{% for visualization in site.visualizations %}
- [{{ visualization.title}}]({{ visualization.url }})
{% endfor %}