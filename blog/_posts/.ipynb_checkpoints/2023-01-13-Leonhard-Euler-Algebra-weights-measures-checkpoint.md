---
layout: post
title: Weights and measures in Leonhard Euler's Algebra
---

> My transcription of Leonhard Euler. *Elements of Algebra*. Translated by Rev. John Hewlett. Third Edition. Longmans, Hurst, Rees, Orme, and Co. London. 1822. [Part II. Chapter 2. “Of the Rule which is called Regula Coeci, for determining, by means of two Equations, three or more Unknown Quantities.”](/assets/euler/en/pt-II-2.pdf)

---

<span class="art">28</span> Goldsmiths and coiners make great use of this rule,
when they propose to make, from three or more kinds of
metal, a mixture of a given value, as the following example
will show.

*Question 3.* A coiner has three kinds of silver, the first of 14 loth fineness, the second of 11 loth fineness,
the third of 9 loth fineness. Now he wishes to form a mixture of them
weighing 30 Marks, of 12 loth fineness: how many Marks of each sort must he take?

<blockquote>
Ein Müntz-Meister hat dreyerley Silber, das erste ist 14löthig,
das andere 11löthig, das dritte 9löthig. Nun soll er eine Maße 30 Marck
schwer machen, welche 12löthig seyn soll, wie viel Marck muß er von jeder
Sorte nehmen?
</blockquote>

<div class="bubblebox">
<p>
A mixture containing silver has 14 loth fineness if ¹⁴⁄₁₆ of its mass is silver (= 875 millesimal fineness), 11 loth fineness if ¹¹⁄₁₆ of its mass is silver (= 782.5 millesimal fineness), and 9 loth fineness if ⁹⁄₁₆ of its mass is silver (= 562.5 millesimal fineness). Fine or pure silver has 16 loth fineness (= 999 millesimal fineness).
</p>
<p>
„LÖTHIG, adj.“, <em>Deutsches Wörterbuch von Jacob Grimm und Wilhelm Grimm</em>, digitalisierte Fassung im <em>Wörterbuchnetz des Trier Center for Digital Humanities, Version 01/21</em>, <a href="https://www.woerterbuchnetz.de/DWB?lemid=L06923">https://www.woerterbuchnetz.de/DWB?lemid=L06923</a>, abgerufen am 19.06.2022.
</p>
<p>
<a href="https://www.ascasonline.org/articoloOTTOB234.html">Giorgio Busetto. "Silver Fineness Marks". Article &#35;234. Association of Small Collectors of Antique Silver - ASCAS. 2018</a>
</p>
</div>

<blockquote>
Da ferner ein Marck von der ersten Sorte 14 Loth fein Silber hält, so werden die 𝑥 Marck enthalten 14𝑥 Loth Silber; eben so werden die 𝑦 Marck von der zweyten Sorte enthalten 11𝑦 Loth; und die 𝑧 Marck von der dritten Sorte werden enthalten 9𝑧 Loth Silber; dahero die gantze Maße an Silber enthalten wird 14𝑥+11𝑦+9𝑧 Loth. 
</blockquote>

<div class="bubblebox">
<table>
<tr>
    <td>1 Mark = 8 ounces</td>
    <td>1 ounce = ⅛ Mark</td>
</tr>
<tr>
    <td>1 Mark = 16 Loths</td>
    <td>1 Loth = ¹⁄₁₆ Mark</td>
</tr>
<tr>
    <td>1 ounce = 2 Loths</td>
    <td>1 Loth = ½ ounce</td>
</tr>
</table>

<p>
„LOTH, n.“, <em>Deutsches Wörterbuch von Jacob Grimm und Wilhelm Grimm</em>, digitalisierte Fassung im <em>Wörterbuchnetz des Trier Center for Digital Humanities, Version 01/21</em>, <a href="https://www.woerterbuchnetz.de/DWB?lemid=L06903" title="„LOTH, n.“ Deutsches Wörterbuch von Jacob Grimm und Wilhelm Grimm">https://www.woerterbuchnetz.de/DWB?lemid=L06903</a>, abgerufen am 19.06.2022.
</p>

