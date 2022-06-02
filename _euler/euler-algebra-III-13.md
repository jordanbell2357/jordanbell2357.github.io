---
layout: post
title: Euler, "Elements of Algebra", Section III, Chapter 13. "Of the Calculation of Interest."
---

### Leonhard Euler, *Elements of Algebra* (*Vollständige Anleitung zur Algebra*)

#### Section III. "Of Ratios and Proportions." Chapter 13. "Of the Calculation of Interest."

<span class="art">540</span> We are accustomed to express the interest of any
principal by *per cents*, signifying how much interest is annually paid for the sum of 100 pounds.
And it is very usual to put out the principal sum at 5 per cent, that is, on
such terms, that we receive 5 pounds interest for every 100
pounds principal. Nothing therefore is more easy than to
calculate the interest for any sum; for we have only to say,
according to the Rule of Three:

As 100 is to the principal proposed, so is the rate *per cent* to the interest required. Let the principal,
for example, be 860*l.*, its annual interest is found by this proportion;

100:5::860:43.

Therefore 43*l.* is the annual interest.

<span class="art">541</span> We shall not dwell any longer on examples of
Simple Interest, but pass on immediately to the calculation
of Compound Interest; where the chief subject of inquiry
is, to what sum does a given principal amount, after a
certain number of years, the interest being annually added
to the principal. In order to resolve this question, we begin
with the consideration, that 100*l.* placed out at 5 per cent,
becomes, at the end of a year, a principal of 105*l.*: therefore
let the principal be $$a$$; its amount, at the end of the year,
will be found, by saying; As 100 is to $$a$$, so is 105 to the
answer; which gives

$$\dfrac{105a}{100} = \dfrac{21a}{20} = \frac{21}{20} \cdot a = a + \frac{1}{20}a.$$

<span class="art">542</span> So that, when we add to the original principal its
twentieth part, we obtain the amount of the principal
at the end of the first year: and adding to this its twentieth
part, we know the amount of the given principal at the end
of two years, and so on. It is easy, therefore, to compute the
successive and annual increases of the principal, and to continue this calculation to any length.

<span class="art">543</span> Suppose, for example, that a principal, which is at
present 1000*l.*, is put out at five per cent; that the interest
is added every year to the principal; and that it were required to find its amount at any time. As this calculation
must lead to fractions, we shall employ decimals, but without carrying them farther than the thousandth parts of a
pound, since smaller parts do not at present enter into consideration.

<table>
<thead>
  <tr>
    <th>Years</th>
    <th>Value (<em>l.</em>)</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>after 1 year</td>
    <td>1050</td>
  </tr>
  <tr>
    <td></td>
    <td>52.5</td>
  </tr>
  <tr>
    <td>after 2 years</td>
    <td>1102.5</td>
  </tr>
  <tr>
    <td></td>
    <td>55.125</td>
  </tr>
  <tr>
    <td>after 3 years</td>
    <td>1157.625</td>
  </tr>
  <tr>
    <td></td>
    <td>57.881</td>
  </tr>
  <tr>
    <td>after 4 years</td>
    <td>1215.506</td>
  </tr>
  <tr>
    <td></td>
    <td>60.775</td>
  </tr>
</tbody>
</table>

which sums are formed by always adding ¹⁄₂₀ of the preceding principal.

<span class="art">544</span> We may continue the same method, for any number
of years; but when this number is very great, the calculation becomes long and tedious; but it may always be
abridged, in the following manner:

Let the present principal be $$a$$, and since a principal of
20*l.* amounts to 21*l.* at the end of a year, the principal $$a$$ will
amount to $$\frac{21}{20}\cdot a$$ at the end of a year: and the same principal
will amount, the following year, to $$\frac{21^2}{20^2}\cdot a=\left(\frac{21}{20}\right)^2 \cdot a$$.
Also, this principal of two years will amount to $$\left(\frac{21}{20}\right)^3 \cdot a$$, the
year after: which will therefore be the principal of three
years; and still increasing in the same manner, the given
principal will amount to $$\left(\frac{21}{20}\right)^4 \cdot a$$ at the end of four years;
to $$\left(\frac{21}{20}\right)^5 \cdot a$$, at the end of five years; and after a century,
it will amount to $$\left(\frac{21}{20}\right)^{100} \cdot a$$; so that, in general, $$\left(\frac{21}{20}\right)^n \cdot a$$
will be the amount of this principal, after $$n$$ years; and this
formula will serve to determine the amount of the principal,
after any number of years,
    
<span class="art">545</span> The fraction ²¹⁄₂₀, which is used in this calculation,
depends on the interest having been reckoned at 5 per cent.,
and on ²¹⁄₂₀ being equal to ¹⁰⁵⁄₁₀₀. But if the interest were
estimated at 6 per cent, the principal $$a$$ would amount to
$$\frac{106}{100}\cdot a$$, at the end of a year; to $$\left(\frac{106}{100}\right)^2\cdot a$$, at the end of
two years; and to $$\left(\frac{106}{100}\right)^n \cdot a$$, at the end of $$n$$ years.
    
