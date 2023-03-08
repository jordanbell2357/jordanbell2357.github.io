---
layout: page
title: Chapter 12. "Of the Rule of Cardano, or of Scipione del Ferro."
part: I
section: IV
chapter: 12
---

### Part {{ page.part }}. Section {{ page.section }}. {{ page.title }}

<span class="art">734</span> When we have removed fractions from an equation
of the third degree, according to the manner which has been
explained, and none of the divisors of the last term are
found to be a root of the equation, it is a certain proof, not
only that the equation lias no root in integer numbers, but
also that a fractional root cannot exist; which may be
proved as follows.

Let there be given the equation
$$x^3-ax^2+bx-c=0$$,
in which, $$a$$, $$b$$, $$c$$
express integer numbers. If we suppose,
for example, $$x=\frac{3}{2}$$,
we shall have $$\frac{27}{8}-\frac{9}{4}a+\frac{3}{2}b-c=0$$.
Now, the first term only has 8 for the denominator; the
others being either integer numbers, or numbers divided
only by 4 or by 2, and therefore cannot make 0 with the
first term. The same thing happens with every other
fraction.

<span class="art">735</span> As in those fractions the roots of the equation are
neither integer numbers, nor fractions, they are irrational,
and, as it often happens, imaginary. The manner, therefore, of expressing them,
and of determining the radical
signs which affect them, forms a very important point, and
deserves to be carefully explained. This method, called *Cardano's Rule*,
is ascribed to Cardano, or more properly to Scipione del Ferro,
both of whom lived some centuries since.

<span class="art">736</span> In order to understand this rule, we must first attentively consider
the nature of a cube, whose root is a binomial.

Let $$a+b$$ be
that root; then the cube of it will be
$$a^3+3a^2b+3ab^2+b^3$$,
and we see that it is composed of
the cubes of the two terms of the binomial, and beside that,
of the two middle terms, $$3a^2b+3ab^2$$, 
which have the common factor $$3ab$$, multiplying the other factor,
$$a+b$$;
that is
to say, the two terms contain thrice the product of the two
terms of the binomial, multiplied by the sum of those terms.

<span class="art">737</span> Let us now suppose $$x=a+b$$;
taking the cube of
each side, we have
$$x^3=a^3+b^3+3ab(a+b)$$:
and, since $$a+b=x$$,
we shall have the equation, $$x^3=a^3+b^3+3abx$$
or $$x^3=3abx+a^3+b^3$$,
one of the roots of which we know
to be $$x=a+b$$.
Whenever, therefore, such an equation
occurs, we may assign one of its roots.

For example, let $$a=2$$ and $$b=3$$;
we shall then have
the equation $$x^3=18x+35$$,
which we know with certainty
to have $$x=5$$ for one of its roots.

<span class="art">738</span> Farther, let us now suppose $$a^3=p$$ and $$b^3=q$$;
we
shall then have $$a=\sqrt[3]{\vphantom{p}}p$$ and $$b=\sqrt[3]{\vphantom{q}}q$$,
consequently, $$ab=\sqrt[3]{\vphantom{pq}}pq$$;
therefore, whenever we meet with an equation, of the form
$$x^3=3x\sqrt[3]{\vphantom{pq}}pq+p+q$$,
we know that one of the roots is
$$\sqrt[3]{\vphantom{p}}p+\sqrt[3]{\vphantom{q}}q$$.

Now, we can determine $$p$$ and $$q$$,
in such a manner, that
both $$3\sqrt[3]{\vphantom{pq}}pq$$ and $$p+q$$
may be quantities equal to determinate numbers; so that we can always resolve an equation
of the third degree, of the kind which we speak of.

<span class="art">739</span> Let, in general, the equation $$x^3=fx+g$$
be proposed. Here, it will be necessary to compare
$$f$$ with $$3\sqrt[3]{\vphantom{pq}}pq$$
and $$g$$ with $$p+q$$;
that is, we must determine $$p$$ and $$q$$ in
such a manner, that
$$3\sqrt[3]{\vphantom{pq}}pq$$ may become equal to
$$f$$, and $$p+q=g$$;
for we then know that one of the roots of our
equation will be
$$x=\sqrt[3]{\vphantom{p}}p+\sqrt[3]{\vphantom{q}}q$$.

