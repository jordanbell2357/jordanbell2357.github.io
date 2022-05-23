---
layout: post
title: Euler, "Elements of Algebra", Section IV, Chapter 10
---

### Leonhard Euler, *Elements of Algebra* (*Vollständige Anleitung zur Algebra*)

#### Section IV. "Of Algebraic Equations, and the Resolution of Them." Chapter 10. "Of Pure Equations of the Third Degree."

**706.** An equation of the third degree is said to be pure,
when the cube of the unknown quantity is equal to a known
quantity, and when neither the square of the unknown
quantity, nor the unknown quantity itself, is found in the
equation; so that $$x^3=125$$, or, more generally, $$x^3=a$$,
$$x^3=\dfrac{a}{b}$$, etc. are equations of this kind.

**707.** It is evident how we are to deduce the value of
$$x$$ from such an equation, since we have only to extract the
cube root of both sides. Thus, the equation $$x^3=125$$ gives
$$x=5$$, the equations $$x^3=a$$ gives 
$$x=\sqrt[3]{\vphantom{a}}a$$, and the equation
$$x^3=\dfrac{a}{b}$$ gives
$$x=\sqrt[3]{\vphantom{\dfrac{a}{b}}}\dfrac{a}{b}$$,
or $$x=\dfrac{\sqrt[3]{\vphantom{a}}a}{\vphantom{b}}b}$$.
To be able,
therefore, to resolve such equations, it is sufficient that we
know how to extract the cube root of a given number.

**708.** But in this manner, we obtain only one value for $$x$$:
but since every equation of the second degree has two
values, there is reason to suppose that an equation of the
third degree has also more than one value.
It will be deserving our attention to investigate this; and, if we find that
in such equations $$x$$ must have several values, it will be necessary to determine those values.

**709.** Let us consider, for example, the equation $$x^3=8$$,
with a view of deducing from it all the numbers, whose cubes
are, respectively, 8. As $$x=2$$ is undoubtedly such a number, what has
been said in the last chapter shows that the quantity $$x^3-8=0$$,
must be divisible by $$x-2$$:
let us
therefore perform this division.

<a href="https://artofproblemsolving.com/texer/nqyxzgxd">
<img src="/assets/euler/nqyxzgxd.png" alt="Polynomial long division" width="247" height="205" style="display:block;margin-left:auto;margin-right:auto;">
</a>

Hence it follows, that our equation, $$x^3=8$$,
may be represented by these factors;

$$(x-2)(x^2+2x+4)=0.$$

**710.** Now, the question is, to know what number we arc
to substitute instead of $$x$$, in order that $$x^3=8$$,
or that $$x^3-8=0$$;
and it is evident that this condition is answered, by supposing the product which we
have just now found equal to 0; but this happens, not only when the first factor
$$x-2=0$$, which gives us $$x=2$$, but also when the
second factor $$x^2+2x+4=0$$. Let us, therefore, make
$$x^2+2x+4=0$$; then we shall have $$x^2=-2x-4$$, and thence
$$x=-1 \pm \surd -3$$.

**711.** So that beside the case, in which $$x=2$$,
which corresponds to the equation $$x^3=8$$,
we have two other values of $$x$$,
the cubes of which are also 8; and these are,

$$\textrm{I} \: x= -1+\surd -3,\qquad
\textrm{II} \: x= -1-\surd -3,$$

as will be
evident, by actually cubing these expressions

$$
\begin{array}{rrr}
-1&+\surd -3&\\
-1&+\surd -3&\\ \hline
1&-\surd -3&\\
&-\surd -3&-3\\ \hline
-2&-2\surd -3
\end{array}
$$

$$
\begin{array}{rrr}
-2&-2\surd -3&\\
-1&+\surd -3&\\ \hline
2&+2\surd -3&\\
&-2\surd -3&+6\\ \hline
8&&
\end{array}
$$

$$
\begin{array}{rrr}
-1&-\surd -3&\\
-1&-\surd -3&\\ \hline
1&+\surd -3&\\
&+\surd -3&-3\\ \hline
-2&+2\surd -3&
\end{array}
$$

$$
\begin{array}{rrr}
-2&+2\surd -3&\\
-1&-\surd -3&\\ \hline
2&-2\surd -3&\\
&+2\surd -3&+6\\ \hline
8&&
\end{array}
$$

It is true, that these values are imaginary, or impossible;
but yet they deserve attention.

712. What we have said applies in general to every cubic
equation, such as $$x^3=a$$; namely, that beside the value
$$x=\sqrt[3]{\vphantom{a}}a$$, we shall always find two other values.
To abridge the calculation, let us suppose $$\sqrt[3]{\vphantom{a}}a=c$$,
so that $$a=c^3$$, our
equation will then assume this form,
$$x^3-c^3=0$$, hich
will be divisible by $$x-c$$,
as the actual division shows

<a href="https://artofproblemsolving.com/texer/chcvtqld">
<img src="/assets/euler/chcvtqld.png" alt="Polynomial long division" width="258" height="205" style="display:block;margin-left:auto;margin-right:auto;">
</a>

#### References

1. Leonhard Euler, *Elements of Algebra*, Translated by Rev. John Hewlett. Longmans, Hurst, Rees, Orme, and Co., London, 1822.
    - [Section IV. Chapter 10. "Of Pure Equations of the Third Degree."](/assets/euler/en/IV-10.pdf)
    - [Archive.org](https://archive.org/details/elementsofalgebr00euleuoft/)
3. Leonhard Euler. *Vollständige Anleitung zur Algebra. Mit den Zusätzen von Joseph Louis Lagrange.* Herausgegeben von Heinrich Weber. B. G. Teubner. Leipzig and Berlin. 1911. Leonhardi Euleri Opera omnia. Series prima. Opera mathematica. Volumen primum.
    - [Zweyter Theil. Erster Abschnitt. Capitel 10. Von der Auflösung der reinen cubischen Gleichungen](/assets/euler/de/II-I-10.pdf)
    - [Springer](https://link.springer.com/book/9783764314002)
2. Leonhard Euler, *Vollständige Anleitung zur Algebra. Zweyter Theil. Von Auflösung algebraischer Gleichungen und der unbestimmten Analytic*, Kays. Acad. der Wissenschaften, St. Petersburg, 1770.
    - [Deutsches Textarchiv](https://www.deutschestextarchiv.de/euler_algebra02_1770)