If the interest is only at 4 per cent, the principal $$a$$ will
amount only to $$\left(\frac{104}{100}\right)^n \cdot a$$, after $$n$$ years.
    
<span class="art">546</span> When the principal $$a$$, as well as the number of
years, is given, it is easy to resolve these formulae by logarithms. For if the question be according to our first supposition,
we shall take the logarithm of $$\left(\frac{21}{20}\right)^n \cdot a$$, which is

$$=\log \left(\frac{21}{20}\right)^n + \log a;$$

because the given formula is the
product of $$\left(\frac{21}{20}\right)^n$$ and $$a$$. Also, as $$\left(\frac{21}{20}\right)^n$$ is a power, we shall
have $$\log \left(\frac{21}{20}\right)^n=n \log \frac{21}{20}$$: so that the logarithm of the
amount required is $$n \log \frac{21}{20} + \log a$$; and farther, the
logarithm of the fraction $$\frac{21}{20}$$ equals $$\log 21 - \log 20$$.
    
<span class="art">547</span> Let now the principal be lOOO*l.* and let it be required
to find how much this principal will amount to at the end of
100 years, reckoning the interest at 5 per cent.
    
Here we have $$n = 100$$; and, consequently, the logarithm
of the amount required will be $$100\log \frac{21}{20} + \log 1000$$,
which is calculated thus:

Subtracting

$$
\begin{array}{rr}
\log 21&=1.3222193\\
\log 20&=1.3010300\\ \hline
\log \frac{21}{20}&=0.0211893.
\end{array}
$$

Multiplying by 100

$$100\log \frac{21}{20} = 0.021189300.$$

Adding $$\log 1000$$,

$$
\begin{array}{rr}
100\log \frac{21}{20}&=0.021189300\\
\log 1000&=3.0000000\\ \hline
100\log \frac{21}{20}+\log 1000&=5.1189300
\end{array}
$$

which is the logarithm of the principal required.

We perceive, from the characteristic of this logarithm,
that the principal required will be a number consisting of
six figures, and it is found to be 131501*l.*
    
<span class="art">548</span> Again, suppose a principal of 3452*l.* were put out at
6 per cent, what would it amount to at the end of 64 years?
    
We have here $$a=3452$$, and $$n=64$$. Wherefore the
logarithm of the amount sought is
    
    
    
And taking the number of this logarithm, we find the
amount required equal to 143763*l.*

<span class="art">549</span> When the number of years is very great, as it is required to multiply this number by the logarithm of a fraction, a considerable error might arise from the logarithms in
the Tables not being calculated beyond 7 figures of decimals
;
for which reason it will be necessary to employ logarithms
carried to a greater number of figures, as in the following
example.
    
A principal of \l. being placed at 5 per cent., compound
interest, for 500 years, it is required to find to what sum this
principal will amount, at the end of that period.

    
We have here a = 1 and n = 500; consequently, the
logarithm of the principal sought is equal to 500 log. ^ -flog: 1, which produces this calculation :
    
<span class="art">550</span> If we not only add the interest annually to the principal, but also increase it every year by a new sum b, the
original principal, which we call a, would increase each year
in the following; manner
    

    
    
    
    
<span class="art">551</span> The resolution of this formula requires us to calculate, separately, its first term (|-^)" x (a -f- ^06), which is
n log. -Q- + /o"\ {a -j- 206) ; for the number which answers
to this logarithm in the Tables, will be the first term ; and
if from this we subtract 206, we shall have the amount
sought.
    
<span class="art">552</span> A person has a principal of 1000/. placed out at
five per cent, compound interest, to which he adds annually
100/. beside the interest : what will be the amount of this
principal at the end of twenty-five years ?


#### References

1. Leonhard Euler, *Elements of Algebra*, Translated by Rev. John Hewlett. Longmans, Hurst, Rees, Orme, and Co., London, 1822.
    - [Section III. Chapter 13. "Of the Calculation of Interest."](/assets/euler/en/III-13.pdf)
    - [Archive.org](https://archive.org/details/elementsofalgebr00euleuoft/)
2. Leonhard Euler. *Vollständige Anleitung zur Algebra. Mit den Zusätzen von Joseph Louis Lagrange.* Herausgegeben von Heinrich Weber. B. G. Teubner. Leipzig and Berlin. 1911. Leonhardi Euleri Opera omnia. Series prima. Opera mathematica. Volumen primum.
    - [Erster Theil. Dritter Abschnitt. Capitel 13. Von den Interessen-Rechnungen](/assets/euler/de/I-III-13.pdf)
    - [Springer](https://link.springer.com/book/9783764314002)
3. Leonhard Euler, *Vollständige Anleitung zur Algebra*, Kayserlichen Akademie der Wissenschaften, St. Petersburg, 1771.
    - [ETH-Bibliothek Zürich](https://doi.org/10.3931/e-rara-9093)