<span class="art">740</span> We have therefore to resolve these two equations,

$$
\begin{gather}
3\sqrt[3]{\vphantom{pq}}pq=f,\\
p+q=g.
\end{gather}
$$

The first gives $$\sqrt[3]{\vphantom{pq}}pq=\dfrac{f}{3}$$;
or $$pq=\dfrac{f^3}{27}=\frac{1}{27}f^3$$,
and $$4pq=\frac{4}{27}f^3$$.
The second equation, being squared, gives
$$p^2+2pq+q^2=g^2$$; if we subtract from it $$4pq=\frac{4}{27}f^3$$,
we have $$q^2-2pq+q^2=g^2-\frac{4}{27}f^3$$,
and taking the
square root of both sides, we have

$$p-q=\surd\left(g^2-\frac{4}{27}f^3\right).$$

Now, since $$p+q=g$$, we have, by adding $$p+q$$
to one
side of the equation, and its equal, $$g$$, to the other,
$$2p=g+\surd\left(g^2-\frac{4}{27}f^3\right)$$;
and by subtracting $$p-q$$ from $$p+q$$, we have
$$2q=g-\surd\left(g^2-\frac{4}{27}f^3\right)$$;
consequently,

$$p=\dfrac{g+\surd\left(g^2-\frac{4}{27}f^3\right)}{2},\quad \textrm{and} \quad q=\dfrac{g-\surd\left(g^2-\frac{4}{27}f^3\right)}{2}.$$

<span class="art">741</span> In a cubic equation, therefore, of the form
$$x^3=fx+g$$,
whatever be the numbers
$$f$$ and $$g$$,
we have always
for one of the roots

$$x=\sqrt[3]{\vphantom{\dfrac{g+\surd\left(g^2-\frac{4}{27}f^3\right)}{2}}}\dfrac{g+\surd\left(g^2-\frac{4}{27}f^3\right)}{2} + \sqrt[3]{\vphantom{\dfrac{g-\surd\left(g^2-\frac{4}{27}f^3\right)}{2}}} \dfrac{g-\surd\left(g^2-\frac{4}{27}f^3\right)}{2};$$

that is, an irrational quantity, containing not only the sign
of the square root, but also the sign of the cube root; and
this is the formula which is called the *Rule of Cardano*.

<span class="art">742</span> Let us apply it to some examples, in order that its
use may be better understood.

Let $$x^3=6x+9$$. First, we shall have $$f=6$$, and $$g=9$$;
so that $$g^2=81$$, $$f^2=216$$, $$\frac{4}{27}f^3=32$$; then
$$g^2-\frac{4}{27}f^3=49$$, and $$\surd\left(g-\frac{4}{27}f^3\right)=7$$.
Therefore, one
of the roots of the given equation is

$$x=\sqrt[3]{\vphantom{\frac{9+7}{2}}} \frac{9+7}{2} + \sqrt[3]{\vphantom{\frac{9-7}{2}}} \frac{9-7}{2} = \sqrt[3]{\vphantom{\frac{16}{2}}} \frac{16}{2} + \sqrt[3]{\vphantom{\frac{2}{2}}} \frac{2}{2} = \sqrt[3]{\vphantom{8}} 8 + \sqrt[3]{\vphantom{1}} 1 = 2+1=3.$$

<span class="art">743</span> Let there be proposed the equation $$x^2=3x+2$$.
Here, we shall have
$$f=3$$ and $$g=2$$;
and consequently,
$$g^2=4$$, $$f^3=27$$, and $$\frac{4}{27}f^3=4$$; which gives
$$\surd \left(g^2-\frac{4}{27}f^3\right)=0$$;
whence it follows, that one of the
roots is

$$x=\sqrt[3]{\vphantom{\frac{2+0}{2}}} \frac{2+0}{2}+\sqrt[3]{\vphantom{\frac{2-0}{2}}} \frac{2-0}{2}=1+1=2.$$

