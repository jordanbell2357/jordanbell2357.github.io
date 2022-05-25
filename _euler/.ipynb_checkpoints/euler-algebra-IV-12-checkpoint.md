---
layout: post
title: Euler, "Elements of Algebra", Section IV, Chapter 12
---

### Leonhard Euler, *Elements of Algebra* (*Vollständige Anleitung zur Algebra*)

#### Section IV. "Of Algebraic Equations, and the Resolution of Them." Chapter 12. "Of the Rule of Cardano, or of Scipione del Ferro."

**734.** When we have removed fractions from an equation
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

**735.** As in those fractions the roots of the equation are
neither integer numbers, nor fractions, they are irrational,
and, as it often happens, imaginary. The manner, therefore, of expressing them,
and of determining the radical
signs which affect them, forms a very important point, and
deserves to be carefully explained. This method, called *Cardano's Rule*,
is ascribed to Cardano, or more properly to Scipione del Ferro,
both of whom lived some centuries since.

**736.** In order to understand this rule, we must first attentively consider
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

**737.** Let us now suppose $$x=a+b$$;
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

**738.** Farther, let us now suppose $$a^3=p$$ and $$b^3=q$$;
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

**739.** Let, in general, the equation $$x^3=fx+g$$
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

**740.** We have therefore to resolve these two equations,

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

**741.** In a cubic equation, therefore, of the form
$$x^3=fx+g$$,
whatever be the numbers
$$f$$ and $$g$$,
we have always
for one of the roots


#### References

1. Leonhard Euler, *Elements of Algebra*, Translated by Rev. John Hewlett. Longmans, Hurst, Rees, Orme, and Co., London, 1822.
    - [Section IV. Chapter 12. "Of the Rule of Cardano, or of Scipione del Ferro."](/assets/euler/en/IV-12.pdf)
    - [Archive.org](https://archive.org/details/elementsofalgebr00euleuoft/)
3. Leonhard Euler. *Vollständige Anleitung zur Algebra. Mit den Zusätzen von Joseph Louis Lagrange.* Herausgegeben von Heinrich Weber. B. G. Teubner. Leipzig and Berlin. 1911. Leonhardi Euleri Opera omnia. Series prima. Opera mathematica. Volumen primum.
    - [Zweyter Theil. Erster Abschnitt. Capitel 12. Von der Regel des Cardani oder des Scipionis Ferrei](/assets/euler/de/II-I-12.pdf)
    - [Springer](https://link.springer.com/book/9783764314002)
2. Leonhard Euler, *Vollständige Anleitung zur Algebra. Zweyter Theil. Von Auflösung algebraischer Gleichungen und der unbestimmten Analytic*, Kays. Acad. der Wissenschaften, St. Petersburg, 1770.
    - [Deutsches Textarchiv](https://www.deutschestextarchiv.de/euler_algebra02_1770)