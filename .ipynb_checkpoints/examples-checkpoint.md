---
layout: page
title: Examples
permalink: /examples/
---

{% assign roots = site.examples | where: "topic", "roots" %}

{% assign vertex = site.examples | where: "topic", "vertex" %}

{% assign directrix = site.examples | where: "topic", "directrix" %}

{% assign focus = site.examples | where: "topic", "focus" %}

{% assign curvature = site.examples | where: "topic", "curvature" %}

{% assign rational = site.examples | where: "topic", "rational" %}

{% assign gm = site.examples | where: "topic", "gm" %}

## WebQuiz

- [Systems of linear equations](https://jordanbell.info/WebQuiz/wq1.html)

- [Systems of linear equations](https://jordanbell.info/WebQuiz/wq2.html)

- [Systems of linear equations](https://jordanbell.info/WebQuiz/wq3.html)


## Rational expressions

{% for example in rational %}
- [{{example.title}} {{example.math}}]({{ example.url }})
{% endfor %}

## Roots of quadratic polynomials

{% for example in roots %}
- [{{example.title}} {{example.math}}]({{ example.url }})
{% endfor %}

## Vertex form for quadratic polynomials

{% for example in vertex %}
- [{{example.title}} {{example.math}}]({{ example.url }})
{% endfor %}

## Focus and directrix of parabolas

{% for example in directrix %}
- [{{example.title}}]({{ example.url }})
{% endfor %}

## Parabolas and reflection

{% for example in focus %}
- [{{example.title}}]({{ example.url }})
{% endfor %}

## Focal length and radius of curvature of parabolas

{% for example in curvature %}
- [{{example.title}}]({{ example.url }})
{% endfor %}

## Graspable Math

{% for exercise in gm %}
- [{{ exercise.title}}]({{ exercise.url }})
{% endfor %}
