---
layout: post
title: Euler, "Elements of Algebra", Section IV, Chapter 5
topic: euler
---

### Leonhard Euler, *Elements of Algebra* (*Vollständige Anleitung zur Algebra*)

#### Section IV. "Of Algebraic Equations, and the Resolution of Them." Chapter 5. "Of the Resolution of Pure Quadratic Equations."

> **623.** An equation is said to be of the second degree, when
> it contains the square, or the second power, of the unknown
> quantity, without any of its higher powers; and an equation,
> containing likewise the third power of the unknown
> quantity, belongs to cubic equations, and its resolution requires particular rules.
>
> **624.** There are, therefore, only three kinds of terms in
> an equation of the second degree:
>
> 1. The terms in which the unknown quantity is not
> found at all, or which is composed only of known numbers.
> 2. The terms in which we find only the first power of the
> unknown quantity.
> 3. The terms which contain the square, or the second
> power, of the unknown quantity.
>
> So that $$x$$ representing an unknown quantity, and the
> letters $$a$$, $$b$$, $$c$$, $$d$$, etc. the known quantities, the terms of
> the first kind will have the form $$a$$, the terms of the second
> kind will have the form $$bx$$, and the terms of the third kind
> will have the form $$cx^2$$.
>
> **625.** We have already seen, how two or more terms of
> the same kind may be united together, and considered as a
> single term.
>
> For example, we may consider the formula
> $$ax^2 - bx^2 + cx^2$$ as a single term, representing it thus,
> $$(a - b + c)x^2$$; since, in fact, $$(a - b + c)$$ is a known
> quantity.
>
> And also, when such terms are found on both sides of the
> sign =, we have seen how they may be brought to one side,
> and then reduced to a single term. Let us take, for example, the equation,
>
$$2x^2-3x+4=5x^2-8x+11;$$
>
> we first subtract $$2x^2$$, and there remains
>
$$-3x+4=3x^2-8x+11;$$
>
> then adding $$8x$$, we obtain,
>
$$5x+4=3x^2+11;$$
>
> lastly, subtracting 11, there remains $$3x^2 = 5x - 7$$.
>
> **626.** We may also bring all the terms to one side of the
> sign =, so as to leave zero, or 0, on the other; but it must
> be remembered, that when terms are transposed from one
> side to the other, their signs must be changed.
>
> Thus, the above equation will assume this form,
> $$3x^2-5x+7 = 0$$; and, for this reason also, the following general
> formula represents all equations of the second degree;
>
$$ax^2 \pm bx \pm c = 0;$$
>
> in which the sign ± is read plus or minus, and indicates,
> that such terms as it stands before may be sometimes
> positive, and sometimes negative.
>
> 627. Whatever therefore be the original form of a quadratic equation, it may always be reduced > to this formula of
> three terms. If we have, for example, the equation
>
$$\dfrac{ax+b}{cx+d} = \dfrac{ex+f}{gx+h}$$
>
> we may, first, destroy the fractions; multiplying, for this
> purpose, by $$cx+d$$, which gives
>
$$ax+b=\dfrac{cex^2+cfx+edx+fd}{gx+h},$$
>
then by $$gx+h$$, we have
>
$$agx^2+bgx+ahx+bh=cex^2+cfx+edx+fd,$$
>
which is an equation of the second degree, reducible to
the three following terms, which we shall transpose by arranging them in the usual manner
>
$$
\begin{Bmatrix}
ag\\
-ce
\end{Bmatrix}
x^2
+
\begin{Bmatrix}
+bg\\
+ah\\
-cf\\
-ed
\end{Bmatrix}
x
+
\begin{Bmatrix}
+bh\\
-fd
\end{Bmatrix}
=
0.
$$
>
> We may exhibit this equation also in the following form,
> which is still more clear
>
$$(ag-ce)x^2+(bg+ah-cf-ed)x+bh-fd=0.$$
>
> **628.** Equations of the second degree, in which all the
> three kinds of terms are found, are called complete, and the
> resolution of them is attended with greater difficulties; for
> which reason we shall first consider those, in which one of
> the terms is wanting.
>
> Now, if the term $$x^2$$ were not found in the equation, it
> would not be a quadratic, but would belong to those of
> which we have already treated; and if the term, which
> contains only known numbers, were wanting, the equation
> would have this form, $$ax^2 \pm bx = 0$$, which being divisible
> by $$x$$, may be reduced to $$ax \pm b = 0$$, which is likewise a
> simple equation, and belongs not to the present class.
>
> **629.** But when the middle term, which contains the first
> power of $$x$$, is wanting, the equation assumes this form,
> $$ax^2 \pm c = 0$$, or $$ax^2 = c$$; as the sign of $$c$$ may be either
> positive, or negative
>
> We shall call such an equation a pure equation of the second
> degree, and the resolution of it is attended with no difficulty;
> for we have only to divide by $$a$$, which gives $$x^2 = \dfrac{c}{a}$$; and
>
$$x=\sqrt{\dfrac{c}{a}};$$
>
> which means the equation is resolved.
>
> **630.** But there are three cases to be considered here. In
> the first, when $$\frac{c}{a}$$ is a square number (of which we can therefore really
> assign the root) we obtain for the value of $$x$$ a
> rational number, which maybe either integral, or fractional.
> For example, the equation $$x^2=144$$, gives $$x = 12$$. And
> $$x^2=\frac{9}{16}$$, gives $$x=\frac{3}{4}$$.
>
> The second case is, when $$\frac{c}{a}$$ is not a square, in which case
> we must therefore be contented with the sign $$\surd$$. If, for
> example, $$x^2 = 12$$, we have $$x =\sqrt{12}$$, the value of which
> may be determined by approximation, as we have already
> shown.
>
> The third case is that, in which $$\frac{c}{a}$$ becomes a negative
> number: the value of $$x$$ is then altogether impossible and
> imaginary \["gar unmöglich oder Imaginär"\]; and this result proves that the question, which
> leads to such an equation, is in itself impossible.
>
> **631.** We shall also observe, before proceeding farther,
> that whenever it is required to extract the square root of a
> number, that root, as we have already remarked, has always
> two values, the one positive and the other negative. Suppose,
> for example, we have the equation $$x^2 = 49$$, the value
> of $$x$$ will be not only +7, but also -7, which is expressed
> by $$x= \pm 7$$. So that all those questions admit of a double
> answer; but it will be easily perceived that in several cases,
> as those which relate to a certain number of men, the negative value cannot exist.



