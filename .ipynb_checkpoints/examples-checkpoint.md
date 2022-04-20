---
layout: page
title: Examples
permalink: /examples/
---

{% assign roots = site.examples | where: "topic", "roots" %}

{% assign factors = site.examples | where: "topic", "factors" %}

{% assign intersections = site.examples | where: "topic", "intersections" %}

{% assign vertex = site.examples | where: "topic", "vertex" %}

{% assign directrix = site.examples | where: "topic", "directrix" %}

{% assign focus = site.examples | where: "topic", "focus" %}

{% assign curvature = site.examples | where: "topic", "curvature" %}

{% assign rational = site.examples | where: "topic", "rational" %}

{% assign gm = site.examples | where: "topic", "gm" %}

{% assign euler = site.examples | where: "topic", "euler" %}

* this unordered seed list will be replaced by toc as unordered list
{:toc}

## Euler, *The Elements of Algebra*

{% for example in euler %}
- [{{example.title}}]({{ example.url }})
{% endfor %}

## Rational expressions

{% for example in rational %}
- [{{example.title}} {{example.math}}]({{ example.url }})
{% endfor %}

## Roots of quadratic polynomials

{% for example in roots %}
- [{{example.title}} {{example.math}}]({{ example.url }})
{% endfor %}

## Factors of quadratic polynomials

{% for example in factors %}
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

## Intersections

{% for example in intersections %}
- [{{example.title}}]({{ example.url }})
{% endfor %}

## Parabolas and reflection

{% for example in focus %}
- [{{example.title}}]({{ example.url }})
{% endfor %}

## Radius of curvature of parabolas

{% for example in curvature %}
- [{{example.title}}]({{ example.url }})
{% endfor %}

## Desmos

{% for post in site.desmos %}
1. [{{ post.title}} {{ post.math}}]({{ post.url }})
{% endfor %}

## GeoGebra

{% for post in site.geogebra %}
1. [{{ post.title}}]({{ post.url }})
{% endfor %}

## WebQuiz

- [Systems of linear equations](https://jordanbell.info/WebQuiz/wq1.html)

- [Systems of linear equations](https://jordanbell.info/WebQuiz/wq2.html)

- [Systems of linear equations](https://jordanbell.info/WebQuiz/wq3.html)

## Graspable Math

{% for exercise in gm %}
- [{{ exercise.title}}]({{ exercise.url }})
{% endfor %}