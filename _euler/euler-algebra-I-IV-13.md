---
layout: page
title: Chapter 13. "Of the Resolution of Equations of the Fourth Degree."
part: I
section: IV
chapter: 13
---

### Part {{ page.part }}. Section {{ page.section }}. {{ page.title }}

<span class="art">750</span> When the highest power of the quantity $$x$$ rises to
the fourth degree, we have equations of the fourth degree,
the general form of which is

$$x^4+ax^3+bx^2+cx+d=0.$$

We shall, in the first place, consider pure equations of
the fourth degree, the expression for which is simply $$x^4=f$$;
the root of which is immediately found by extracting the
biquadrate root of both sides, since we obtain $$x=\sqrt[4]{\vphantom{f}}f$$.

<span class="art">751</span> As $$x^4$$ is the square of $$x^2$$, the calculation is greatly facilitated by beginning
with the extraction of the square root; for we shall then have $$x^2 = \surd f$$; and, taking the
square root again, we have $$x=\sqrt[4]{\vphantom{f}}f$$; so that $$\sqrt[4]{\vphantom{f}}f$$
is nothing but the square root of the square root of $$f$$.

For example, if we had the equation $$x^4=2401$$, we should immediately have $$x^2=49$$, and then $$x=7$$.

<span class="art">752</span> It is true this is only one root; and since there are
always three roots in an equation of the third degree, so also
there are four roots in an equation of the fourth degree:
but the method which we have explained will actually give
those four roots. For, in the above example, we have not
only $$x^2=49$$, but also $$x^2=-49$$; now, the first value gives
the two roots $$x=7$$ and $$x=-7$$, and the second value gives
$$x = \surd -49 = 7\surd -1$$,
and $$x=-\surd -49=-7\surd -1$$; whcih are the four biquadrate roots of 2401.
The same is also true with respect to other numbers.

<span class="art">753</span> Next to these pure equations, we shall consider
others, in which the second and fourth terms are wanting,
and which have the form $$x^4+fx^2+g=0$$. These may be
resolved by the rule for equations of the second degree;
for if we make $$x^2=y$$, we have $$y^2+fy+g=0$$, or
$$y^2=-fy-g$$, whence we deduce

$$y=-\frac{1}{2}f \pm \surd \left(\frac{1}{4}f^2-g\right) = \left( \dfrac{-f \pm \surd(f^2-4g)}{2}\right).$$

Now, $$x^2=y$$; so that

$$x = \pm \surd \left( \dfrac{-f \pm \surd(f^2-4g)}{2}\right),$$

in which the double signs ± indicate all the four roots.

<span class="art">754</span> But whenever the equation contains all the terms, it
may be considered as the product of four factors. In fact,
if we multiply these four factors together, 

$$(x-p) \cdot (x-q) \cdot (x-r) \cdot (x-s),$$

we get the product

$$x^4 - (p+q+r+s)x^3 + (pq+pr+ps+qr+qs+rs)x^2
-(pqr+pqs+prs+qrs)x+pqrs;$$

and this quantity cannot be equal to 0, except when one of the four
factors is = 0. Now, that may happen in four ways;

1. when $$x=p$$;
2. when $$x=q$$;
3. when $$x=r$$;
4. when $$x=s$$;

and consequently these are the four roots of the equation.

<span class="art">755</span> If we consider this formula with attention, we observe, in the second term, the sum of the four roots multiplied by
$$-x^3$$; in the third term, the sum of all the possible products of two roots, multiplied by $$x^2$$;
in the fourth term, the sum of the products of the roots combined three by three, multiplied by $$-x$$; lastly,
in the fifth term, the product of all the four roots multiplied together.

<span class="art">756</span> As the last term contains the product of all the roots,
it is evident that such an equation of the fourth degree can
have no rational root, which is not a divisor of the last term.
This principle, therefore, furnishes an easy method of determining all the rational roots, when there are any; since
we have onlv to substitute successively for $$x$$ all the divisors
of the last term, till we find one which satisfies the terms of
the equation: for having found such a root, for example,
$$x=p$$, we have only to divide the equation by $$x-p$$, after
having brought all thr terms to one side, and then suppose the quotient = 0. We thus obtian an equation
of the third degree, which may be resolved by the rules already given.

