---
layout: page
title: Chapter 7. "Of a particular Method, by which the Formula 𝑎𝑛𝑛+1 becomes a Square in Integers."
part: II
chapter: 7
---

### Part {{ page.part}}. {{ page.title }}

<span class="art">96</span> That which has been taught in the last chapter, cannot be completely performed, unless we are able to assign for
any number $$a$$, a number $$n$$, such that $$an^2+1$$ may become a square; or that we may have
$$m^2=an^2+1$$.

This equation would be easy to resolve, if we were satisfied with fractional numbers, since we should have only to
make $$m=1+\dfrac{np}{q}$$; for, by this supposition, we have

$$m^2=1+\dfrac{2np}{q}+\dfrac{n^2p^2}{q^2} = an^2+1;$$

in which equation, we
may expunge 1 from both sides, and divide the other terms
by $$n$$: then multiplying by $$q^2$$, we obtain $$2pq+np^2=anq^2$$;
and this equation, giving $$n=\dfrac{2pq}{aq^2-p^2}$$, would furnish an
infinite number of values for $$n$$: but as $$n$$ must be an integer
number, this method will be of no use, and therefore very
different means must be employed in order to accomplish
our object.

<span class="art">97</span> We must begin with observing, that if we wished
to have $$an^2+1$$ a square, in integer numbers, (whatever be
the value of $$a$$), the thing required would not be possible.

For, in the first place, it is necessary to exclude all the
cases, in which a would be negative; next, we must exclude
those also, in which $$a$$ would be itself a square; because
then $$an^2$$ would be a square, and no square can become a
square, in integer numbers, by being increased by unity. We
are obliged, therefore, to restrict our formula to the condition,
that $$a$$ be neither negative, nor a square;
but whenever $$a$$ is a positive number, without being a square, it is
possible to assign such an integer value of $$n$$, that $$an^2 + 1$$
may become a square: and when one such value has been
found, it will be easy to deduce from it an infinite number
of others, as was taught in the last chapter: but for our
purpose it is sufficient to know a single one, even the least;
and this, Pell, an English writer, has tauglit us to find bv
an ingenious method, which we shall here explain.

<span class="art">98</span> This method is not such as may be employed generally, for any number $$a$$ whatever; it is apphcable only to
each particular case.

We shall therefore begin with the easiest cases, and shall
first seek such a value of $$n$$, that $$2n^2+1$$ may be a square,
or that $$\surd(2n^2+1)$$ may become rational.

We immediately see that this square root becomes greater
than $$n$$, and less than $$2n$$. If, therefore, we express this root
by $$n+p$$, it is obvious that $$p$$ must be less than $$n$$; and we
shall have $$\surd(2n^2+1)=n+p$$; then, by squaring,
$$2n^2+1=n^2+2np+p^2$$; therefore

$$n^2=2np+p^2-1,\quad \textrm{and} \quad n=p+\surd(2p^2-1).$$

The whole is reduced, therefore, to the condition of $$2p^2-1$$
being a square; now, this is the case if $$p=1$$, which gives
$$n=2$$, and $$\surd(2n+1)=3$$.

If this case had not been immediately obvious, we should
have gone farther; and since $$\surd(2p^2-1)>p$$, and consequently,
$$n>2p$$, we should have made $$n=2p+q$$; and should thus have had

$$2p+q=p+\surd(2p^2-1),\quad \textrm{or} \quad p+q=\surd(2p^2-1),$$

and, squaring, $$p^2+2pq+q^2=2p^2-1$$, whence

$$p^2=2pq+q^2+1,$$

which would have given $$p=q+\surd(2q^2+1)$$; so that it
would have been necessary to have $$2q^2+1$$ a square;
and as this is the case, if we make $$q = 0$$, we shall have $$p = 1$$,
and $$n = 2$$, as before. This example is sufficient to give an
idea of the method; but it will be rendered more clear and
distinct from what follows.

<span class="art">99</span> Let $$a = 3$$, that is to say, let it be required to transform the formula
$$3n^2+1$$ into a square. Here we shall make $$\surd(3n^2+1)=n+p$$, which gives

$$3n^2+1=n^2+2np+p^2,\quad 2n^2=2np+p^2-1;$$

whence we obtain $$n=\dfrac{p+\surd(3p^2-2)}{2}$$. Now, since
$$\surd(3p^2-2)$$ exceeds $$p$$, and, consequently, $$n$$ is greater
than $$\dfrac{2p}{2}$$, or than $$p$$, let us suppose $$n=p+q$$, and we shall have

$$
\begin{align}
2p+2q&=p+\surd(3p^2-2), \; \textrm{or}\\
p+2q&=\surd(3p^2-2);
\end{align}
$$

then, by squaring, $$p^2+4pq+4q^2=3p^2-2$$; so that

$$2p^2=4pq+4q^2+2,\quad \textrm{or} \quad p^2=2pq+2q^2+1,$$

and

$$p=q+\surd(3q^2+1).$$

Now, this formula being similar to the one proposed, we may make
$$q=0$$, and shall thus obtain $$p=1$$, and $$n=1$$; whence
$$\surd(3n^2+1)=2$$.

<span class="art">100</span> Let $$a = 5$$, that we may have to make a square of
the formula $$5n^2+1$$, the root of which is greater than $$2n$$.
We shall therefore suppose

$$\surd(5n^2+1)=2n+p,\quad \textrm{or} \quad 5n^2+1=4n^2+4np+p^2;$$

whence we obtain

$$n^2=4np+p^2-1,\quad \textrm{and} \quad n=2p+\surd(5p^2-1).$$

Now, $$\surd(5p^2-1)>2p$$; whence it follows that $$n>4p$$; for which reason,
we shall make $$n=4p+q$$, which gives
$$2p+q=\surd(5p^2-1)$$, or $$4p^2+4pq+q^2=5p^2-1$$, and
$$p^2=4pq+q^2+1$$; so that $$p=2q+\surd(5q^2+1)$$; and as
$$q=0$$ satisfies the terms of this equation, we shall have
$$p=1$$, and $$n=4$$; therefore $$\surd(5n^2+1)=9$$.

<span class="art">101</span>




<span class="art">102</span>




<span class="art">103</span>




<span class="art">104</span>




<span class="art">105</span>




<span class="art">106</span>




<span class="art">107</span>




<span class="art">108</span>




<span class="art">109</span>




<span class="art">110</span>




<span class="art">111</span>

#### Editions

1. Leonhard Euler. *Elements of Algebra*. Translated by Rev. John Hewlett. Third Edition. Longmans, Hurst, Rees, Orme, and Co. London. 1822.
    - [Part {{ page.part}}. {{ page.title }}](/assets/euler/en/pt-II-7.pdf)
2. Leonhard Euler. *Vollständige Anleitung zur Algebra. Mit den Zusätzen von Joseph Louis Lagrange.* Herausgegeben von Heinrich Weber. B. G. Teubner. Leipzig and Berlin. 1911. Leonhardi Euleri Opera omnia. Series prima. Opera mathematica. Volumen primum.
    - [Zweyter Theil. Zweyter Abschnitt. Capitel 7. Von einer besondern Methode die Formel $$ann+1$$ zu einem Quadrat in gantzen Zahlen zu machen](/assets/euler/de/II-II-7.pdf)