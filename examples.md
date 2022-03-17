---
layout: page
title: Examples
permalink: /examples/
---

- [GeoGebra](#geogebra)
- [Desmos](#desmos)
- [Graspable Math](#gm)
- [Step by step solutions](#solutions)
- [WebQuiz](#webquiz)
- [PhET](#phet)

# GeoGebra {#geogebra}

{% for post in site.desmos %}
1. [{{ post.title}} {{ post.math}}]({{ post.url }})
{% endfor %}

# Desmos {#desmos}

{% for post in site.desmos %}
1. [{{ post.title}} {{ post.math}}]({{ post.url }})
{% endfor %}

# Graspable Math {#gm}

{% for exercise in site.gm %}
1. [{{ exercise.title}}]({{ exercise.url }})
{% endfor %}

# Step by step solution {#solutions}

{% for example in site.examples %}
1. [{{ example.title}} {{ example.math}}]({{ example.url }})
{% endfor %}

# WebQuiz {#webquiz}

1. [Systems of linear equations](https://jordanbell.info/WebQuiz/wq1.html)

1. [Systems of linear equations](https://jordanbell.info/WebQuiz/wq2.html)

1. [Systems of linear equations](https://jordanbell.info/WebQuiz/wq3.html)

# PhET {#phet}

{% for exercise in site.phet %}
1. [{{ exercise.title}}]({{ exercise.url }})
{% endfor %}