<span class="art">744</span> It often happens, however, that, though such an
equation has a rational root, that root cannot be found by
the rule which we are now considering.

Let there be given the equation $$x^3=6x+40$$, in which
$$x=4$$ is one of the roots. We have here
$$f=6$$ and $$g=40$$; farther, $$g^2=1600$$, and $$\frac{4}{27}f^3=32$$; so that
$$g^2-\frac{4}{27}f^3=1568$$, and

$$\surd\left(g-\frac{4}{27}f^3\right)=\surd 1568=\surd (4\cdot 4\cdot 49\cdot 2)=28\surd 2;$$

consequently one of the roots
will be

$$x=\sqrt[3]{\vphantom{\frac{40+28\surd 2}{2}}} \frac{40+28\surd 2}{2} + \sqrt[3]{\vphantom{\frac{40-28\surd 2}{2}}} \frac{40-28\surd 2}{2}$$

or

$$x=\sqrt[3]{\vphantom{1}} (20+14\surd 2) + \sqrt[3]{\vphantom{1}} (20-14\surd 2);$$

which quantity is really =4, although, upon inspection, we
should not suppose it. In fact, the cube root of 2+√2 being 20+14√2,
we have, reciprocally, the cube root of 20+14√2 equal to 2+√2; in the same manner,
$$\sqrt[3]{1}(20-14\surd 2)=2-\surd 2$$;
wherefore our root
$$x=2+\surd 2+2-\surd 2=4$$.

<span class="art">745</span> To this rule it might be objected, that it does not
extend to all eqviations of the third degree, because the
square of $$x$$ does not occur in it; that is to say, the second
term of the equation is wanting. But we may remark, that
every complete equation may be transformed into another,
in which the second term is wanting, which will therefore
enable us to apply the rule.

To prove this, let us take the complete equation
$$x^3-6x^2+11x-6=0$$: where, if we take the third of the
coefficient 6 of the second term, and make $$x-2=y$$, we shall have

$$x=y+2,\qquad x^2=y^2+4y+4,\quad \textrm{and} \quad x^3=y^3+6y^2+12y+8;$$

Consequently,

<table>
<tbody>
  <tr>
    <td>\(x^3\)</td>
    <td>\(y^3\)</td>
    <td>\(+6y^2\)</td>
    <td>\(+12y\)</td>
    <td>+8</td>
  </tr>
  <tr>
    <td>\(-6x^2\)</td>
    <td></td>
    <td>\(-6y^2\)</td>
    <td>\(-24y\)</td>
    <td>-24</td>
  </tr>
  <tr>
    <td>\(11x\)</td>
    <td></td>
    <td></td>
    <td>\(11y\)</td>
    <td>+22</td>
  </tr>
  <tr>
    <td>-6</td>
    <td></td>
    <td></td>
    <td></td>
    <td>-6</td>
  </tr>
  <tr>
    <td>or, \(x^3-6x^2+11x-6\)</td>
    <td>\(y^3\)</td>
    <td></td>
    <td>\(-y\)</td>
    <td></td>
  </tr>
</tbody>
</table>

We have, therefore, the equation $$y^3-y=0$$, the resolution of which it is evident, since we immediately perceive
that it is the product of the factors

$$y(y^2-1)=y(y+1)(y-1)=0.$$

If we now make each of these factors =0, we have

<table>
<thead>
  <tr>
    <th>I</th>
    <th>II</th>
    <th>III</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>\(y=0\),</td>
    <td>\(y=-1\),</td>
    <td>\(y=1\),</td>
  </tr>
  <tr>
    <td>\(x=2\),</td>
    <td>\(x=1\),</td>
    <td>\(x=3\),</td>
  </tr>
</tbody>
</table>

that is to say, the three roots which we have already found.

<span class="art">746</span> Let there now be given the general equation of the
third degree,  $$x^3+ax^2+bx+c=0$$, of which it is required to destroy the second term.

For this purpose, we must add to $$x$$ the third of the coefficient of the second term, preserving the same sign, and
then write for this sum a new letter, as for example $$y$$, so
that we shall have $$x+\frac{1}{3}a=y$$, and $$x=y-\frac{1}{3}a$$; whence
results the following calculation:

