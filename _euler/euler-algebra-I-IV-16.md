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

<span class="art">792</span> 



span class="art">793</span> 

#### Editions

1. Leonhard Euler. *Elements of Algebra*. Translated by Rev. John Hewlett. Third Edition. Longmans, Hurst, Rees, Orme, and Co. London. 1822.
    - [Part {{ page.part }}. Section {{ page.section }}. {{ page.title }}](/assets/euler/en/IV-16.pdf)
2. Leonhard Euler. *Vollständige Anleitung zur Algebra. Mit den Zusätzen von Joseph Louis Lagrange.* Herausgegeben von Heinrich Weber. B. G. Teubner. Leipzig and Berlin. 1911. Leonhardi Euleri Opera omnia. Series prima. Opera mathematica. Volumen primum.
    - [Zweyter Theil. Erster Abschnitt. Capitel 16. Von der Auflösung der Gleichungen durch die Näherung](/assets/euler/de/II-I-16.pdf)