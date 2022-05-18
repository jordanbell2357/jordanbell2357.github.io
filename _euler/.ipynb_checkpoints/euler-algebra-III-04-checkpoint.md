---
layout: post
title: Euler, "Elements of Algebra", Section III, Chapter 4
---

### Leonhard Euler, *Elements of Algebra* (*Vollständige Anleitung zur Algebra*)

#### Section III. "Of Ratios and Proportions." Chapter 4. "Of the Summation of Arithmetical Progressions."

**412.** It is often necessary also to find the sum of an
arithmetical progression. This might be done by adding
all the terms together ; but as the addition would be very
tedious, when the progression consisted of a great number
of terms, a rule has been devised, by which the sum may be
more readily obtained.

**413.** We shall first consider a particular given progression,
such that the first term is 2, the difference 3, the last term
29, and the number of terms 10;

<table>
<tbody>
  <tr>
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
    <td>2,</td>
    <td>5,</td>
    <td>8,</td>
    <td>11,</td>
    <td>14,</td>
    <td>17,</td>
    <td>20,</td>
    <td>23,</td>
    <td>26,</td>
    <td>29.</td>
  </tr>
</tbody>
</table>

In this progression we see that the sum of the first and
last term is 31; the sum of the second and the last but one
31; the sum of the third and the last but two 31, and so on:
hence we conclude, that the sum of any two terms equally
distant, the one from the first, and the other from the last
term, is always equal to the sum of the first and the last
term.

**414.** The reason of this may be easily traced; for if we
suppose the first to be $$a$$, the last $$z$$, and the difference $$d$$, the
sum of the first and the last term is $$a+z$$; the second
term being $$a + d$$, and the last but one $$z-d$$, the sum of
these two terms is also $$a+z$$. Farther, the third time being
$$a + 2d$$, and the last but two $$z-2d$$, it is evident that these
two terms also, when added together, make $$a+z$$ and the
demonstration may be easily extended to any other two
terms equally distant from the first and last.

**415.** To determine, therefore, the sum of the progression
proposed, let us write the same progression term by term,
inverted, and add the corresponding terms together, as
follows:

<table>
<tbody>
  <tr>
    <td>2</td>
    <td>+5</td>
    <td>+8</td>
    <td>+11</td>
    <td>+14</td>
    <td>+17</td>
    <td>+20</td>
    <td>+23</td>
    <td>+26</td>
    <td>+29</td>
  </tr>
  <tr>
    <td>29</td>
    <td>+26</td>
    <td>+23</td>
    <td>+20</td>
    <td>+17</td>
    <td>+14</td>
    <td>+11</td>
    <td>+8</td>
    <td>+5</td>
    <td>+2</td>
  </tr>
  <tr>
    <td>31</td>
    <td>31</td>
    <td>31</td>
    <td>31</td>
    <td>31</td>
    <td>31</td>
    <td>31</td>
    <td>31</td>
    <td>31</td>
    <td>31</td>
  </tr>
</tbody>
</table>

This series of equal terms is evidently equal to twice the
sum of the given progression: now, the number of those
equal terms is 10, as in the progression, and their sum consequently is equal to
10·31=310. Hence, as this sum
is twice the sum of the arithmetical progression, the sum required must be 155.

**416.** If we proceed in the same manner with respect to
any arithmetical progression, the first term of which is $$a$$, the
last $$z$$, and the number of terms $$n$$; writing under the given
progression the same progression inverted, and adding term
to term, we shall have a series of $$n$$ terms, each of which will
be expressed hy $$a + z$$; therefore the sum of this series will
be $$n(a+z)$$, which is twice the sum of the proposed arithmetical progression;
the latter, therefore, will be represented by

$$\frac{n(a+z)}{2}.$$

**417.** This result furnishes an easy method of finding the
sum of any arithmetical progression ; and inay be reduced to
the following rule:

Multiply the sum of the first and the last term by the
number of terms, and half the product will be the sum of
the whole progression. Or, which amounts to the same,
multiply the sum of the first and the last term by half the
number of terms. Or, multiply half the sum of the first and
the last term by the whole number of terms.

**418.** It will be necessary to illustrate this rule by some
examples.

