---
layout: post
title: Euler, "Elements of Algebra", Section II, Chapter 5. "Of the Resolution of Fractions into Infinite Series."
---

### Leonhard Euler, *Elements of Algebra* (*Vollständige Anleitung zur Algebra*)

#### Section II. "Of the different Methods of calculating Compound Quantities." Chapter 5. "Of the Resolution of Fractions into Infinite Series."

<span class="art">289</span> When the dividend is not divisible by the divisor,
the quotient is expressed, as we have already observed, by a
fraction: thus, if we have to divide 1 by $$1-a$$, we obtain
the fraction $$\dfrac{1}{1-a}$$. This, however, does not prevent us from
attempting the division according to the rules that have been
given, nor from continuing it as far as we please; and we
shall not fail thus to find the true quotient, though under
different forms.

<span class="art">290</span> To prove this, let us actually divide the dividend 1
by the divisor $$1-a$$, thus

<a href="https://artofproblemsolving.com/texer/fpedyycq">
<img src="/assets/euler/fpedyycq.png" alt="Long division" width="182" height="282" style="display:block;margin-left:auto;margin-right:auto;">
</a>

<a href="https://artofproblemsolving.com/texer/zrwgmxoi">
<img src="/assets/euler/zrwgmxoi.png" alt="Long division" width="192" height="454" style="display:block;margin-left:auto;margin-right:auto;">
</a>

<span class="art">291</span> This shews that the fraction $$\dfrac{1}{1-a}$$ may be exhibited under all the following forms:

1. $$1+\dfrac{a}{1-a}$$
2. $$1+a+\dfrac{a^2}{1-a}$$
3. $$1+a+a^2+\dfrac{a^3}{1-a}$$
4. $$1+a+a^2+a^3+\dfrac{a^4}{1-a}$$
5. $$1+a+a^2+a^3+a^4+\dfrac{a^5}{1-a}$$, etc.

Now, by considering the first of these expressions, which
is $$1+\dfrac{a}{1-a}$$, and remembering that 1 is the same as
$$\dfrac{1-a}{1-a}$$, we have

$$1+\dfrac{a}{1-a}=\dfrac{1-a}{1-a}+\dfrac{a}{1-a} = \dfrac{1-a+a}{1-a} = \dfrac{1}{1-a}.$$

If we follow the same process, with regard to the second
expression, $$1+a+\dfrac{a^2}{1-a}$$, that is to say, if we reduce the
integral part $$1+a$$ to the same denominator, $$1-a$$, we shall have
$$\dfrac{1-a^2}{1-a}$$, to which if we add $$+\dfrac{a^2}{1-a}$$,
we shall have
$$\dfrac{1-a^2+a^2}{1-a}$$, that is to say, $$\dfrac{1}{1-a}$$.

In the third expression,
$$1+a+a^2+\dfrac{a^3}{1-a}$$,
the integers
reduced to the denominator
$$1-a$$ make $$\dfrac{1-a^3}{1-a}$$;
and if we add to that the fraction
$$\dfrac{a^3}{1-a}$$, we have $$\dfrac{1}{1-a}$$, as before;
therefore all these expressions are equal in value to $$\dfrac{1}{1-a}$$,
the proposed fraction.

<span class="art">292</span> This being the case, we may continue the series as
far as we please, without being under the necessity of performing any more calculations;
and thus we shall have

$$\dfrac{1}{1-a}=1+a+a^2+a^3+a^4+a^5+a^6+a^7+\dfrac{a^8}{1-a};$$

or we might continue this farther, and still go on without
end; for which reason it may be said that the proposed
fraction has been resolved into an infinite series, which is,

$$1+a+a^2+a^3+a^4+a^5+a^6+a^7+a^8+a^9+a^{10}+a^{11}+a^{12}+\textrm{etc.}$$

to infinity: and there are sufficient grounds to maintain,
that the value of this infinite series is the same as that of the
fraction $$\dfrac{1}{1-a}$$.

<span class="art">293</span> What we have said may at first appear strange;
but the consideration of some particular cases will make it
easily understood. Let us suppose, in the first place, $$a=1$$;
our series will become

1 + 1 + 1 + 1 + 1 + 1 + 1 + etc.;

and the fraction $$\dfrac{1}{1-a}$$, to which it must be equal, becomes $$\frac{1}{0}$$.
Now, we have before remarked, that $$\frac{1}{0}$$
is a number infinitely
great; which is therefore here confirmed in a satisfactory
manner. See **Articles 83** and **84**.

Again, if we suppose $$a=2$$, our series becomes

1 + 2 + 4 + 8 + 16 + 32 + 64 + etc. to infinity,

and its value must be the same as $$\dfrac{1}{1-2}$$, that is to say,
$$\dfrac{1}{-1}=-1$$;
which at first
sight will appear absurd. But it must be remarked, that if
we wish to stop at any term of the above series, we cannot do
so without annexing to it the fraction which remains. Suppose,
for example, we were to stop at 64, after having written

1 + 2 + 4 + 8 + 16 + 32 + 64,

we must add the fraction
$$\frac{128}{1-2}$$, or $$\dfrac{128}{-1}$$, or -128;
we shall therefore have 127 - 128,
that is in fact -1.

Were we to continue the series without intermission, the
fraction would be no longer considered; but, in that case,
the series would still go on.


#### References

1. Leonhard Euler, *Elements of Algebra*, Translated by Rev. John Hewlett. Longmans, Hurst, Rees, Orme, and Co., London, 1822.
    - [Section II. Chapter 5. "Of the Resolution of Fractions into Infinite Series."](/assets/euler/en/II-5.pdf)
    - [Archive.org](https://archive.org/details/elementsofalgebr00euleuoft/)
2. Leonhard Euler. *Vollständige Anleitung zur Algebra. Mit den Zusätzen von Joseph Louis Lagrange.* Herausgegeben von Heinrich Weber. B. G. Teubner. Leipzig and Berlin. 1911. Leonhardi Euleri Opera omnia. Series prima. Opera mathematica. Volumen primum.
    - [Erster Theil. Zweyter Abschnitt. Capitel 5. Von der Auflösung der Brüche in unendlichen Reihen](/assets/euler/de/I-II-5.pdf)
    - [Springer](https://link.springer.com/book/9783764314002)
3. Leonhard Euler, *Vollständige Anleitung zur Algebra*, Kayserlichen Akademie der Wissenschaften, St. Petersburg, 1771.
    - [ETH-Bibliothek Zürich](https://doi.org/10.3931/e-rara-9093)