<span class="art">757</span> Now, for this purpose, it is absolutely necessary
that all the terms should consist of integers, and that the
first should have only unity for the coefficient; whenever,
therefore, any terms contain fractions, we must begin by destroying those fractions, and this may always be done by
substituting, instead $$x$$, the quantity $$y$$, divided by a number which contains all the denominators of those fractions.

For example, if we have the equation

$$x^4-\frac{1}{2}x^3+\frac{1}{3}x^2-\frac{3}{4}x+\frac{1}{18}=0,$$

as we find here fractions which have for denominators 2, 3,
and multiples of these numbers, let us suppose $$x=\dfrac{y}{6}$$,
and we shall then have

$$\dfrac{y^4}{6^4} - \dfrac{\frac{1}{2}y^3}{6^3} + \dfrac{\frac{1}{3}y^2}{6^2} - \dfrac{\frac{3}{4}y}{6} + \dfrac{1}{18} = 0,$$

an equation, which, multiplied by $$6^4$$, becomes

$$y^4-3y^3+12y^2-162y+72=0.$$

If we now wish to know whether this equation has rational
roots, we must write, instead of $$y$$, the divisors of 72 successively,
in order to see in what cases the formula would
really be reduced to 0.

<span class="art">758</span> But as the roots may as well be positive as negative,
we must make two trials with each divisor ; one, supposing
that divisor positive, the other, considering it as negative.
However, the following rule will frequently enable us to
dispense with this. Whenever the signs + and - succeed each other regularly,
the equation has as many positive
roots as there are changes in the signs; and as many times
as the same sign recurs without the other intervening, so
many negative roots belong to the equation. Now, our
example contains four changes of the signs, and no succession; so that all the roots are positive: and we have no
need to take any of the divisors of the last term negatively.

<span class="art">759</span> Let there be given the equation

$$x^4+2x^3-7x^2-8x+12=0.$$

We see here two changes of signs, and also two successions;
whence we conclude, with certainty, that this equation contains two positive,
and as many negative roots, which must
all be divisors of the number 12. Now, its divisors being
1, 2, 3, 4, 6, 12, let us first try $$x=+1$$, which actually produces
0; therefore one of the roots is $$x=1$$.

If we next make $$x=-1$$, we find +1-2-7+8+12=21-9=12: so that $$x=-1$$ is not one of the
roots of the equation. Let us now make $$x=2$$, and we again find the quantity = 0;
consequently, another of the roots is $$x=2$$; but $$x=-2$$, on the contrary, is found
not to be a root. If we suppose $$x=3$$, we have 81+54-63-24+12=60, so that the supposition
does not answer; but $$x=-3$$, giving 81-54-63+24+12=0, this is evidently one of the roots
sought. Lastly, when we try $$x=-4$$, we likewise see the equation reduced to nothing;
so that all the four roots are rational, and have the following values: $$x=1$$, $$x=2$$, $$x=-3$$,
and $$x=-4$$;
and, according to the rule given above, two of these roots are positive, and the other two
are negative. 

<span class="art">760</span> But as no root could be determined by this method,
when the roots are all irrational, it was necessary to devise
other expedients for expressing the roots whenever this case
occurs; and two different methods have been discovered for
finding such roots, whatever be the nature of the equation of
the fourth degree.

But before we explain those general methods, it will be
proper to give the solution of some particular cases, which
may frequently be applied with great advantage.

<span class="art">761</span> When the equation is such, that the coefficients of
the terms succeed in the same manner, both in the direct
and in the inverse order of the terms, as happens in the following equation;

$$x^4+mx^3+nx^2+mx+1=0;$$

or in this other equation, which is more general:

$$x^4+max^3+na^2x^2+ma^3x+a^4=0;$$

