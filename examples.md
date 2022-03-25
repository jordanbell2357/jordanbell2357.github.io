---
layout: page
title: Examples
permalink: /examples/
---

{% for example in site.examples %}
1. [{{ example.title}} {{ example.math}}]({{ example.url }})
{% endfor %}

{% for exercise in site.gm %}
1. [{{ exercise.title}}]({{ exercise.url }})
{% endfor %}


1. [Systems of linear equations](https://jordanbell.info/WebQuiz/wq1.html)

2. [Systems of linear equations](https://jordanbell.info/WebQuiz/wq2.html)

3. [Systems of linear equations](https://jordanbell.info/WebQuiz/wq3.html)