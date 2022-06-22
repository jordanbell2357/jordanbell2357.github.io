---
layout: page
title: Chapter 2. "Of the Rule which is called Regula Coeci, for determining, by means of two Equations, three or more Unknown Quantities."
part: II
chapter: 2
---

### Part {{ page.part}}. {{ page.title }}

<span class="art">24</span> In the preceding chapter, we have seen how, by means
of a single equation, two unknown quantities may be determined,
so far as to express them in integer and positive
numbers. If, therefore, we had two equations, in order that
the question may be indeterminate, those equations must
contain more than two unknown quantities. Questions of
this kind occur in the common books of arithmetic; and are
resolved by the rule called **Regula Coeci**, or **The Rule of False Position**;
the foundation of which we shall now explain, beginning with the following example:

<span class="art">25</span> *Question 1.* Thirty persons, men, wbmen, and children, spend 50 crowns in a tavern;
the share of a man is 3 crowns, that of a woman 2 crowns, and that of a child is 1
crown; how many persons were there of each class?

If the number of men be $$p$$, of women $$q$$, and of children $$r$$,
we shall have the two following equations;

1. $$p+q+r=30$$, and
2. $$3p+2q+r=50$$,

from which it is required to find the value of the three letters $$p$$, $$q$$,
$$r$$, in integer and positive numbers. The first equation gives
$$r=30-p-q$$; whence we immediately conclude that $$p+q$$ must be less than 30;
and, substituting this value of $$r$$ in the second equation, we have
$$2p+q+30=50$$; so that $$q=20-2p$$, and $$p+q=20-p$$, which evidently is
also less than 30. Now, as we may, in this equation, assume all numbers for $$p$$
which do not exceed 10, we shall have the following eleven answers:
the number of men $$p$$, of women $$q$$, and of children $$r$$, being as follows:

<table>
<tr>
<td>\(p\) = </td>
<td>0</td>
<td>1</td>
<td>2</td>
<td>3</td>
<td>4</td>
<td>5</td>
<td>6</td>
<td>7</td>
<td>8</td>
<td>9</td>
<td>10</td>
</tr>
<tr>
<td>\(q\) =</td>
<td>20</td>
<td>18</td>
<td>16</td>
<td>14</td>
<td>12</td>
<td>10</td>
<td>8</td>
<td>6</td>
<td>4</td>
<td>2</td>
<td>0</td>
</tr>
<tr>
<td>\(r\) =</td>
<td>10</td>
<td>11</td>
<td>12</td>
<td>13</td>
<td>14</td>
<td>15</td>
<td>16</td>
<td>17</td>
<td>18</td>
<td>19</td>
<td>20</td>
</tr>
</table>

and, if we omit the first and the last, there will remain 9.

<span class="art">26</span> *Question 2.* A certain person buys hogs, goats, and sheep, to the number of 100, for 100 crowns;
the hogs cost him 3½ crowns apiece; the goats, 1⅓ crown; and the sheep, ½ a crown. How many had he of each?

Let the number of hogs be $$p$$, that of the goats $$q$$, and of
the sheep $$r$$, then we shall have the two following equations:

1. $$p$$ + $$q$$ + $$r$$ = 100,
2. 3½$$p$$ + 1⅓$$q$$ + ½$$r$$ = 100;

the latter of which being multiplied by 6, in order to remove
the fractions, becomes $$21p+8q+3r=600$$.
Now, the first gives $$r=100-p-q$$; and if we substitute this value of $$r$$ in the second,
we have $$18p+5q=300$$, or $$5q=300-18p$$, and $$q=60-\dfrac{18p}{5}$$: consequently,
$$18p$$ must be divisible by 5, and therefore, as 18 is not divisible by 5, $$p$$ must contain
5 as a factor. If we therefore make $$p=5s$$, we obtain $$q=60-18s$$, and $$r=13s+40$$;
in which we may assume for the value of $$s$$ any integer number
whatever, provided it be such, that $$q$$ does not become negative: but this condition
limits the value of $$s$$ to 3; so that
if we also exclude 0, there can only be three answers to the
question; which are as follow:

<table>
<tr>
<td class="underline">When \(s\) =</td>
<td class="underline">1</td>
<td class="underline">2</td>
<td class="underline">3</td>
</tr>
<tr>
<td>We have \(p\) =</td>
<td>5</td>
<td>10</td>
<td>15</td>
</tr>
<tr>
<td>and \(q\) =</td>
<td>42</td>
<td>24</td>
<td>6</td>
</tr>
<tr>
<td>and \(r\) =</td>
<td>53</td>
<td>66</td>
<td>79</td>
</tr>
</table>

<span class="art">27</span> In forming such examples for practice, we must take
particular care that they may be possible; in order to which,
we must observe the following particulars:

Let us represent the two equations, to which we were just
now brought, by

1. $$x+y+z=a$$, and
2. $$fx+gy+hz=b$$,