#### References

1. Leonhard Euler, *Elements of Algebra*, Translated by Rev. John Hewlett. Longmans, Hurst, Rees, Orme, and Co., London, 1822.
    - [Chapter 5. "Of the Resolution of Pure Quadratic Equations."](/assets/euler/chap5.pdf)
    - [Archive.org](https://archive.org/details/elementsofalgebr00euleuoft/)
2. Leonhard Euler, *Vollständige Anleitung zur Algebra. Zweyter Theil. Von Auflösung algebraischer Gleichungen und der unbestimmten Analytic*, Kays. Acad. der Wissenschaften, St. Petersburg, 1770.
    - [Deutsches Textarchiv](https://www.deutschestextarchiv.de/euler_algebra02_1770)
3. Leonhard Euler. *Vollständige Anleitung zur Algebra. Mit den Zusätzen von Joseph Louis Lagrange.* Herausgegeben von Heinrich Weber. B. G. Teubner. Leipzig and Berlin. 1911. Leonhardi Euleri Opera omnia. Series prima. Opera mathematica. Volumen primum.
    - [Capitel 5. Von der Auflösung der reinen Quadratischen Gleichungen.](/assets/euler/cap5.pdf)
    - [Springer](https://link.springer.com/book/9783764314002)
5. [Ian Bruce: Euler's Algebra](https://www.17centurymaths.com/contents/euleralgebra.htm)