First, let it be required to find the sum of the progression
of the natural numbers, 1, 2, 3, etc. to 100. This will be,
by the first rule, $$\frac{100\cdot 101}{2} =\frac{10100}{2}= 5050$$.

If it were required to tell how many strokes a clock strikes
in twelve hours; we must add together the numbers 1, 2, 3,
as far as 12; now this sum is found immediately to be
$$\frac{12\cdot 13}{2} = 6\cdot 13=78$$.
If we wished to know the sum of
the same progression continued to 1000, we should find it to
be 500500; and the sum of this progression, continued to
10000, would be 50005000.

**419.** Suppose a person buys a horse, on condition that for
the first nail he shall pay 5 pence, for the second 8 pence, for
the third 11 pence, and so on, always increasing 3 pence more
for each nail, the whole number of which is 32; required
the purchase of the horse?

In this question it is required to find the sum of an
arithmetical progression, the first term of which is 5, the
difference 3, and the number of terms 32; we must therefore begin
by determining the last term; which is found by
the rule, in *Articles 406* and *411*, to be 5+(31·3)=98;
after which the sum required is easily found to be ^
$$\frac{103\cdot 32}{2}=103\cdot 16$$; whence we conclude that the horse costs 1648
pence, or 6*l.* 17*s.* 4*d.*

**420.** Generally, let the first term be $$a$$, the difference $$d$$,
and the number of terms $$n$$ ; and let it be required to find,
by means of these data, the sum of the whole progression.
As the last term must be $$a + {n - 1)d$$, the sum of the first
and the last will be $$2a + (n-1)d$$; and multiplying this
sum by the number of terms $$n$$, we have $$2na + n(n - l)d$$;
the sum required therefore will be

$$na + \frac{n(n-1)d}{2}.$$


Now, this formula, if applied to the preceding example,
or to $$a = 5$$, $$d = 3$$, and $$n = 32$$, gives

$$5\cdot 32+\frac{32\cdot 31\cdot 3}{2} = 160+1488=1648;$$

the same sum that we
obtained before.

**421.** If it be required to add together all the natural
numbers from 1 to $$n$$, we have, for finding this sum, the first
term 1, the last term $$n$$, and the number of terms $$n$$;
therefore the sum required is $$\frac{n^2+n}{2}=\frac{n(n+1)}{2}$$.
If we make $$n=1766$$, the sum of all the numbers, from 1 to 1766, will
be 883, or half the number of terms, multiplied by 1767, =1560261.

**422.** Let the progression of uneven numbers be proposed,
1, 3, 5, 7, etc. continued to $$n$$ terms, and let the sum of it be
required. Here the first term is 1, the difference 2, the
number of terms $$n$$; the last term will therefore be
$$1+(n-1) 2=2n-1$$,
and consequently the sum required $$=n^2$$.

The whole therefore consists in multiplying the number
of terms by itself; so that whatever number of terms of this
progression we add together, the sum will be always a square,
namely, the square of the number of terms; which we shall
exemplify as follows


#### References

1. Leonhard Euler, *Elements of Algebra*, Translated by Rev. John Hewlett. Longmans, Hurst, Rees, Orme, and Co., London, 1822.
    - [Section III. Chapter 4. "Of the Summation of Arithmetical Progressions."](/assets/euler/en/III-4.pdf)
    - [Archive.org](https://archive.org/details/elementsofalgebr00euleuoft/)
2. Leonhard Euler. *Vollständige Anleitung zur Algebra. Mit den Zusätzen von Joseph Louis Lagrange.* Herausgegeben von Heinrich Weber. B. G. Teubner. Leipzig and Berlin. 1911. Leonhardi Euleri Opera omnia. Series prima. Opera mathematica. Volumen primum.
    - [Erster Theil. Dritter Abschnitt. Capitel 4. Von der Summation der arithmetischen Progressionen](/assets/euler/de/I-III-4.pdf)
    - [Springer](https://link.springer.com/book/9783764314002)
3. Leonhard Euler, *Vollständige Anleitung zur Algebra*, Kayserlichen Akademie der Wissenschaften, St. Petersburg, 1771.
    - [ETH-Bibliothek Zürich](https://doi.org/10.3931/e-rara-9093)