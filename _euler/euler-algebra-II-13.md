---
layout: post
title: Euler, "Elements of Algebra", Section II, Chapter 13. "Of the Resolution of Negative Powers."
---

### Leonhard Euler, *Elements of Algebra* (*Vollständige Anleitung zur Algebra*)

#### Section II. "Of the different Methods of calculating Compound Quantities." Chapter 13. "Of the Resolution of Negative Powers."

<span class="art">370</span> We have already shown, that $$\frac{1}{a}$$ may be expressed 
by $$a^{-1}$$; we may therefore express $$\dfrac{1}{a+b}$$ also by $$(a+b)^{-1}$$;
so that the fraction $$\dfrac{1}{a+b}$$ may be considered as a power of $$a+b$$,
namely, that power whose exponent is -1; from which it follows, that the series already found
as the value of $$(a+b)^n$$ extends also to this case.

<span class="art">371</span> Since, therefore $$\dfrac{1}{a+b}$$ is the same as $$(a+b)^{-1}$$,
let us suppose, in the general formula, <span class="art">Art. 361</span>, $$n=-1$$;
and we shall first have, for the coefficients,

$$\frac{n}{1}=-1; \quad \frac{n-1}{2}=-1; \quad \frac{n-2}{3}=-1; \quad \frac{n-3}{4}=-1, \quad \textrm{etc.}$$

And, for the powers of $$a$$, we have

$$a^n = a^{-1}=\dfrac{1}{a}; \quad
a^{n-1} = a^{-2} = \dfrac{1}{a^2}; \quad
a^{n-2} = \frac{1}{a^3}; \quad
a^{n-3} = \frac{1}{a^4}, \quad \textrm{etc.}:$$

so that

$$(a+b)^{-1} = \dfrac{1}{a+b} = \dfrac{1}{a} - \dfrac{b}{a^2} + \dfrac{b^2}{a^3} - \dfrac{b^3}{a^4}
+\dfrac{b^4}{a^5} - \dfrac{b^5}{a^6}, \; \textrm{etc.}$$

which is the same series that we found before by division.

<span class="art">372</span> Farther, $$\dfrac{1}{(a+b)^2}$$ being the same with $$(a+b)^{-2}$$, let
us reduce this quantity also to an infinite series. For this purpose,
we must suppose $$n=-2$$, and we shall first have, for the coefficients,

$$\frac{n}{1}=-\frac{2}{1}; \quad \frac{n-1}{2}=-\frac{3}{2}; \quad \frac{n-2}{3}=-\frac{4}{3}; \quad
\frac{n-3}{4} = -\frac{5}{4}; \quad \textrm{etc.};$$

and, for the powers of $$a$$, we obtain

$$a^n=\dfrac{1}{a^2}; \quad a^{n-1}=\dfrac{1}{a^3}; \quad a^{n-2} = \dfrac{1}{a^4}; \quad a^{n-3} =  \dfrac{1}{a^5},
\quad \textrm{etc.}$$

We have therefore

$$(a+b)^{-2} = \dfrac{1}{(a+b)^2} = \dfrac{1}{a^2} - \dfrac{2\cdot b}{1\cdot a^3} + \dfrac{2\cdot 3\cdot b^2}{1\cdot 2\cdot a^4}
-\dfrac{2\cdot 3\cdot 4\cdot b^3}{1\cdot 2\cdot 3\cdot a^5}
+\dfrac{2\cdot 3\cdot 4\cdot 5\cdot b^4}{1\cdot 2\cdot 3\cdot 4\cdot a^6},
\; \textrm{etc.}$$

Now,

$$\frac{2}{1}=2; \; \dfrac{2\cdot 3}{1\cdot 2}=3; \;
\dfrac{2\cdot 3\cdot 4}{1\cdot 2\cdot 3}=4; \;
\dfrac{2\cdot 3\cdot 4\cdot 5}{1\cdot 2\cdot 3\cdot 4}=5,
\quad \textrm{etc.}$$

and consequently,

