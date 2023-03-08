---
layout: page
title: Chapter 12. "Of the Expression of Irrational Powers by Infinite Series."
part: I
section: II
chapter: 12
---

### Part {{ page.part }}. Section {{ page.section }}. {{ page.title }}

<span class="art">361</span> As we have shewn the method of finding any power
of the root $$a + b$$, however great the exponent may be, we
are able to express, generally, the power of $$a + b$$ whose
exponent is undetermined; for it is evident that if we
represent that exponent by $$n$$, we shall have by the rule already
given (<span class="artref">Art. 348</span> and the following):

$$
\begin{align}
(a+b)^n &= a^n + \frac{n}{1}a^{n-1}b+\frac{n}{1}\cdot \frac{n-1}{2} a^{n-2}b^2\\
&+\frac{n}{1}\cdot \frac{n-1}{2} \cdot \frac{n-2}{3} a^{n-3}b^3\\
&+\frac{n}{1}\cdot \frac{n-1}{2} \cdot \frac{n-2}{3} \cdot \frac{n-3}{4} a^{n-4}b^4
+\textrm{etc.}
\end{align}
$$


<span class="art">362</span> If the same power of the root $$a-b$$ were required,
we need only change the signs of the second, fourth,
sixth, etc. terms, and should have

$$
\begin{align}
(a-b)^n &= a^n - \frac{n}{1}a^{n-1}b+\frac{n}{1}\cdot \frac{n-1}{2} a^{n-2}b^2\\
&-\frac{n}{1}\cdot \frac{n-1}{2} \cdot \frac{n-2}{3} a^{n-3}b^3\\
&+\frac{n}{1}\cdot \frac{n-1}{2} \cdot \frac{n-2}{3} \cdot \frac{n-3}{4} a^{n-4}b^4
-\textrm{etc.}
\end{align}
$$

<span class="art">363</span> These formulas are remarkably useful, since they
serve also to express all kinds of radicals; for we have shown
that all irrational quantities may assume the form of powers
whose exponents are fractional, and that
$$\sqrt[2]{\vphantom{a}}a=a^{\frac{1}{2}}$$,
$$\sqrt[3]{\vphantom{a}}a=a^{\frac{1}{3}}$$,
$$\sqrt[4]{\vphantom{a}}a=a^{\frac{1}{4}}$$,
etc.: we have, therefore,

$$\sqrt[2]{\vphantom{(a+b)}}(a+b)=(a+b)^{\frac{1}{2}};
\; \sqrt[3]{\vphantom{(a+b)}}(a+b)=(a+b)^{\frac{1}{3}};
\; \sqrt[4]{\vphantom{(a+b)}}(a+b)=(a+b)^{\frac{1}{4}},
\; \textrm{etc.}$$

Consequently, if we wish to find the square root of $$a+b$$,
we have only to substitute for the exponent $$n$$ the fraction
½ in the general formula, <span class="artref">Art. 361</span>, and we shall have first, for
the coefficients,

$$\frac{n}{1}=\frac{1}{2}; \; \frac{n-1}{2}=-\frac{1}{4}; \;
\frac{n-2}{3}=-\frac{3}{6}; \; \frac{n-3}{4}=-\frac{5}{8}; \;
\frac{n-4}{5}=-\frac{7}{10}; \; \frac{n-5}{6}=-\frac{9}{12}.$$

Then $$a^n=a^{\frac{1}{2}}=\surd a$$ and $$a^{n-1}=\dfrac{1}{\surd a}$$;
$$a^{n-2}=\dfrac{1}{a\surd a}$$; $$a^{n-3}=\dfrac{1}{a^2 \surd a}$$, etc.
or we might express those powers of $$n$$ in the following manner:
$$a^n=\surd a$$; $$a^{n-1}=\dfrac{\surd a}{a}$$; $$a^{n-2}=\dfrac{a^n}{a^2}=\dfrac{\surd a}{a^2}$$;
$$a^{n-3}=\dfrac{a^n}{a^3} = \dfrac{\surd a}{a^3}$$;
$$a^{n-4}=\dfrac{a^n}{a^4} = \dfrac{\surd a}{a^4}$$, etc.

<span class="art">364</span> This being laid down, the square root of $$a + b$$ may
be expressed in the following manner:

$$\surd(a+b) = \surd a - \frac{1}{2}b \dfrac{\surd a}{a}-\frac{1}{2} \cdot \frac{1}{4} b^2 \dfrac{\surd a}{aa}
+\frac{1}{2}\cdot \frac{1}{4}\cdot \frac{3}{6}b^3 \dfrac{\surd a}{a^3}
-\frac{1}{2}\cdot \frac{1}{4}\cdot \frac{3}{6}\cdot \frac{5}{8} b^4 \dfrac{\surd a}{a^4},
\; \textrm{etc.}$$

<span class="art">365</span> If $$a$$ therefore be a square number, we may assign
the value of $$\surd a$$, and, consequently, the square
root of $$a+b$$ may be expressed by an infinite series, without
any radical sign.

Let, for example, $$a=c^2$$, we shall have $$\surd a=c$$;
then

$$\surd(c^2+b) = c + \frac{1}{2} \cdot \dfrac{b}{c} - \frac{1}{8} \cdot \dfrac{b^2}{c^3}
+\frac{1}{16} \cdot \dfrac{b^3}{c^5} - \frac{5}{128} \cdot \dfrac{b^4}{c^7},
\; \textrm{etc.}$$

We see, therefore, that there is no number, whose square
root we may not extract in this manner; since every number
may be resolved into two parts, one of which is a square represented
by $$c^2$$. If, for example, the square root of 6 be
required, we make 6 = 4 + 2, consequently, $$c^2=4$$, $$c = 2$$,
$$b = 2$$, whence results

√6 = 2 + ½ - ¹⁄₁₆ + ¹⁄₆₄ - ⁵⁄₁₀₂₄ + etc.

If we take only the two leading terms of this series, we
shall have 2½ = ⁵⁄₂, the square of which, ²⁵⁄₄,
is ¼ greater
than 6; but if we consider three terms, we have
2⁷⁄₁₆ = ³⁹⁄₁₆, the square of which, ¹⁵²¹⁄₂₅₆, is still
¹⁵⁄₂₅₆ too small.

<span class="art">366</span> Since, in this example, ⁵⁄₂
approaches very nearly to the true value of √6, we shall
take for 6 the equivalent quantity ²⁵⁄₄ - ¼;
thus $$c^2=\frac{25}{4}$$; $$c=\frac{5}{2}$$; $$b=\frac{1}{4}$$;
and calculating only the two leading terms,
we find

$$\surd 6 = \frac{5}{2}+\frac{1}{2}\cdot \dfrac{-\frac{1}{4}}{\frac{5}{2}} = \frac{5}{2} - \frac{1}{2} \cdot
\dfrac{\frac{1}{4}}{\frac{5}{2}} = \frac{5}{2} - \frac{1}{20} = \frac{49}{20},$$

the square of which fraction being ²⁴⁰¹⁄₄₀₀, it exceeds the square of
√6 only by ¹⁄₄₀₀.

Now, making 6 = ²⁴⁰¹⁄₄₀₀ - ¹⁄₄₀₀, so that $$c=\frac{49}{20}$$ and $$b=-\frac{1}{400}$$;
and still taking only the two leading terms, we have

$$\surd 6 = \frac{49}{20} + \frac{1}{2} \cdot \dfrac{-\frac{1}{400}}{\frac{49}{20}}
=\frac{49}{20} - \frac{1}{2} \cdot \dfrac{\frac{1}{400}}{\frac{49}{20}} = \frac{49}{20}
-\frac{1}{1960} = \frac{4801}{1960},$$

the square of which is ²³⁰⁴⁹⁶⁰¹⁄₃₈₄₁₆₀₀; and 6,
when reduced to the same denominator, is = ²³⁰⁴⁹⁶⁰⁰⁄₃₈₄₁₆₀₀;
the error therefore is only ¹⁄₃₈₄₁₆₀₀.

