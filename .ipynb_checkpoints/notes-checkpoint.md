---
layout: page
title: Notes
permalink: /notes/
---

{% for example in site.notes %}
1. [{{example.title}}]({{ example.url }})
{% endfor %}