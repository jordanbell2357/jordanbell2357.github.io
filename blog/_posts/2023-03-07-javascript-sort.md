---
layout: post
title: JavaScript sort
---

<button onclick="myFunction1()">Sort Alphabetically</button>
<button onclick="myFunction2()">Sort Numerically</button>

<p id="demo1"></p>

<script>
var points = [40, 100, 1, 5, 25, 10];
document.getElementById("demo1").innerHTML = points;

function myFunction1() {
  points.sort();
  document.getElementById("demo1").innerHTML = points;
}

function myFunction2() {
  points.sort(function(a, b){return a - b});
  document.getElementById("demo1").innerHTML = points;
}
</script>

```javascript
<button onclick="myFunction1()">Sort Alphabetically</button>
<button onclick="myFunction2()">Sort Numerically</button>

<p id="demo"></p>

<script>
var points = [40, 100, 1, 5, 25, 10];
document.getElementById("demo").innerHTML = points;

function myFunction1() {
  points.sort();
  document.getElementById("demo").innerHTML = points;
}

function myFunction2() {
  points.sort(function(a, b){return a - b});
  document.getElementById("demo").innerHTML = points;
}
</script>
```

<h2>JavaScript Array Sort</h2>
<p>The highest number is <span id="demo2"></span>.</p>

<script>
const points = [40, 100, 1, 5, 25, 10];
document.getElementById("demo2").innerHTML = myArrayMax(points);

function myArrayMax(arr) {
  return Math.max.apply(null, arr);
}
</script>

```javacript
<h2>JavaScript Array Sort</h2>
<p>The highest number is <span id="demo"></span>.</p>

<script>
const points = [40, 100, 1, 5, 25, 10];
document.getElementById("demo").innerHTML = myArrayMax(points);

function myArrayMax(arr) {
  return Math.max.apply(null, arr);
}
</script>
```