$$x=y-\frac{1}{3}a, \qquad x^2=y^2-\frac{2}{3}ay+\frac{1}{9}a^2,$$

and

$$x^3=y^3-ay^2+\frac{1}{3}a^2y+\frac{1}{27}a^3$$

Consequently,

<table>
<tbody>
  <tr>
    <td>\(x^3\)</td>
    <td>\(y^3\)</td>
    <td>\(-ay^2\)</td>
    <td>\(+\frac{1}{3}a^2y\)</td>
    <td>\(-\frac{1}{27}a^3\)</td>
  </tr>
  <tr>
    <td>\(ax^2\)</td>
    <td></td>
    <td>\(ay^2\)</td>
    <td>\(-2/3a^2y\)</td>
    <td>\(+\frac{1}{9}a^3\)</td>
  </tr>
  <tr>
    <td>\(bx\)</td>
    <td></td>
    <td></td>
    <td>\(by\)</td>
    <td>\(-\frac{1}{3}ab\)</td>
  </tr>
  <tr>
    <td>\(c\)</td>
    <td></td>
    <td></td>
    <td></td>
    <td>\(c\)</td>
  </tr>
</tbody>
</table>

or,

$$y^2 - \left(\frac{1}{3}a-b\right)y + \frac{2}{27}a \sqrt[3]{\vphantom{-\frac{1}{3}ab}} -\frac{1}{3}ab + c =0,$$

an equation in which the second term is wanting.

<span class="art">747</span> We are enabled, by means of this transformation, to
find the roots of all equations of the third degree, as the following example will show.

Let it be proposed to resolve the equation

$$x^3-6x^2+13x-12=0.$$

Here it is first necessary to destroy the second term; for
which purpose, let us make $$x-2=y$$, and then we shall
have $$x=y+2$$, $$x^2=y^2+4y+4$$, and $$x^3=y^3+6y^2+12y+8$$; therefore

<table>
<tbody>
  <tr>
    <td>\(x^3\)</td>
    <td>=</td>
    <td>\(y^3\)</td>
    <td>\(+6y^2\)</td>
    <td>\(+12y\)</td>
    <td>+8</td>
  </tr>
  <tr>
    <td>\(-6x^2\)</td>
    <td>=</td>
    <td></td>
    <td>\(-6y^2\)</td>
    <td>\(-24y\)</td>
    <td>-24</td>
  </tr>
  <tr>
    <td>\(13x\)</td>
    <td>=</td>
    <td></td>
    <td></td>
    <td>\(13y\)</td>
    <td>+26</td>
  </tr>
  <tr>
    <td>-12</td>
    <td>=</td>
    <td></td>
    <td></td>
    <td></td>
    <td>-12</td>
  </tr>
</tbody>
</table>

which gives $$y^3+y-2=0$$; or $$y^3=-y+2$$.

And if we compare this equation with the formula, (<span class="artref">Art. 741</span>)
$$x^3=fx+g$$, we have $$f=-1$$, and $$g=2$$; wherefore, $$g^2=4$$, and
$$\frac{4}{27}f^3=-\frac{4}{27}$$; also, $$g^2-\frac{4}{27}f^3=4+\frac{4}{27}=\frac{112}{27}$$,
and

$$\surd \left(g^2-\frac{4}{27}f^3\right)= \surd \frac{112}{27} = \dfrac{4\surd 21}{9};$$

consequently,

$$y=\sqrt[3]{\vphantom{\dfrac{2+\frac{4\surd 21}{9}}{2}}} \left( \dfrac{2+\frac{4\surd 21}{9}}{2} \right)
+\sqrt[3]{\vphantom{\dfrac{2-\frac{4\surd 21}{9}}{2}}} \left( \dfrac{2-\frac{4\surd 21}{9}}{2} \right),$$

or

$$
y=
\sqrt[3]{\vphantom{1+\dfrac{2\surd 21}{9}}} \left(1+\dfrac{2\surd 21}{9} \right)
+
\sqrt[3]{\vphantom{1-\dfrac{2\surd 21}{9}}} \left(1-\dfrac{2\surd 21}{9} \right),
$$

