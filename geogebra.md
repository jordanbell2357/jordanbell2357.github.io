---
layout: page
title: GeoGebra
permalink: /geogebra/
---

{% for exercise in site.geogebra %}
1. [{{ exercise.title}}]({{ exercise.url }})
{% endfor %}
