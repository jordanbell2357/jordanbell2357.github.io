---
layout: post
title: Euler, "Elements of Algebra", Section III, Chapter 11
---

### Leonhard Euler, *Elements of Algebra* (*Vollständige Anleitung zur Algebra*)

#### Section III. "Of Ratios and Proportions." Chapter 11. "Of Geometrical Progressions."

**505.** A series of numbers, which are always becoming a
certain number of times greater, or less, is called a **geometrical progression**,
because each term is constantly to the
following one in the same geometrical ratio: and the number
which expresses how many times each term is greater than
the preceding, is called the *exponent*, or *ratio*. Thus, when
the first term is 1 and the exponent, or ratio, is 2, the geometrical progression becomes,

<table>
<tbody>
  <tr>
    <td>Terms</td>
    <td>1</td>
    <td>2</td>
    <td>3</td>
    <td>4</td>
    <td>5</td>
    <td>6</td>
    <td>7</td>
    <td>8</td>
    <td>9</td>
    <td>etc.</td>
  </tr>
  <tr>
    <td>Progression</td>
    <td>1,</td>
    <td>2,</td>
    <td>4,</td>
    <td>8,</td>
    <td>16,</td>
    <td>32,</td>
    <td>64,</td>
    <td>128,</td>
    <td>256,</td>
    <td>etc.</td>
  </tr>
</tbody>
</table>

The numbers 1, 2, 3, etc. always marking the place which
each term holds in the progression.

**506.** If we suppose, in general, the first term to be $$a$$,
and the ratio $$b$$, we have the following geometrical progression

<table>
<tbody>
  <tr>
    <td>Terms</td>
    <td>1</td>
    <td>2</td>
    <td>3</td>
    <td>4</td>
    <td>5</td>
    <td>6</td>
    <td>7</td>
    <td>8</td>
    <td>⋯</td>
    <td>\(n\)</td>
  </tr>
  <tr>
    <td>Progression</td>
    <td>\(a\),</td>
    <td>\(ab\),</td>
    <td>\(ab^2\),</td>
    <td>\(ab^3\),</td>
    <td>\(ab^4\),</td>
    <td>\(ab^5\),</td>
    <td>\(ab^6\),</td>
    <td>\(ab^7\),</td>
    <td>⋯</td>
    <td>\(ab^{n-1}\).</td>
  </tr>
</tbody>
</table>

So that, when this progression consists of $$n$$ terms, the
last term is $$ab^{n-1}$$. We must, however, remark here, that if
the ratio $$b$$$ be greater than unity, the terms increase continually;
if $$b=1$$, the terms are all equal; lastly, if $$b$$ be
less than 1, or a fraction, the terms continually decrease.
Thus, when $$a=1$$, and $$b=\frac{1}{2}$$, we have this geometrical
progression:

1, ½, ¼, ⅛, ¹⁄₁₆, ¹⁄₃₂, ¹⁄₆₄, ¹⁄₁₂₈, etc.

**507.** Here therefore we have to consider:

1. The first term, which we have called $$a$$.
2. The exponent, which we call $$b$$.
3. The number of terms, which we have expressed by $$n$$.
4. And the last term, which, we have already seen, is expressed by $$ab^{n-1}$$.

So that, when the first three of these are given, the last term
is found by multiplying the $$n-1$$ power of $$b$$, or $$b^{n-1}$$,
by the first term $$a$$.

If, therefore, the 50th term of the geometrical progression
1, 2, 4, 8, etc. were required, we should have $$a=1$$, $$b = 2$$,
and $$n=50$$; consequently the 50th term would be $$2^{49}$$; and
as $$2^9$$=512, we shall have $$2^{10}$$=1024; wherefore the square
of $$2^{10}$$, or $$2^{20}$$, =1048576, and the square of this number,
which is 1099511627776=$$2^{40}$$. Multiplying therefore this
value of $$2^{40}$$ by $$2^9$$, or 512, we have $$2^{49}$$ = 562949953421312
for the 50th term.

**508.** One of the principal questions which occurs on this
subject, is to find the sum of all the terms of a geometrical
progression; we shall therefore explain the method of doing
this. Let there be given, first, the following progression,
consisting of ten terms:

1, 2, 4, 8, 16, 32, 64, 128, 256, 512,

the sum of which we shall represent by $$s$$, so that

$$s=1+2+4+8+16+32+64+128+256+512;$$

doubling both sides, we shall have

$$2s=2+4+8+16+32+64+128+256+512+1024;$$

and subtracting from this the progression represented by $$s$$,
there remains $$s=1024-1=1023$$; wherefore the sum
required is 1023.

**509.** Suppose now, in the same progression, that the
number of terms is undetermined, that is, let them be generally represented by $$n$$,
so that the sum in question, or

$$s=1+2+2^2+2^3+2^4+\cdots+2^{n-1}.$$

If we multiply by 2, we have

$$2s=2+2^2+2^3+2^4+\cdots+2^n,$$

then subtracting from this equation the preceding one, we
have $$s=2^n-1-1$$. It is evident, therefore, that the sum required is found,
by multiplying the last term, $$2^{n-1}$$, by the
exponent 2, in order to have $$2^n$$, and subtracting unity from
that product.

**510.** This is made still more evident by the following
examples, in which we substitute successively for $$n$$, the
numbers 1, 2, 3, 4, etc.

1=1;  
1+2=3;  
1+2+4=7;  
1+2+4+8=15;  
1+2+4+8+16=31;  
1+2+4+8+16+32=63,
etc.

**511.** On this subject, the following question is generally
proposed. A man offers to sell his horse on the following
condition ; that is, he demands 1 penny for the first nail, 2
for the second, 4 for the third, 8 for the fourth, and so on,
doubling the price of each succeeding nail. It is required
to find the price of the horse, the nails being 32 in number?

This question is evidently reduced to finding the sum of
all the terms of the geometrical progression 1, 2, 4, 8, 16,
&c. continued to the 32d term. Now, that last term is 2^^
;
and, as we have already found 9r'^ — 1048576, and 2^° =
1024, we shall have 2-" x 2'« = 9?"" = 1073741824; and
multiplying again by 2, the last term S"*^ — 2147483648;
doubling therefore this number, and subtracting unity from
the product, the sum required becomes 4294967295 pence
;
which being reduced, we have 17895697/. 1,?. 3if. for the
price of the horse.


#### References

1. Leonhard Euler, *Elements of Algebra*, Translated by Rev. John Hewlett. Longmans, Hurst, Rees, Orme, and Co., London, 1822.
    - [Section III. Chapter 11. "Of Geometrical Progressions."](/assets/euler/en/III-11.pdf)
    - [Archive.org](https://archive.org/details/elementsofalgebr00euleuoft/)
2. Leonhard Euler. *Vollständige Anleitung zur Algebra. Mit den Zusätzen von Joseph Louis Lagrange.* Herausgegeben von Heinrich Weber. B. G. Teubner. Leipzig and Berlin. 1911. Leonhardi Euleri Opera omnia. Series prima. Opera mathematica. Volumen primum.
    - [Erster Theil. Dritter Abschnitt. Capitel 11. Von den geometrischen Progressionen](/assets/euler/de/I-III-11.pdf)
    - [Springer](https://link.springer.com/book/9783764314002)
3. Leonhard Euler, *Vollständige Anleitung zur Algebra*, Kayserlichen Akademie der Wissenschaften, St. Petersburg, 1771.
    - [ETH-Bibliothek Zürich](https://doi.org/10.3931/e-rara-9093)