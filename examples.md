---
layout: page
title: Examples
permalink: /examples/
---

{% assign roots = site.examples | where: "topic", "roots" %}

{% assign vertex = site.examples | where: "topic", "vertex" %}

{% assign directrix = site.examples | where: "topic", "directrix" %}

{% assign focus = site.examples | where: "topic", "focus" %}

{% assign rational = site.examples | where: "topic", "rational" %}

## Roots

{% for example in roots %}
- [{{example.title}} {{example.math}}]({{ example.url }})
{% endfor %}

<!--
{% for example in site.examples %}
- [{{ example.title}} {{ example.math}}]({{ example.url }})
{% endfor %}
-->

## Vertex form

{% for example in vertex %}
- [{{example.title}} {{example.math}}]({{ example.url }})
{% endfor %}

## Focus and directrix

{% for example in directrix %}
- [{{example.title}} {{example.math}}]({{ example.url }})
{% endfor %}

## Focus and center of curvature

{% for example in focus %}
- [{{example.title}}]({{ example.url }})
{% endfor %}

## Rational expressions

{% for example in rational %}
- [{{example.title}} {{example.math}}]({{ example.url }})
{% endfor %}

## GM

{% for exercise in site.gm %}
- [{{ exercise.title}}]({{ exercise.url }})
{% endfor %}


## WebQuiz exercises

- [Systems of linear equations](https://jordanbell.info/WebQuiz/wq1.html)

- [Systems of linear equations](https://jordanbell.info/WebQuiz/wq2.html)

- [Systems of linear equations](https://jordanbell.info/WebQuiz/wq3.html)