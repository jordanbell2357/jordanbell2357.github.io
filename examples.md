---
layout: page
title: Examples
permalink: /examples/
---

{% for example in site.examples %}
- [{{ example.title}} {{ example.math}}]({{ example.url }})
{% endfor %}

{% for exercise in site.gm %}
- [{{ exercise.title}}]({{ exercise.url }})
{% endfor %}


- [Systems of linear equations](https://jordanbell.info/WebQuiz/wq1.html)

- [Systems of linear equations](https://jordanbell.info/WebQuiz/wq2.html)

- [Systems of linear equations](https://jordanbell.info/WebQuiz/wq3.html)