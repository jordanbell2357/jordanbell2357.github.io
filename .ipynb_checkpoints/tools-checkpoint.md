---
layout: page
title: Tools
permalink: /tools/
---

* [Desmos](https://www.desmos.com/)
* [GeoGebra](https://www.geogebra.org/geometry)
* [Wolfram Alpha](https://www.wolframalpha.com/)

# PhET {#phet}

{% for exercise in site.phet %}
1. [{{ exercise.title}}]({{ exercise.url }})
{% endfor %}