<p>
<a href="https://ikmk.smb.museum/object?id=18201786" title="1 Mark weight. Staatlichen Museen zu Berlin">Münzkabinett der Staatlichen Museen zu Berlin. Object number 18201786. "KBA / 65536 / 1 / MARCK"</a>
</p>
</div>

> Kölner Mark, 233.97 g. Münzkabinett der Staatlichen Museen zu Berlin, 18201786 <https://ikmk.smb.museum/object?id=18201786>
> 
> [![Image files are licensed Public Domain Mark 1.0. Münzkabinett der Staatlichen Museen zu Berlin, 18201786. Photographs by Reinhard Saczewski.](/assets/images/DE-MUS-814819-18201786-av.png)](https://ikmk.smb.museum/object?id=18201786)

If he take 𝑥 Marks of the first kind, 𝑦 Marks of the second,
and 𝑧 Marks of the third, he will have 𝑥+𝑦+𝑧=30,
which is the first equation.

Then, since a Mark of the first sort contains 14 Loths of
fine silver, the 𝑥 Marks of this sort will contain 14𝑥 Loths of
such silver. Also, the 𝑦 Marks of the second sort will contain 11𝑦 Loths,
and the 𝑧 Marks of the third sort will contain 9𝑧 Loths of fine silver; so that the whole mass will
contain 14𝑥+11𝑦+9𝑧 Loths of fine silver.

As this mixture is to weigh 30 Marks, and each of these Marks must
contain 12 Loths of fine silver, it follows that the whole mass
will contain 360 Loths of fine silver; and thence results the
second equation, 

14x+11𝑦+9𝑧=360.

If we now subtract from this equation nine
times the first, or 9𝑥+9𝑦+9𝑧=270, there remains 5𝑥+2𝑦=90,
an equation which must give the values of 𝑥 and 𝑦 in integer numbers;
and with regard to the value of 𝑧, we may derive it from the first
equation 𝑧=30-𝑥-𝑦. Now, the former equation gives 2y=90-5𝑥, and
$$y=45-\dfrac{5x}{2}$$; therefore, if 𝑥=2𝑢, we shall have

𝑦=45-5𝑢, and 𝑧=3𝑢-15;

which shows that 𝑢 must be greater than 4, and yet less than 10. Consequently,
the question admits of the following solutions:

$$
\begin{array}{lllllll}
\textrm{If}&u=&5&6&7&8&9\\ \hline
\textrm{Then}&x=&10&12&14&16&18\\
&y=&20&15&10&5&0\\
&z=&0&3&6&9&12
\end{array}
$$



---

```bash
convert DE-MUS-814819-18201786-av.jpg -resize 400x400^ DE-MUS-814819-18201786-av.png
```

[Command-line Basics: Resizing Images with ImageMagick \| DigitalOcean](https://www.digitalocean.com/community/tutorials/workflow-resizing-images-with-imagemagick)

#### Editions

1. Leonhard Euler. *Elements of Algebra*. Translated by Rev. John Hewlett. Third Edition. Longmans, Hurst, Rees, Orme, and Co. London. 1822.
    - [Part II. Chapter 2. "Of the Rule which is called Regula Coeci, for determining, by means of two Equations, three or more Unknown Quantities."](/assets/euler/en/pt-II-2.pdf)
2. Leonhard Euler. *Vollständige Anleitung zur Algebra. Mit den Zusätzen von Joseph Louis Lagrange.* Herausgegeben von Heinrich Weber. B. G. Teubner. Leipzig and Berlin. 1911. Leonhardi Euleri Opera omnia. Series prima. Opera mathematica. Volumen primum.
    - [Zweyter Theil. Zweyter Abschnitt. Capitel 2. Von der sogenannten Regula-Coeci, wo aus zwey Gleichungen drey oder mehr unbekannte Zahlen bestimmt werden sollen](/assets/euler/de/II-II-2.pdf)