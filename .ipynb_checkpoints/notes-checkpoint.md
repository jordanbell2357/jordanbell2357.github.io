---
layout: page
title: Notes
permalink: /notes/
---

{% for example in site.notes %}
- [{{example.title}}]({{ example.url }})
{% endfor %}