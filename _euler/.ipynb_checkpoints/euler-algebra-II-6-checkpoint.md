---
layout: page
title: Chapter 6. "Of the Cases in Integer Numbers, in which the Formula 𝑎𝑥𝑥+𝑏 becomes a Square."
part: II
chapter: 6
---

### Part {{ page.part}}. {{ page.title }}

<span class="art">79</span> We have already shwn, <span class="artref">Art. 63</span>, how such formulae
as $$a+bx+cx^2$$ are to be transformed, in order that the
second term may be destroyed  we shall therefore confine
our present inquiries to the formula $$ax^2 + b$$, in which it is
required to find for $$x$$ only integer numbers, which may
transform that formula into a square. Now, first of all,
such a formula must be possible; for, if it be not, we shall
not even obtain fractional values of $$x$$, far less integer ones.

<span class="art">80</span> Let us suppose then $$ax^2+b=y^2$$; $$a$$ and $$b$$ being
integer numbers, as well as $$x$$ and $$y$$.

Now, here it is absolutely necessary for us to know, or to
have already found a case in integer numbers; otherwise it
would be lost labor to seek for other similar cases, as the
formula might happen to be impossible.

We shall, therefore, suppose that this formula becomes a
square, by making $$x-f$$, and we shall represent that square
by $$g^2$$, so that $$af^2+b=g^2$$, where $$f$$ and $$g$$ are known
numbers. Then we have only to deduce from this case other similar
cases; and this inquiry is so much the more important,
as it is subject to considerable difficulties; which,
however, we shall be able to surmount by particular artifices.

<span class="art">81</span> Since we have already found $$af^2+b=g^2$$,
and likewise, by hypothesis, $$ax^2+b=y^2$$,
let us subtract the first
equation from the second, and we shall obtain a new one,
$$ax^2-af^2=y^2-g^2$$, which may be represented by factors
in the following manner;

$$a(x+f)\cdot(x-f) = (y+g)\cdot (y-g),$$

and which, by multiplying both sides by $$pq$$, becomes

$$apq(x+f)\cdot(x-f)=pq(y+g)\cdot(y-g).$$

If we now decompound this equation, by making $$ap(x+f)=q(y+g)$$,
and $$q(x-f) = p(y-g)$$, we may derive, from
these two equations, values of the two letters $$x$$ and $$y$$. The
first, divided by $$q$$, gives $$y+g = \dfrac{apx+apf}{q}$$;
and the second, divided by $$p$$, gives $$y-g = \dfrac{qx-qf}{p}$$.
Subtracting this
latter equation from the former, we have

$$2g = \dfrac{(ap^2-q^2)x+(ap^2+q^2)f}{pq},$$

or

$$2gpq = (ap^2-q^2)x+(ap^2+q^2)f;$$

therefore

$$x=\dfrac{2gpq}{ap^2-q^2} - \dfrac{(ap^2+q^2)f}{ap^2-q^2},$$

from which we obtain

$$y=g+\dfrac{2gq^2}{ap^2-q^2} - \dfrac{(ap^2+q^2)fq}{(ap^2-q^2)p} - \dfrac{qf}{p}.$$

And as, in this latter value, the first two terms, both containing the letter $$g$$,
may be put into the form $$\dfrac{g(ap^2+q^2)}{ap^2-q^2}$$, and as the other two,
containing the letter $$f$$, may be expressed by $$\dfrac{2afpq}{ap^2-q^2}$$,
all the
terms will be reduced to the same denomination, and we
shall have

$$y=\dfrac{g(ap^2+q^2)-2afpq}{ap^2-q^2}.$$

<span class="art">82</span> This operation seems not, at first, to answer our purpose;
since having to find integer values of $$x$$ and $$y$$, we are
brought to fractional results; and it would be required to
solve this new question, - What numbers are we to substitute
for $$p$$ and $$q$$, in order that the fraction may disappear? A
question apparently still more difficult than our original one:
but here we may employ a particular artifice, that will
readily bring us to our object, which is as follows:

As every thing must be expressed in integer numbers, let
us make $$\dfrac{ap^2+q^2}{ap^2-q^2}=m$$, and $$\dfrac{2pq}{ap^2-q^2}=n$$,
in order that we may have $$x=ng-mf$$, and $$y=mg-naf$$.

Now, we cannot here assume $$m$$ and $$n$$ at pleasure, since
these letters must be such as will answer to what has been
already determined: therefore, for this purpose, let us consider their squares, and we shall find

$$m^2=\dfrac{a^2p^4+2ap^2q^2+q^4}{a^2p^4-2ap^2q^2+q^4},$$

and

$$n^2=\dfrac{4p^2q^2}{a^2p^4-2ap^2q^2+q^4};$$

and hence

$$
\begin{align}
m^2-an^2&=\dfrac{a^2p^4+2ap^2q^2+q^4-4ap^2q^2}{a^2p^4-2ap^2q^2+q^4}\\
&=\dfrac{a^2p^4-2ap^2q^2+q^4}{a^2p^4-2ap^2q^2+q^4}\\
&=1.
\end{align}
$$

<span class="art">83</span> We see, therefore, that tlie two numbers $$m$$ and $$n$$
must be such, that $$m^2=an^2+1$$. So that, as $$a$$ is a known
number, we must begin by considering the means of determining such an integer number for $$n$$,
as will make
$$an^2+1$$ a square; for then $$m$$ will be the root of that square;
and when we have likewise determined the number $$f$$ so,
that $$af^2+b$$ may become a square, namely $$g^2$$ we shall obtain for $$x$$ and $$y$$
the following values in integer numbers;

$$x=ng-mf,\qquad y =mg-naf;$$

and thence, lastly, $$ax^2+b=y^2$$.

<span class="art">84</span>



<span class="art">85</span>



<span class="art">86</span>

#### Editions

1. Leonhard Euler. *Elements of Algebra*. Translated by Rev. John Hewlett. Third Edition. Longmans, Hurst, Rees, Orme, and Co. London. 1822.
    - [Part {{ page.part}}. {{ page.title }}](/assets/euler/en/pt-II-6.pdf)
2. Leonhard Euler. *Vollständige Anleitung zur Algebra. Mit den Zusätzen von Joseph Louis Lagrange.* Herausgegeben von Heinrich Weber. B. G. Teubner. Leipzig and Berlin. 1911. Leonhardi Euleri Opera omnia. Series prima. Opera mathematica. Volumen primum.
    - [Zweyter Theil. Zweyter Abschnitt. Capitel 6. Von den Fällen in gantzen Zahlen, da die Formel $$axx + b$$ ein Quadrat wird](/assets/euler/de/II-II-6.pdf)