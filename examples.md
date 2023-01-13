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

## Factors of quadratic polynomials

{% for example in factors %}
1. [{{example.title}} {{example.math}}]({{ example.url }})
{% endfor %}

## Roots of quadratic polynomials

{% for example in roots %}
1. [{{example.title}} {{example.math}}]({{ example.url }})
{% endfor %}

## Vertex form for quadratic polynomials

{% for example in vertex %}
1. [{{example.title}} {{example.math}}]({{ example.url }})
{% endfor %}

## Focus and directrix of parabolas

{% for example in directrix %}
1. [{{example.title}}]({{ example.url }})
{% endfor %}

## Intersections

{% for example in intersections %}
1. [{{example.title}}]({{ example.url }})
{% endfor %}

## Parabolas and reflection

{% for example in focus %}
1. [{{example.title}}]({{ example.url }})
{% endfor %}

## Radius of curvature of parabolas

{% for example in curvature %}
1. [{{example.title}}]({{ example.url }})
{% endfor %}

## Rational expressions

{% for example in rational %}
1. [{{example.title}} {{example.math}}]({{ example.url }})
{% endfor %}

## Desmos

<ul class="spaced_list">
  {% for post in site.categories.desmos %}
    <li>
      <a href="{{ post.url }}">{{ post.title }} \({{ post.math}}\)</a> {{ post.date | date_to_long_string }}
    </li>
  {% endfor %}
</ul>

## GeoGebra

{% for post in site.geogebra %}
1. [{{ post.title}}]({{ post.url }})
{% endfor %}

## WebQuiz

1. [Systems of linear equations](https://jordanbell.info/WebQuiz/wq1.html)

1. [Systems of linear equations](https://jordanbell.info/WebQuiz/wq2.html)

1. [Systems of linear equations](https://jordanbell.info/WebQuiz/wq3.html)

## Graspable Math

{% for exercise in gm %}
1. [{{ exercise.title}}]({{ exercise.url }})
{% endfor %}