or

$$
y=\sqrt[3]{\vphantom{\dfrac{9+2\surd 21}{9}}} \left( \dfrac{9+2\surd 21}{9} \right)
+
\sqrt[3]{\vphantom{\dfrac{9-2\surd 21}{9}}} \left( \dfrac{9-2\surd 21}{9} \right),
$$

or

$$
y=\sqrt[3]{\vphantom{\dfrac{27+7\surd 21}{27}}} \left( \dfrac{27+7\surd 21}{27} \right)
+
\sqrt[3]{\vphantom{\dfrac{27-7\surd 21}{27}}} \left( \dfrac{27-7\surd 21}{27} \right),
$$

or

$$
y=\frac{1}{3}\sqrt[3]{\vphantom{1}}(27+6\surd 21) + \frac{1}{3}\sqrt[3]{\vphantom{1}}(27-6\surd 21);
$$

and it remains to substitute this value in $$x=y+2$$.

<span class="art">748</span> In the solution of this example, we have been
brought to a quantity doubly irrational; but we must not
immediately conclude that the root is irrational: because the
binomials $$27 \pm 6\surd 21$$ might happen to be real cubes; and
this is the case here; for the cube of
$$\dfrac{3+\surd 21}{2}$$ being $$\dfrac{216+48\surd 21}{8}=27+6\surd 21$$,
it follows that the cube root of $$27-6\surd 21$$ is $$\dfrac{3-\surd 21}{2}$$.
Hence the value which we
found for $$y$$ becomes

$$y=\frac{1}{3}\left( \dfrac{3+\surd 21}{2}\right)+\frac{1}{3}\left( \dfrac{3-\surd 21}{2}\right)=\frac{1}{2}+\frac{1}{2}=1.$$

Now, since $$y=1$$, we have $$x=3$$ for one of the roots of the
equation proposed, and the other two will be found by
dividing the equation by $$x-3$$.

<a href="https://artofproblemsolving.com/texer/oqfowwuq">
<img src="/EulerAlgebra/oqfowwuq.png" alt="Polynomial long division" width="230" height="176">
</a>

Also making the quotient $$x^2-3x+4=0$$, we have $$x^2=3x-4$$; and

$$x=\frac{3}{2} \pm \surd \left(\frac{9}{4}-\frac{16}{4}\right)=\frac{3}{2} \pm \surd -\frac{7}{4} = \dfrac{3 \pm \surd -7}{2};$$

which are the other two roots, but they are imaginary.

<span class="art">749</span> It was, however, by chance, as we have remarked,
that we were able, in the preceding example, to extract the
cube root of the binomials that we obtained, which is the
case only when the equation has a rational root; consequently, the rules of the preceding chapter are more easily
employed for finding that root. But when there is no
rational root, it is, on the other hand, impossible to express
the root which we obtain in any other way, than according
to the rule of Cardano; so that it is then impossible to apply
reductions. For example, in the equation
$$x^3=6x+4$$, we have $$f=6$$ and $$g=4$$; so that

$$x=\sqrt[3]{\vphantom{1}}(2+2\surd -1)+\sqrt[3]{\vphantom{1}}(2-2\surd -1),$$

which cannot be otherwise expressed.


#### Editions

1. Leonhard Euler. *Elements of Algebra*. Translated by Rev. John Hewlett. Third Edition. Longmans, Hurst, Rees, Orme, and Co. London. 1822.
    - [Part {{ page.part }}. Section {{ page.section }}. {{ page.title }}](/EulerAlgebra/en/IV-12.pdf)
2. Leonhard Euler. *Vollständige Anleitung zur Algebra. Mit den Zusätzen von Joseph Louis Lagrange.* Herausgegeben von Heinrich Weber. B. G. Teubner. Leipzig and Berlin. 1911. Leonhardi Euleri Opera omnia. Series prima. Opera mathematica. Volumen primum.
    - [Zweyter Theil. Erster Abschnitt. Capitel 12. Von der Regel des Cardani oder des Scipionis Ferrei](/EulerAlgebra/de/II-I-12.pdf)