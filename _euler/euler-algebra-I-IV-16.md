---
layout: page
title: Chapter 16. "Of the Resolution of Equations by Approximation."
part: I
section: IV
chapter: 16
---

### Part {{ page.part }}. Section {{ page.section }}. {{ page.title }}

<span class="art">784</span> When the roots of an equation are not rational,
whether they may be expressed by radical quantities, or
even if we have not that resource, as is the case with equations which exceed the fourth degree,
we must be satisfied
with determining their values by approximation; that is to
say, by methods which are continually bringing us nearer to
the true value, till at last the error being very small, it may
be neglected. Different niethods of this kind have been proposed, the chief of which we shall explain.

<span class="art">785</span> The first method which we shall mention, supposes
that we have already determined, with tolerable exactness,
the value of one root; that we know, for example, that
such a value exceeds 4, and that it is less than 5. In this
case, if we suppose this value = $$4+p$$, we are certain that
$$p$$ expresses a fraction. Now, as $$p$$ is a fraction, and consequently less than unity,
the square of $$p$$, its cube, and, in
general, all the higher powers of $$p$$, will be much less with respect to unity;
and, for this reason, since we require only an
approximation, they may be neglected in the calculation.
When we have, therefore, nearly determined the fraction $$p$$,
we shall know more exactly the root $$4+p$$; from that we
proceed to determine a new value still more exact, and continue the same process till we come as near the truth as we
desire.

<span class="art">786</span> We shall illustrate this method first by an easy example, requiring by approximation the root of the equation
$$x^2=20$$.

Here we perceive, that $$x$$ is greater than 4 and less than 5;
making, therefore, $$x=4+p$$, we shall have

$$x^2=16+8p+p^2=20;$$