we may always consider such a formula as the product of
two factors, which are of the second degree, and are easily
resolved. In fact, if we represent this last equation by the
product

$$(x^2+pax+a^2)\cdot(x^2+qax+a^2)=0,$$

in which it is required to determine $$p$$ and $$q$$ in such a manner,
that the above equation may be obtained, we shall find,
by performing the multiplication,

$$x^4+(p+q)ax^3+(pq+2)a^2x^2+(p+q)a^3x+a^4=0;$$

and, in order that this equation may be the same as the
former, we must have,

1. $$p+q=m$$,
2. $$pq+2=n$$,

and, consequently, $$pq=n-2$$.

Now, squaring the first of those equations, we have

$$p^2+2pq+q^2=m^2$$; and if from this we subtract the second,
taken four times, or $$4pq=4n-8$$, there remains
$$p^2-2pq+q^2=m^2-4n+8$$; and taking the square root,
we find $$p-q=\surd(m^2-4n+8)$$; also, $$p+q=m$$; we
shall therefore have, by addition, $$2p=m+\surd(m^2-4n+8)$$,
or $$p=\dfrac{m+\surd(m^2-4n+8)}{2}$$; and, by subtraction,
$$2q=m-\surd(m^2-4n+8)$$, or $$q=\dfrac{m-\surd(m^2-4n+8)}{2}$$. Having
therefore found $$p$$ and $$q$$, we have only to suppose each
factor = 0, in order to determine the value of $$x$$. The first
gives $$x^2+pax+a^2=0$$, or $$x^2=-pax-a^2$$, whence we obtain

$$x=-\dfrac{pa}{2} \pm \surd \left(\dfrac{p^2a^2}{4} - a^2\right),$$

or

$$x = -\dfrac{pa}{2} \pm \frac{1}{2} a \surd(p^2-4).$$

The second factor gives

$$x=-\dfrac{qa}{2} \pm \frac{1}{2}a\surd(q^2-4);$$

and these are the four roots of the given equation.

<span class="art">762</span> To render this more clear, let there be given the
equation

$$x^4-4x^3-3x^2-4x+1=0.$$

We have here $$a=1$$, $$m=-4$$, $$n=-3$$; consequently, $$m^2-4n+8=36$$, and the
square root of this quantity is = 6; therefore

$$p=\dfrac{-4+6}{2}=1,\quad \textrm{and} \quad q=\dfrac{-4-6}{2} = -5;$$

whence result the four roots, the first and second

$$x=-\frac{1}{2} \pm \frac{1}{2} \surd -3 = \dfrac{-1 \pm \surd (-3)}{2};$$

and the third and fourth

$$x = \frac{5}{2} \pm \frac{1}{2}\surd 21 = \dfrac{5 \pm \surd 21}{2};$$

that is, the four roots of the given equation are:

1. $$x=\dfrac{-1+\surd -3}{2}$$,
2. $$x=\dfrac{-1-\surd -3}{2}$$,
3. $$x=\dfrac{5+\surd 21}{2}$$,
4. $$x=\dfrac{5-\surd 21}{2}$$.

The first two of these roots are imaginary, or impossible;
but the last two are possible; since we may express √21
to any degree of exactness, by means of decimal fractions.
In fact, 21 being the same with 21.00000000, we have only to
extract the square root, which gives √21 = 4.5825.

Since, therefore, √21 = 4.5825, the third root is very nearly $$x=4.7912$$,
and the fourth $$x=0.2087$$.
It would have been easy to have determined these roots with still
more precision; for we observe that the fourth root is very nearly
²⁄₁₀, or ⅕, which value will answer the equation with
sufficient exactness. In fact, if we make $$x=\frac{1}{5}$$, we find

¹⁄₆₂₅ - ⁴⁄₁₂₅ - ³⁄₂₅ - ⅘ + 1 = ³¹⁄₆₂₅.

We ought however to have obtained 0, but the difference is evidently not great.

