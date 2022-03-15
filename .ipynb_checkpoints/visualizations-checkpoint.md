---
layout: page
title: Visualizations
permalink: /visualizations/
---

{% for visualization in site.visualizations %}
1. [{{ visualization.title}}]({{ visualization.url }})
{% endfor %}