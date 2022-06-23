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
of 14 loth fineness, the second of 11 loth fineness, the third of 9 loth fineness.
Now he wishes to form a mixture of them
weighing 30 Marks, of 12 loth fineness: how many Marks of each
sort must he take?

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
Da ferner ein Marck von der ersten Sorte 14 Loth fein Silber hält, so werden die \(x\) Marck enthalten \(14x\) Loth Silber; eben so werden die \(y\) Marck von der zweyten Sorte enthalten 11\(y\) Loth; und die \(z\) Marck von der dritten Sorte werden enthalten 9\(z\) Loth Silber; dahero die gantze Maße an Silber enthalten wird 14\(x\) + 11\(y\) + 9\(z\) Loth. 
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

<cite>
„LOTH, n.“, <em>Deutsches Wörterbuch von Jacob Grimm und Wilhelm Grimm</em>, digitalisierte Fassung im <em>Wörterbuchnetz des Trier Center for Digital Humanities, Version 01/21</em>, <a href="https://www.woerterbuchnetz.de/DWB?lemid=L06903" title="„LOTH, n.“ Deutsches Wörterbuch von Jacob Grimm und Wilhelm Grimm">https://www.woerterbuchnetz.de/DWB?lemid=L06903</a>, abgerufen am 19.06.2022.
</cite>

<cite>
<a href="https://ikmk.smb.museum/object?id=18201786" title="1 Mark weight. Staatlichen Museen zu Berlin">Münzkabinett der Staatlichen Museen zu Berlin. Object number 18201786. "KBA / 65536 / 1 / MARCK"</a>
</cite>
</div>

If he take $$x$$ Marks of the first kind, $$y$$ Marks of the second,
and $$z$$ Marks of the third, he will have $$x + y + z = 30$$,
which is the first equation.

Then, since a Mark of the first sort contains 14 Loths of
fine silver, the $$x$$ Marks of this sort will contain 14$$x$$ Loths of
such silver. Also, the $$y$$ Marks of the second sort will contain 11$$y$$ Loths,
and the $$z$$ Marks of the third sort will contain 9$$z$$ Loths of fine silver; so that the whole mass will
contain $$14x+11y+9z$$ Loths of fine silver.

As this
mixture is to weigh 30 Marks, and each of these Marks must
contain 12 Loths of fine silver, it follows that the whole mass
will contain 360 Loths of fine silver; and thence results the
second equation, 

$$14x+11y+9z=360.$$

If we now subtract from this equation nine
times the first, or $$9x+9y+9z=270$$, there remains $$5x+2y=90$$,
an equation which must give the values of $$x$$ and $$y$$ in integer numbers;
and with regard to the value of $$z$$, we may derive it from the first
equation $$z=30-x-y$$. Now, the former equation gives $$2y=90-5x$$, and
$$y=45-\dfrac{5x}{2}$$; therefore, if $$x=2u$$, we shall have

$$y=45-5u,\quad \textrm{and} \quad z=3u-15;$$

which shows that $$u$$ must be greater than 4, and yet less than 10. Consequently,
the question admits of the following solutions:

$$
\begin{array}{lllllll}
\textrm{If}&u=&5&6&7&8&9\\ \hline
\textrm{Then}&x=&10&12&14&16&18\\
&y=&20&15&10&5&0\\
&z=&0&3&6&9&12
\end{array}
$$

<span class="art">29</span> Questions sometimes occur, containing more than three
unknown quantities; but they are also resolved in the same
manner, as the following example will show.

*Question 4.* A person buys 100 head of livestock for 100
Reichsthalers, oxen at 10 Reichsthalers each, cows at 5 Reichsthalers,
calves at 2 Reichsthalers, and sheep at ½ Reichsthaler each. How
many oxen, cows, calves, and sheep, did he buy?

Let the number of oxen he $$p$$, that of the cows $$q$$, of calves
$$r$$, and of sheep $$s$$. Then we have the following equations:

1. $$p+q+r+s=100$$
2. $$10p+5q+2r+\frac{1}{2}s=100,$$

or, removing the fractions, 20$$p$$ + 10$$q$$ + 4$$r$$ = 200:
then subtracting the first equation from this, there remains
19$$p$$ + 9$$q$$ + 3$$r$$ = 100; whence

$$
\begin{gather}
3r=100-19p-9q\\
r=33+\frac{1}{3}-6p-\frac{1}{3}p-3q\\
r=33-6p-3q+\dfrac{1-p}{3};
\end{gather}
$$

whence $$1-p$$, or $$p-1$$, must be divisible by 3; therefore if we make
$$p-1=3t$$, we have

$$
\begin{gather}
p=3t+1\\
q=q\\
r=27-19t-3q\\
s=72+2q+16t;
\end{gather}
$$

whence it follows, that 19$$t$$ + 3$$q$$ must be less than 27, and
that, provided this condition be observed, we may give any
value to $$q$$ and $$t$$. We have therefore to consider the following cases:

<table>
<tr>
<th>1. If \(t\) = 0</th>
<th>2. If \(t\) = 1</th>
</tr>
<tr>
<td>we have \(p=1\),</td>
<td>we have \(p=4\),</td>
</tr>
<tr>
<td>\(q=q\),</td>
<td>\(q=q\),</td>
</tr>
<tr>
<td>\(r=27-3q\),</td>
<td>\(r=8-3q\),</td>
</tr>
<tr>
<td>\(s=72+2q\).</td>
<td>\(s=88+2q\)</td>
</tr>
</table>

We cannot make $$t=2$$, because $$r$$ would then become negative.

Now, in the first case, $$q$$ cannot exceed 9; and, in the
second, it cannot exceed 2; so that these two cases give
the following solutions, the first giving the following ten
answers:

<table>
<tr>
<th></th>
<th>1</th>
<th>2</th>
<th>3</th>
<th>4</th>
<th>5</th>
<th>6</th>
<th>7</th>
<th>8</th>
<th>9</th>
<th>10</th>
</tr>
<tr>
<td>\(p\) =</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td>\(q\) =</td>
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
</tr>
<tr>
<td>\(r\) =</td>
<td>27</td>
<td>24</td>
<td>21</td>
<td>18</td>
<td>15</td>
<td>12</td>
<td>9</td>
<td>6</td>
<td>3</td>
<td>0</td>
</tr>
<tr>
<td>\(r\) =</td>
<td>72</td>
<td>74</td>
<td>76</td>
<td>78</td>
<td>80</td>
<td>82</td>
<td>84</td>
<td>86</td>
<td>89</td>
<td>92</td>
</tr>
</table>

And the second furnishes the three following answers:

<table>
<tr>
<th></th>
<th>1</th>
<th>2</th>
<th>3</th>
</tr>
<tr>
<td>\(p\) =</td>
<td>4</td>
<td>4</td>
<td>4</td>
</tr>
<tr>
<td>\(q\) =</td>
<td>0</td>
<td>1</td>
<td>2</td>
</tr>
<tr>
<td>\(r\) =</td>
<td>8</td>
<td>5</td>
<td>2</td>
</tr>
<tr>
<td>\(s\) =</td>
<td>88</td>
<td>90</td>
<td>92</td>
</tr>
</table>

There are, therefore, in all, thirteen answers, which are reduced to ten if we exclude those that
contain zero, or 0.

<span class="art">30</span> The method would still be the same, even if the letters
in the first equation were multiplied by given numbers, as
will be seen from the following example.

*Question 5.* To find three such integer numbers, that if
the first be multiplied by 3, the second by 5, and the third
by 7, the sum of the products may be 560;
and if we multiply the first by 9, the second by 25, and the third by 49,
the sum of the products may be 2920.

If the first number be $$x$$, the second $$y$$, and the third $$z$$, we shall have the two equations,

1. $$3x+5y+7z=560$$
2. $$9x+25y+49z=2920.$$

And here, if we subtract three times the first, or
$$9x+15y+21z=1680$$, from the second, there remains
$$10y+28z=1240$$; dividing by 2, we have $$5y+14z=620$$; whence
we obtain $$y=124-\dfrac{14z}{5}$$: so that $$z$$ must be divisible
by 5. If therefore we make $$z=5u$$, we shall have $$y=124-14u$$; which values
of $$y$$ and $$z$$ being substituted in the first equation, we have
$$3x-35u+620=560$$; or $$3x-35u-60$$, and $$x=\dfrac{35u}{3}-20$$; therefore we
shall make $$u=3t$$, from which we obtain the following answer,
$$x=35t-20$$, $$y=124-42t$$, and $$z=15t$$, in which we must substitute
for $$t$$ an integer number greater than 0 and less than 3: so that
we are limited to the two following answers:

1. If $$t=1$$, we have $$x=15$$, $$y=82$$, $$z=15$$.
2. If $$t=2$$, we have $$x=50$$, $$y=40$$, $$z=30$$.
    
#### Editions

1. Leonhard Euler. *Elements of Algebra*. Translated by Rev. John Hewlett. Third Edition. Longmans, Hurst, Rees, Orme, and Co. London. 1822.
    - [Part {{ page.part}}. {{ page.title }}](/assets/euler/en/pt-II-2.pdf)
2. Leonhard Euler. *Vollständige Anleitung zur Algebra. Mit den Zusätzen von Joseph Louis Lagrange.* Herausgegeben von Heinrich Weber. B. G. Teubner. Leipzig and Berlin. 1911. Leonhardi Euleri Opera omnia. Series prima. Opera mathematica. Volumen primum.
    - [Zweyter Theil. Zweyter Abschnitt. Capitel 2. Von der sogenannten Regula-Coeci, wo aus zwey Gleichungen drey oder mehr unbekannte Zahlen bestimmt werden sollen](/assets/euler/de/II-II-2.pdf)