in which $$f$$, $$g$$, and $$h$$, as well as $$a$$ and $$b$$, are given numbers.
Now, if we suppose that among the numbers $$f$$, $$g$$, and $$h$$,
the first, $$f$$, is the greatest, and $$h$$ the least, since we have
$$fx+fy+fz=fa$$, or $$(x+y+z)f=fa$$ (because $$x+y+z=a$$),
it is evident that $$fx+fy+fz$$ is greater than $$fx+gy+hz$$;
consequently, $$fa$$ must be greater than $$b$$, or $$b$$ must be less
than $$fa$$. Farther, since $$hx+hy+hz=ha$$, or $$(x+y+z)h=ha$$,
and $$hx+hy+hz$$ is undoubtedly less than $$fx+gy+hz$$, $$ha$$ must be
less than $$b$$, or $$b$$ must be greater than $$ha$$. Hence
it follows, that if $$h$$ be not less than $$fa$$, and also greater than
$$ha$$, the question will be impossible: which condition is also
expressed, by saying that $$h$$ must be contained between the
limits $$fa$$ and $$ha$$; and care must also be taken that it may
not approach either limit too nearly, as that would render it
impossible to determine the other letters.

<span class="art">28</span> Goldsmiths and coiners make great use of this rule,
when they propose to make, from three or more kinds of
metal, a mixture of a given value, as the following example
will show.

*Question 3.* A coiner has three kinds of silver, the first
of 14 lot fineness, the second of 11 lot fineness, the third of 9 lot fineness.
Now he wishes to form a mixture of them
weighing 30 Marks, of 12 lot fineness: how many Marks of each
sort must he take?

<blockquote>
Ein Müntz-Meister hat dreyerley Silber, das erste ist 14löthig,
das andere 11löthig, das dritte 9löthig. Nun soll er eine Maße 30 Marck
schwer machen, welche 12löthig seyn soll, wie viel Marck muß er von jeder
Sorte nehmen?
</blockquote>

<div class="bubblebox">
<p>
A mixture containing silver has 14 lot fineness if ¹⁴⁄₁₆ of its mass is silver (= 875 millesimal fineness), 11 lot fineness if ¹¹⁄₁₆ of its mass is silver (= 782.5 millesimal fineness), and 9 lot fineness if ⁹⁄₁₆ of its mass is silver (= 562.5 millesimal fineness). Fine or pure silver has 16 lot fineness (= 999 millesimal fineness).
</p>
<p>
„LÖTHIG, adj.“, <em>Deutsches Wörterbuch von Jacob Grimm und Wilhelm Grimm</em>, digitalisierte Fassung im <em>Wörterbuchnetz des Trier Center for Digital Humanities, Version 01/21</em>, <a href="https://www.woerterbuchnetz.de/DWB?lemid=L06923">https://www.woerterbuchnetz.de/DWB?lemid=L06923</a>, abgerufen am 19.06.2022.
</p>
<p>
<a href="https://www.ascasonline.org/articoloOTTOB234.html">Giorgio Busetto. "Silver Fineness Marks". Article &#35; 234. Association of Small Collectors of Antique Silver - ASCAS. 2018</a>
</p>
</div>

<blockquote>
Da ferner ein Marck von der ersten Sorte 14 Loth fein Silber hält, so werden die \(x\) Marck enthalten \(14x\) Loth Silber; eben so werden die \(y\) Marck von der zweyten Sorte enthalten 11\(y\) Loth; und die \(z\) Marck von der dritten Sorte werden enthalten 9\(z\) Loth Silber; dahero die gantze Maße an Silber enthalten wird 14\(x\) + 11\(y\) + 9\(z\) Loth. 
</blockquote>
    
- 1 Mark = 8 ounces; 1 ounce = ⅛ Mark.1

- [Münzkabinett der Staatlichen Museen zu Berlin. Object number 18201786. "KBA / 65536 / 1 / MARCK"](https://ikmk.smb.museum/object?id=18201786)

- 1 Mark = 16 Lots; 1 Lot = ¹⁄₁₆ Mark. 1 ounce = 2 Lots; 1 Lot = ½ ounce.

- „LOTH, n.“, *Deutsches Wörterbuch von Jacob Grimm und Wilhelm Grimm*, digitalisierte Fassung im *Wörterbuchnetz des Trier Center for Digital Humanities, Version 01/21*, <https://www.woerterbuchnetz.de/DWB?lemid=L06903>, abgerufen am 19.06.2022.




<span class="art">28</span>



<span class="art">29</span>



<span class="art">30</span>


    
#### Editions

1. Leonhard Euler. *Elements of Algebra*. Translated by Rev. John Hewlett. Third Edition. Longmans, Hurst, Rees, Orme, and Co. London. 1822.
    - [Part {{ page.part}}. {{ page.title }}](/assets/euler/en/pt-II-2.pdf)
2. Leonhard Euler. *Vollständige Anleitung zur Algebra. Mit den Zusätzen von Joseph Louis Lagrange.* Herausgegeben von Heinrich Weber. B. G. Teubner. Leipzig and Berlin. 1911. Leonhardi Euleri Opera omnia. Series prima. Opera mathematica. Volumen primum.
    - [Zweyter Theil. Zweyter Abschnitt. Capitel 2. Von der sogenannten Regula-Coeci, wo aus zwey Gleichungen drey oder mehr unbekannte Zahlen bestimmt werden sollen](/assets/euler/de/II-II-2.pdf)