<span class="art">367</span> In the same manner, we may express the cube root of
$$a+b$$ by an infinite series; for since $$\surd[3]{\vphantom{(a+b)}}(a+b) = (a+b)^{\frac{1}{3}$$,
we shall have in the general formula, $$n=\frac{1}{2}$$, and for the coefficients,

$$\frac{n}{1}=\frac{1}{3}; \; \frac{n-1}{2}=-\frac{1}{3}; \; \frac{n-2}{3}=-\frac{5}{9}; \;
\frac{n-3}{4} = -\frac{2}{3}; \; \frac{n-4}{5}= - \frac{11}{15}; \quad \textrm{etc.}$$

and, with regard to the powers of $$a$$, we shall have

$$a^n = \sqrt[3]{\vphantom{a}}a; \; a^{n-1} = \dfrac{\sqrt[3]{\vphantom{a}}a}{a}; \;
a^{n-2} = \dfrac{\sqrt[3]{\vphantom{a}}a}{a^2}; \;
a^{n-3} = \dfrac{\sqrt[3]{\vphantom{a}}a}{a^3}; \quad \textrm{etc.}$$

then

$$\sqrt[3]{\vphantom{(a+b)}} = \sqrt[3]{\vphantom{a}} + \frac{1}{3} \cdot b \dfrac{\sqrt[3]{\vphantom{a}}a}{a}
-\frac{1}{9} \cdot b^2 \dfrac{\sqrt[3]{\vphantom{a}}a}{a^2}
+\frac{5}{81} \cdot b^3 \dfrac{\sqrt[3]{\vphantom{a}}a}{a^3}
-\frac{10}{243} \cdot b^4 \dfrac{\sqrt[3]{\vphantom{a}}a}{a^4},
\quad \textrm{etc.}$$

<span class="art">368</span> If $$a$$ therefore be a cube, or $$a=c^3$$,
we have $$\sqrt[3]{\vphantom{a}}=c$$,
and the radical signs will vanish; for we shall have

$$\sqrt[3]{\vphantom(c^3+b)}} (c^3+b) = c + \frac{1}{3} \cdot \frac{b}{c^2}-\frac{1}{9} \cdot \frac{b^2}{c^5}
+\frac{5}{81} \codt \frac{b^3}{c^8} - \frac{10}{243} \cdot \frac{b^4}{c^11}
+\textrm{etc.}$$

<span class="art">369</span> We have therefore arrived at a formula, which will
enable us to find, by approximation, the cube root of any
number; since every number may be resolved into two parts,
as $$c^3+b$$, the first of which is a cube.

If we wish, for example, to determine the cube root of 2,
we represent 2 by 1 + 1, so that $$c=1$$ and $$b=1$$;
consequently,

$$\sqrt[3]{\vphantom{2}} 2 = 1 + \frac{1}{3} - \frac{1}{9} + \frac{5}{81}, \textrm{etc.}$$

The two leading terms of this series make 1⅓ = ⁴⁄₃, the cube of which ⁶⁴⁄₂₇
is too great by ¹⁰⁄₂₇: let us therefore make 2 = ⁶⁴⁄₂₇ - ¹⁰⁄₂₇, we have
$$c=\frac{4}{3}$$ and $$b=-\frac{10}{27}$$, and consequently,

$$\sqrt[3]{\vphantom{2}} 2 = \frac{4}{3} + \frac{1}{3} \cdot \dfrac{-\frac{10}{27}}{\frac{16}{9}}:$$

two two terms give ⁴⁄₃ - ⁵⁄₇₂ = ⁹¹⁄₇₂, the cube of which is ⁷⁵³⁵⁷¹⁄₃₇₃₂₄₈:
but, 2 = ⁷⁴⁶⁴⁹⁶⁄₃₇₃₂₄₈, so that the error is
⁷⁰⁷⁵⁄₃₇₃₂₄₈; and in this way we might still approximate, the faster
in proportion as we take a greater number of terms.

#### Editions

1. Leonhard Euler. *Elements of Algebra*. Translated by Rev. John Hewlett. Third Edition. Longmans, Hurst, Rees, Orme, and Co. London. 1822.
    - [Part {{ page.part }}. Section {{ page.section }}. {{ page.title }}](/EulerAlgebra/en/II-12.pdf)
2. Leonhard Euler. *Vollständige Anleitung zur Algebra. Mit den Zusätzen von Joseph Louis Lagrange.* Herausgegeben von Heinrich Weber. B. G. Teubner. Leipzig and Berlin. 1911. Leonhardi Euleri Opera omnia. Series prima. Opera mathematica. Volumen primum.
    - [Erster Theil. Zweyter Abschnitt. Capitel 12. Von der Entwickelung der irrationalen Potestäten durch unendliche Reihen](/EulerAlgebra/de/I-II-12.pdf)