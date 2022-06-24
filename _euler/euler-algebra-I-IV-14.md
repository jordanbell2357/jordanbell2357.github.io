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

<span class="art">769</span> Let us illustrate this rule by an example, and suppose that the equation

$$x^4-10x^3+35x^2-50x+24=0$$

was given. If we compare it with our general formula (at the end of <span class="artref">Art. 767</span>),
we have $$a=-10$$, $$b=35$$, $$c=-50$$, $$d=24$$; and, consequently, the equation which must give
the value of $$p$$ is

$$8p^3-140p^2+808p-1540=0,$$

or

$$2p^3-35p^2+202p-385=0.$$

The divisors of the last term are 1, 5, 7, 11, etc.; the
first of which does not answer; but making $$p=5$$, we get
250-875+1010-385=0, so that $$p=5$$; and if we farther suppose
686-1715+1414-385=0, a proof that $$p=7$$ is the second root.
It remains now to find the third root; let us therefore divide
the equation by 2, in order to have

$$p^3-\frac{35}{2}p^2+101p-\frac{385}{2}=0,$$

and let us consider that the coefficients of the second term, or
³⁵⁄₂, being the sum of all the three roots, and the first two
making together 12, the third must necessarily be ¹¹⁄₂.

We consequently know the three roots required. But it
may be observed that one would have been sufficient,
because each gives the same four roots for our equation of the
fourth degree.

<span class="art">770</span> To prove this, let $$p=5$$; we shall then have, by the formula, $$\surd\left(\frac{1}{4}a^2+2p-b\right)$$,

$$q=\surd(25+10-35)=0, \quad \textrm{and} \quad r=\dfrac{-50+50}{0} = \frac{0}{0}.$$

Now, nothing being determined
by this, let us take the third equation,

$$r^2=p^2-d=25-24=1,$$

so that $$r=1$$; our two equations of the second degree will then be:

1. $$x^2=5x-4$$,
2. $$x^2=5x-6$$.

The first gives the roots

$$x=\frac{5}{2}\pm\surd \frac{9}{4},\quad \textrm{or} \quad x=\dfrac{5 \pm 3}{2},$$

that is to say, $$x=4$$ and $$x=1$$.

The second equation gives

$$x=\frac{5}{2} \pm \surd \frac{1}{4} = \dfrac{5 \pm 1}{2},$$

that is to say, $$x=3$$, and $$x=2$$.

But suppose now $$p=7$$, we shall have

$$q=\surd(25+14-35)=2,\quad \textrm{and} \quad r=\dfrac{-70+50}{4}=-5,$$

whence results the two equations of the second degree,

1. $$x^2=7x-12$$,
2. $$x^2=3x-2$$;

the first gives $$x=\frac{7}{2} \pm \surd \frac{1}{4}$$, or $$x=\dfrac{7 \pm 1}{2}$$,
so that $$x=4$$, and $$x=3$$; the second furnishes the root

$$x=\frac{3}{2} \pm \surd \frac{1}{4} = \dfrac{3 \pm 1}{2},$$

and, consequently, $$x=2$$, and $$x=1$$; therefore by this second supposition
the same four roots are found as by the first.

Lastly, the same roots are found, by the third value of $$p$$,
= ¹¹⁄₂: for, in this case, we have

$$q=\surd(25+11-35)=1,\quad \textrm{and} \quad r=\dfrac{-55+50}{2}= -\frac{5}{2};$$

so that the two equations of the second degree become,

1. $$x^2=6x$$,
2. $$x^2=4x-3$$.

Whence we obtain from the first, $$x=3 \pm \surd 1$$, that is to say,
$$x=4$$, and $$x=2$$; and from the second, $$x=2 \pm \surd 1$$,
that is to say, $$x=3$$, and $$x=1$$, which are the roots that we originally
obtained.

<span class="art">771</span> Let there now be proposed the equation

$$x^4-16x-12=0,$$

in which $$a=0$$, $$b=0$$, $$c=-16$$, $$d=-12$$; and our equation
of the third degree will be

$$8p^3+96p-256=0, \quad \textrm{or} \quad p^3+12p-32=0,$$

and we may make this equation still more simple, by writing
$$p = 2t$$; for we have then

$$8t^3+24t-32=0,\quad \textrm{or} \quad t^3+3t-4=0.$$

The divisors of the last term are 1, 2, 4; whence one of the roots is found to
be $$t=1$$; therefore $$p=2$$, $$q=\surd 4=2$$, and $$r=\frac{16}{4}=4$$.
Consequently, the two equations of the second degree are

$$x^2=2x+2,\quad \textrm{and} \quad x^2=-2x-6;$$

which give the roots

$$x=1 \pm \surd 3,\quad \textrm{and} \quad x=-1 \pm \surd -5.$$

<span class="art">772</span> We shall endeavour to render this resolution still
more familiar, by a repetition of it in the following example.
Suppose there were given the equation

$$x^4-6x^3+12x^2-12x+4=0,$$

which must be contained in the formula

$$(x^2-3x+p)^2 - (qx+r)^2 = 0,$$

in the former part of which we have put $$-3x$$,
because -3 is half the coefficient -6, of the given equation.
This formula being expanded, gives

$$x^4-6x^3+(2p+9-q^2)x^2-(6p+2qr)x+p^2-r^2=0;$$

which, compared with our equation, there will result from
that comparison the following equations:

1. $$2p+9-q^2=12$$,
2. $$6p+2qr=12$$,
3. $$p^2-r^2=4$$.

The first gives $$q^2=2p-3$$;  
the second, $$2qr=12-6p$$, or $$qr=6-3p$$;  
the third, $$r^2=p^2-4$$.

Multiplying $$r^2$$ by $$q^2$$, and $$p^2-4$$ by $$2p-3$$, we have

$$q^2r^2 = 36 - 36p + 9p^2;$$

so that we have the equation

$$
\begin{gather}
2p^3-3p^2-8p+12=9p^2-36p+36,\\
2p^3-12p^2+28p-24=0,\\
p^3-6p^2+14p-12=0.
\end{gather}
$$

one of the roots of which is $$p=2$$; and it follows that
$$q^2=1$$, $$q=1$$, and $$qr-r=0$$. Therefore our equation
will be $$(x^2-3x+2)^2 = x^2$$, and its square root will be
$$x^2-3x+2 = \pm x$$. If we take the upper sign, we have
$$x^2=4x-2$$; and taking the lower sign, we obtain
$$x^2=2x-2$$, whence we derive the four roots $$x=2 \pm \surd 2$$$,
and $$x=1 \pm \surd -1$$.

#### Editions

1. Leonhard Euler. *Elements of Algebra*. Translated by Rev. John Hewlett. Third Edition. Longmans, Hurst, Rees, Orme, and Co. London. 1822.
    - [Part {{ page.part }}. Section {{ page.section }}. {{ page.title }}](/assets/euler/en/IV-14.pdf)
2. Leonhard Euler. *Vollständige Anleitung zur Algebra. Mit den Zusätzen von Joseph Louis Lagrange.* Herausgegeben von Heinrich Weber. B. G. Teubner. Leipzig and Berlin. 1911. Leonhardi Euleri Opera omnia. Series prima. Opera mathematica. Volumen primum.
    - [Zweyter Theil. Erster Abschnitt. Capitel 14. Von des Bombelli Regel die Auflösung der biquadratischen Gleichungen auf cubische zu bringen](/assets/euler/de/II-I-14.pdf)