<span class="art">763</span> The second case in which such a resolution takes
place, is the same as the first with regard to the coefficients,
but differs from it in the signs, for we shall suppose that the
second and the fourth terms have different signs; such, for
example, as the equation

$$x^4+max^3+na^2x^2-ma^3x+a^4=0,$$

which may be represented by the product

$$(x^2+pax-a^2) \cdot (x^2+qax-a^2)=0.$$

For the actual multiplication of these factors gives

$$x^4+(p+q)ax^3+(pq-2)a^2x^2 - (p+q)a^3x + a^4,$$

a quantity equal to that which was given, if we suppose,
in the first place, $$p+q=m$$, and in the second place,
$$pq-2=n$$, or $$pq=n+2$$; because in this manner the fourth terms
become equal of themselves. If we now square
the first equation, as before (<span class="artref">Art. 761</span>)
we shall have
$$p^2+2pq+q^2=m^2$$; and if from this we subtract the second, taken four
times, or $$4pq=4n+8$$, there will remain $$p^2-2pq+q^2=m^2-4n-8$$; the square
root of which is $$p-q=\surd(m^2-4n-8)$$, and thence, by adding
$$pn+q=m$$, we obtain

$$p=\dfrac{m+\surd(m^2-4n-8)}{2};$$

and by subtracting $$p+q$$,

$$q = \dfrac{m-\surd(m^2-4n-8)}{2}.$$

Having therefore found $$p$$ and $$q$$,
we shall obtain from the first factor (as in <span class="artref">Art. 761</span>)
the two roots

$$x=-\frac{1}{2}pa \pm \frac{1}{2}a \surd(p^2+4),$$

and from the second factor, the two roots

$$x=-\dfrac{1}{2}qa \pm \frac{1}{2}a\surd(q^2+4),$$

that is, we have the four roots of the equation proposed.

<span class="art">764</span> Let there be given the equation

$$x^4-3\cdot 2x^3 + 3\cdot 8x + 16=0.$$

Here, we have $$a=2$$, $$m=-3$$, and $$n=0$$; so that
$$\surd(m^2-4n-8)=1$$, which is equal to $$p-q$$; and, consequently,

$$p=\dfrac{-3+1}{2}=-1,\quad \textrm{and}\quad q=\dfrac{-3-1}{2}=-2.$$

Therefore the first two roots are $$x=1 \pm \surd 5$$, and the
last two are $$x=2 \pm \surd 8$$; so that the four roots sought
will be,

1. $$x=1+\surd 5$$,
2. $$x=1-\surd 5$$,
3. $$x=2+\surd 8$$,
4. $$x=2-\surd 8$$.

Consequently, the four factors of our equation will be

$$(x-1-\surd 5)\cdot (x-1+\surd 5)\cdot (x-2-\surd 8)\cdot (x-2+\surd 8),$$

and their actual multiplication produces the given equation;
for the first two being multiplied together, give $$x^2-2x-4$$, and the other
two give $$x^2-4x-4$$: now, these product multiplied together, make
$$x^4-6x^3+24x+16$$, which is the same equation that was proposed.

#### Editions

1. Leonhard Euler. *Elements of Algebra*. Translated by Rev. John Hewlett. Third Edition. Longmans, Hurst, Rees, Orme, and Co. London. 1822.
    - [Part {{ page.part }}. Section {{ page.section }}. {{ page.title }}](/EulerAlgebra/en/IV-13.pdf)
2. Leonhard Euler. *Vollständige Anleitung zur Algebra. Mit den Zusätzen von Joseph Louis Lagrange.* Herausgegeben von Heinrich Weber. B. G. Teubner. Leipzig and Berlin. 1911. Leonhardi Euleri Opera omnia. Series prima. Opera mathematica. Volumen primum.
    - [Zweyter Theil. Erster Abschnitt. Capitel 13. Von der Auflösung der Gleichungen des vierten Grades, welche auch biquadratische Gleichungen genennt werden](/EulerAlgebra/de/II-I-13.pdf)