but as $$p^2$$ must be very small, we shall neglect it,
in order that we may only the equation $$16+8p=20$$, or $$8p=4$$.
This gives $$p=\frac{1}{2}$$, and $$x=4\frac{1}{2}$$,
which already approaches nearer the true root. If, therefore,
we now suppose $$x=4\frac{1}{2}+p'$$; we are sure that $$p'$$
expresses a fraction much smaller than before, and that we
may neglect $${p'}^2$$ with greater propriety. We have,
therefore, $$x^2=20\frac{1}{4}+9p'=20$$, or $$9p'=-\frac{1}{4}$$;
and consequently, $$p'=-\frac{1}{36}$$; therefore

$$x=4\frac{1}{2}-\frac{1}{36}=4\frac{17}{36}.$$

And if we wished to approximate still nearer to the true
value, we must make $$x=4\frac{17}{36}+p''$$, and should
thus have

$$x^2 = 20\frac{1}{1296} + 8\frac{34}{36}p''=20;$$

so that $$8\frac{34}{36}p''=-\frac{1}{1296}$$,

$$322p'=-\frac{36}{1296}=-\frac{1}{36},$$

and

$$p=-\dfrac{1}{36\cdot 322} = -\frac{1}{11592}:$$

therefore

$$x=4\frac{17}{36} - \frac{1}{11592} = 4\frac{4473}{11592},$$

a value which is so near the truth, that we may consider the error
as of no importance.

<span class="art">787</span> Now, in order to generalise what we have here laid
down, let us suppose the given equation to be $$x^2=a$$,
and that we previously know $$x$$ to be greater than $$n$$, but less
than $$n+1$$. If we now make $$x=n+p$$, $$p$$ must be a fraction,
and $$p^2$$ may be neglected as a very small quantity,
so that we shall have $$x^2=n^2+2np=a$$; or $$2np=a-n^2$$,
and $$p=\dfrac{a-n^2}{2n}$$; consequently,

$$x=n+\dfrac{a-n^2}{2n} = \dfrac{n^2+a}{2n}.$$

Now, if $$n$$ approximated towards the true value, this new value
$$\dfrac{n^2+a}{2n}$$ will approximate much nearer; and, by
substituting it for $$n$$, we shall find the result much nearer the
truth; that is, we shall obtain a new value, which may again
be substituted, in order to approach still nearer; and the
same operation may be continued as long as we please.

For example, let $$x^2=2$$; that is to say, let the square
root of 2 be required; as as we already know a value sufficiently
near, which is expressed by $$n$$, we shall have a still
nearer value of the root expressed by $$\dfrac{n^2+2}{2n}$$. Let therefore,

1. $$n=1$$, and we shall have $$x=\frac{3}{2}$$,
2. $$n=\frac{3}{2}$$, and we shall have $$x=\frac{17}{12}$$,
3. $$n=\frac{17}{12}$$, and we shall have $$x=\frac{577}{408}$$.

This last value approaches so near √2, that its square ³³²⁹²⁹⁄₁₆₆₄₆₄
differs from the number 2 only by the small quantity
¹⁄₁₆₆₄₆₄, by which it exceeds it.

<span class="art">788</span> We may proceed in the same manner, when it is
required to find by approximation cube roots, biquadrate
roots, etc.

Let there be given the equation of the third degree,
$$x^3=a$$; or let it be proposed to find the value of $$\sqrt[3]{\vphantom{a}}a$$.

Knowing that it is nearly $$n$$, we shall suppose $$x=n+p$$;
neglecting $$p^2$$ and $$p^3$$, we shall have $$x^3=n^3+3n^2p=a$$;
so that $$3n^2p=a-n^3$$, and $$p=\dfrac{a-n^3}{3n^2}$$; whence
$$x=\dfrac{2n^3+a}{3n^2}$$. If, therefore, $$n$$ is nearly equal $$\sqrt[3]{\vphantom{a}}a$$,
the quantity which we have
now found will be much nearer it. But for still greater
exactness, we may agani substitute this new value for $$n$$, and
so on.

For example, let $$x^3=2$$; and let it be required to determine $$\sqrt[3]{\vphantom{2}}2$$.
Here, if $$n$$ is nearly the vaue of the number sought, the formula $$\dfrac{2n^3+2}{3n^2}$$ will
express that number still more nearly; let us therefore make

1. $$n=1$$, and we shall have $$x=\frac{4}{3}$$,
2. $$n=\frac{4}{3}$$, and we shall have $$x=\frac{91}{72}$$,
3. $$n=\frac{91}{72}$$, and we shall have $$x=\frac{162130896}{128634294}$$.

<span class="art">789</span> This method of approximation may be employed,
with the same success, in finding the roots of all equations.

To show this, suppose we have the general equation of
the third degree,

$$x^3+ax^2+bx+c=0,$$

in which $$n$$ is very nearly the value of one of the roots. Let us make
$$x=n-p$$; and, since $$p$$ will be a fraction, neglecting the
powers of this letter, which are higher than the first degree,
we shall have $$x^2=n^2-2np$$, and $$x^3=n^3-3n^2p$$; whence
we have the equation

$$n^3-3n^2p+an^2-2anp+bn-bp+c=0,$$

or

$$n^3+an^2+bn+c=3n^2p+2anp+bp=(3n^2+2an+b)p;$$

so that $$p=\dfrac{n^3+an^2b+n-c}{3n^2+2an+b}$$, and

$$x=n-\left(\dfrac{n^3+an^2+bn+c}{3n^2+2an+b}\right)
=\dfrac{2n^3+an^2-c}{3n^2+2an+b}.$$

This value, which is more exact than the first, being substituted for $$n$$,
will furnish a new value still more accurate.

<span class="art">790</span> In order to apply this operation to an example, let

$$x^3+2x^2+3x-50=0,$$

in which $$a=2$$, $$b=3$$, and $$c=-50$$. If $$n$$ is supposed to be nearly
the value of one of the roots, $$x=\dfrac{2n^3+2n^2+50}{3n^2+4n+3}$$, will be a value
still nearer the truth.

Now, the assumed value of $$x=3$$ not being far from the true one,
we shall suppose $$n=3$$, which gives us $$x=\frac{62}{21}$$;
and if we were to substitute this new value instead of $$n$$,
we should find another still more exact.

<span class="art">791</span> We shall give only the following example, for equations of higher dimensions than the third.

Let $$x^5=6x+10$$, or $$x^5-6x-10=0$$, where we readily perceive that 1 is too small, and that
2 is too great. Now, if $$x=n$$ is a value not far from the true one, and we make
$$x=n+p$$, we shall have $$x^5=n^5+5n^4p$$; and, consequently,

$$n^5+5n^4p=6n+6p+10;$$

or

$$p(5n^4-6) = 6n+10-n^5.$$

Wherefore $$p=\dfrac{6n+10-n^5}{5n^4-6}$$, and $$x=\dfrac{4n^5+10}{5n^4-6}$$.
If we suppose $$n=1$$, we shall hae $$x=\dfrac{14}{-1} = -14$$;
this value is altogether inapplicable, a circumstance which arises
from the approximated value of $$n$$ having been taken by much too
small. We shall therefore make $$n=2$$, and shall thus obtain
$$x=\dfrac{138}{74} = \frac{69}{37}$$, a value which is much nearer
the truth. And if we were now to substitute for $$n$$, the fraction
⁶⁹⁄₃₇, we should obtain a still more exact value for the root $$x$$.

<span class="art">792</span> Such is the most usual method of finding the roots
of an equation by approxmiation, and it applies successfully
to all cases.

We shall however explain another method, which deserves attention,
on account of the facility of the calculation.
The foundation of this method consists in determining for
each equation a series of numbers, as $$a$$, $$b$$, $$c$$, etc. such, that
each term of the series, divided by the preceding one, may
express the value of the root with so much the more exactness,
according as this series of numbers is carried to a
greater length.

Suppose we have already got the terms $$p$$, $$q$$, $$r$$, $$s$$, $$t$$, etc.,
$$\dfrac{q}{p}$$ must express the root $$x$$ with tolerable exactness;
that is to say, we have $$\dfrac{q}{p}=x$$ nearly. We shall have also
$$\dfrac{r}{q}=x$$, and the multiplication of the two values will
give $$\dfrac{r}{p}=x^2$$. Farther as $$\dfrac{s}{r}=x$$, we shall also have
$$\dfrac{s}{p}=x^3$$; then, since $$\dfrac{t}{s}=x$$, we shall have $$\dfrac{t}{p}=x^4$$,
and so on.

<span class="art">793</span> For the better explanation of this method, we shall
begin with an equation of the second degree,
$$x^2=x+1$$, and shall suppose that in the above series we
have found the terms $$p$$, $$q$$, $$r$$, $$s$$, $$t$$, etc.
Now, as $$\dfrac{q}{p}=x$$, and
$$\dfrac{r}{p}=x^2$$, we shall have the equation
$$\dfrac{r}{p}=\dfrac{q}{p}+1$$, or $$q+p=r$$.
And as we find, in the same manner, that $$s=r+q$$ and $$t=s+r$$;
we conclude that each term of our series is the sum of the two preceding terms;
so that having the first two terms, we can easily continue the series to any
length. With regard to the first two terms, they may be taken at pleasure:
if we therefore suppose them to be 0, 1, our series will be

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, etc.

and such, that if we divide any term by that which immediately precedes it,
we shall have a value of $$x$$ so much nearer the true one, according as we
have chosen a term more distant.
The error, indeed, is very great at first, but it diminishes as we advance.
The series of those values of $$x$$, in the order in which they are always approximating
towards the true one, is as follows:

$$x=\frac{1}{0},\frac{1}{1},\frac{2}{1},\frac{3}{2},\frac{5}{3},\frac{8}{5},\frac{13}{8},\frac{21}{13},\frac{34}{21},
\frac{55}{34},\frac{89}{55},\frac{144}{89},\; \textrm{etc.}$$

If, for example, we make $$x=\frac{21}{13}$$, we have

⁴⁴¹⁄₁₆₉ = ²¹⁄₁₃ + 1 = ⁴⁴²⁄₁₆₉,

in which the error is only ¹⁄₁₆₉. Any of the succeeding terms will render it still less.

<span class="art">794</span> Let us also consider the equation $$x^2=2x+1$$;
and since, in all cases, $$x=\dfrac{p}{q}$$, and $$x^2=\dfrac{r}{p}$$, we shall have
$$\dfrac{r}{p}=\dfrac{2q}{p}+1$$, or $$r=2q+p$$; whence we infer
that the double of each term, added to the preceding term, will
give the succeeding one. If, therefore, we begin again with 0, 1, we shall have
the series

0, 1, 2, 5, 12, 29, 70, 169, 408, etc.

Whence it follows, that the value of $$x$$ will be expressed
still more accurately by the following fractions:

$$x=\frac{1}{0},\frac{2}{1},\frac{5}{2},\frac{12}{5},\frac{29}{12},\frac{70}{29},\frac{169}{70},\frac{408}{169},\; \textrm{etc.}$$

wliich, consequently, will always approximate nearer and
nearer the true value of $$x = 1 +\surd 2$$; so that if we take
unity from these fractions, the value of √2 will be expressed
more and more exactly by the succeeding fractions:

¹⁄₀, ¹⁄₀, ³⁄₂, ⁷⁄₅, ¹⁷⁄₁₂, ⁴¹⁄₂₉, ⁹⁹⁄₇₀, ²³⁹⁄₁₆₉, etc.

For example, ⁹⁹⁄₇₀ has for its square ⁹⁸⁰¹⁄₄₉₀₀, which differs
only by ¹⁄₄₉₀₀ from the number 2.

<span class="art">795</span> This method is no less applicable to equations, which
have a greater number of dimensions. If, for example, we
have the equation of the third degree $$x^3=x^2+2x+1$$,
we must make $$x=\dfrac{q}{p}$$, $$x^2=\dfrac{r}{p}$$, and $$x^3=\dfrac{s}{p}$$;
we shall then have $$s=r+2q+p$$; which shows how, by means of the three terms
$$p$$, $$q$$, and $$r$$, we are to determine the succeeding one, $$s$$;
and, as the beginning is always arbitrary, we may form the following series:

0, 0, 1, 1, 3, 6, 13, 28, 60, 129, etc.

from which result the following fractions for the approximate values of $$x$$:

$$x=\frac{0}{0},\frac{1}{0},\frac{1}{1},\frac{3}{1},\frac{6}{3},\frac{13}{6},\frac{28}{13},\frac{60}{28},\frac{129}{60},\;\textrm{etc.}$$

The first of these values would be very far from the truth;
but if we substitute in the equation ⁶⁰⁄₂₈, or ¹⁵⁄₇, instead of $$x$$, we obtain

³³⁷⁵⁄₃₄₃ = ²²⁵⁄₄₉ + ³⁰⁄₇ + 1 = ³³⁸⁸⁄₃₄₃,

in which the error is only ¹³⁄₃₄₃.



<span class="art">796</span>



<span class="art">797</span>

#### Editions

1. Leonhard Euler. *Elements of Algebra*. Translated by Rev. John Hewlett. Third Edition. Longmans, Hurst, Rees, Orme, and Co. London. 1822.
    - [Part {{ page.part }}. Section {{ page.section }}. {{ page.title }}](/assets/euler/en/IV-16.pdf)
2. Leonhard Euler. *Vollständige Anleitung zur Algebra. Mit den Zusätzen von Joseph Louis Lagrange.* Herausgegeben von Heinrich Weber. B. G. Teubner. Leipzig and Berlin. 1911. Leonhardi Euleri Opera omnia. Series prima. Opera mathematica. Volumen primum.
    - [Zweyter Theil. Erster Abschnitt. Capitel 16. Von der Auflösung der Gleichungen durch die Näherung](/assets/euler/de/II-I-16.pdf)