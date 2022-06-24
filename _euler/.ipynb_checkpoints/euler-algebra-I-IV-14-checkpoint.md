---
layout: page
title: Chapter 14. "Of the Rule of Bombelli, for reducing the Resolution of Equations of the Fourth Degree to that of Equations of the Third Degree."
part: I
section: IV
chapter: 14
---

### Part {{ page.part }}. Section {{ page.section }}. {{ page.title }}

<span class="art">765</span> We have already shown how equations of the third
degree are resolved by the rule of Cardano; so that the principal object,
with regard to equations of the fourth degree,
is to reduce them to equations of the third degree. For it
is impossible to resolve, generally, equations of the fourth
degree, without the aid of those of the third; since, when
we have determined one of the roots, the others always
depend on an equation of the third degree. And hence
we may conclude, that the resolution of equations of higher
dimensions presupposes the resolution of all equations of lower
degrees.

<span class="art">766</span> It is now some centuries since Bombelli, an Italian,
gave a rule for this purpose, which we shall explain in this
chapter.

Let there be given the general equation of the fourth
degree,

$$x^4+ax^3+bx^2+cx+d=0,$$

in which the letters $$a$$, $$b$$, $$c$$, $$d$$, represent any possible numbers;
and let us suppose that this equation is the same as

$$\left(x^2+\frac{1}{2}ax+p\right)^2 - (qx+r)^2 = 0,$$

in which it is required to determine the letters $$p$$, $$q$$, $$r$$, in order that we may obtain
the equation proposed.
By squaring, and ordering this new equation, we shall have

$$
\begin{array}
x^4&+ax^3&+\frac{1}{4}a^2x^2&+apx&+p^2\\
&&2px^2&-2qrx&-r^2\\
&&-q^2x^2&&
\end{array}
$$

Now, the first two terms are already the same here as in the given equation;
the third term requires us to make

$$\frac{1}{4}a^2+2p-q^2=b,$$

which gives

$$q^2=\frac{1}{4}a^2+2p-b;$$

the fourth term shows that we must make $$ap-2qr=c$$,
or

$$2qr=ap-c;$$

and, lastly, we have for the last term $$p^2-r^2=d$$, or
$$r^2=p^2-d$$. We have therefore three equations which will give
the values of $$p$$, $$q$$, and $$r$$.

<span class="art">767</span> The easiest method of deriving those values from
them is the following: if we take the first equation four
times, we shall have $$4q^2=a^2+8p-4b$$;
which equation, multiplied by the last, $$r^2=p^2-d$$, gives

$$4q^2r^2=8p^3+(a^2-4b)p^2-8dp-d(a^2-4b).$$

Farther, if we square the second equation, we have

$$4q^2r^2=a^2p^2-2acp+c^2.$$

So that we have two values of $$4q^2r^2$$, which, being made equal,
will furnish the equation

$$8p^3+(a^2-4b)p^2-8dp-d(a^2-4b) = a^2p^2-2acp+c^2,$$

or, bringing all the terms to one side, and arranging,

$$8p^3-4bp^2+(2ac-8d)p-a^2d+4bd-c^2=0,$$

an equation of the third degree, which will always give
the value of $$p$$ by the rules already explained.

<span class="art">768</span> Having therefore determined three values of $$p$$ by
the given quantities $$a$$, $$b$$, $$c$$, $$d$$, when it was required to find
only one of those values, we shall also have the values of
the two other letters $$q$$ and $$r$$; for the first equation will
give $$q=\surd\left(\frac{1}{4}a^2+2p-b\right)$$, and the second gives
$$r=\dfrac{ap-c}{2q}$$.
Now, these three values being determined for each given case, the four
roots of the proposed equation may be found in the following manner:

This equation having been reduced to the form

$$\left(x^2+\frac{1}{2}ax+p\right)^2 - (qx+r)^2=0,$$

we shall have

$$\left(x^2+\frac{1}{2}ax+p\right)^2 = (qx+r)^2,$$

and, extracting the root, $$x^2+\frac{1}{2}ax+p=qx+r$$,
or $$x^2+\frac{1}{2}ax+p=-qx-r$$. The first equation gives
$$x^2=\left(q-\frac{1}{2}a\right)x-p+r$$, from which we may
find two roots; and the second equation, to which we may
give the form $$x^2=-\left(q+\frac{1}{2}a\right)x-p-r$$,
will furnish the two other roots.

<span class="art">769</span> 


<span class="art">770</span> 


#### Editions

1. Leonhard Euler. *Elements of Algebra*. Translated by Rev. John Hewlett. Third Edition. Longmans, Hurst, Rees, Orme, and Co. London. 1822.
    - [Part {{ page.part }}. Section {{ page.section }}. {{ page.title }}](/assets/euler/en/IV-14.pdf)
2. Leonhard Euler. *Vollständige Anleitung zur Algebra. Mit den Zusätzen von Joseph Louis Lagrange.* Herausgegeben von Heinrich Weber. B. G. Teubner. Leipzig and Berlin. 1911. Leonhardi Euleri Opera omnia. Series prima. Opera mathematica. Volumen primum.
    - [Zweyter Theil. Erster Abschnitt. Capitel 14. Von des Bombelli Regel die Auflösung der biquadratischen Gleichungen auf cubische zu bringen](/assets/euler/de/II-I-14.pdf)