$$\dfrac{1}{(a+b)^2} = \dfrac{1}{a^2} - 2\cdot \dfrac{b}{a^3}
+3 \cdot \dfrac{b^2}{a^4} - 4\cdot \dfrac{b^3}{a^5} + 5\cdot \dfrac{b^4}{a^6}
-6\cdot \dfrac{b^5}{a^7} +7\cdot \dfrac{b^6}{a^8},
\; \textrm{etc.}$$

<span class="art">373</span> Let us proceed, and suppose $$n=-3$$, and we shall
have a series expressing the value of $$\dfrac{1}{(a+b)^3}$$,
or of $$(a+b)^{-3}$$.
Here the coefficients will be

$$\frac{n}{1} = -\frac{3}{1}; \quad
\frac{n-1}{2}=-\frac{4}{2}; \quad
\frac{n-2}{3} = -\frac{5}{3}, \quad \textrm{etc.}$$

which gives

$$
\begin{align}
\dfrac{1}{(a+b)^3}&=
\dfrac{1}{a^3} - \dfrac{3\cdot b}{1\cdot a^4} + \dfrac{3\cdot 4\cdot b^2}{1\cdot 2\cdot a^5} - \dfrac{3\cdot 4\cdot 5\cdot b^3}{1\cdot 2\cdot 3\cdot a^6}\\
&+\dfrac{3\cdot 4\cdot 5\cdot 6\cdot b^4}{1\cdot 2\cdot 3\cdot 4\cdot a^7}\\
&=\dfrac{1}{a^3}-3\cdot \dfrac{b}{a^4}+6\cdot \dfrac{b^2}{a^5}
-10\cdot \dfrac{b^3}{a^6} 
+15\cdot\dfrac{b^4}{a^7}
-21\cdot \dfrac{b^5}{a^8}
+28\cdot \dfrac{b^6}{a^9},
\; \textrm{etc.}
\end{align}
$$

If we now make $$n=-4$$; we shall have for the
coefficients

$$
\frac{n}{1} = -\frac{4}{1}; \quad
\frac{n-1}{2}=-\frac{5}{2}; \quad
\frac{n-2}{3} = -\frac{6}{3}; \quad
\frac{n-3}{4} = -\frac{7}{4}, \quad \textrm{etc.}
$$

And for the powers,

$$a^n=\dfrac{1}{a^4}; \quad a^{n-1}=\dfrac{1}{a^5}; \quad a^{n-2} = \dfrac{1}{a^6}; \quad a^{n-3} =  \dfrac{1}{a^7}; \quad a^{n-4} = \dfrac{1}{a^8},$$

whence we obtain,

$$
\begin{align}
\dfrac{1}{(a+b)^4} &= \dfrac{1}{a^4} - \dfrac{4b}{1\cdot a^5} - \dfrac{4\cdot 5\cdot b^2}{1\cdot 2\cdot a^6}\\
&- \dfrac{4\cdot 5\cdot 6\cdot b^3}{1\cdot 2\cdot 3\cdot a^7}, \; \textrm{etc.}\\
&= \dfrac{1}{a^4} - 4\dfrac{b}{a^5} + 10\dfrac{b^2}{a^6}\\
&- 20\dfrac{b^3}{a^7} + 35\dfrac{b^4}{a^8}
-56\dfrac{b^5}{a^9}+, \; \textrm{etc.}$$

<span class="art">374</span>


<span class="art">375</span>


<span class="art">376</span>


<span class="art">377</span>

#### Editions

1. Leonhard Euler. *Elements of Algebra*. Translated by Rev. John Hewlett. Third Edition. Longmans, Hurst, Rees, Orme, and Co. London. 1822.
    - [Section II. Chapter 13. "Of the Resolution of Negative Powers."](/assets/euler/en/II-13.pdf)
2. Leonhard Euler. *Vollständige Anleitung zur Algebra. Mit den Zusätzen von Joseph Louis Lagrange.* Herausgegeben von Heinrich Weber. B. G. Teubner. Leipzig and Berlin. 1911. Leonhardi Euleri Opera omnia. Series prima. Opera mathematica. Volumen primum.
    - [Erster Theil. Zweyter Abschnitt. Capitel 13. Von der Entwickelung der negativen Potestäten durch unendliche Reihen](/assets/euler/de/I-II-13.pdf)