---
layout: post
title: Euler, "Elements of Algebra", Section IV, Chapter 4
topic: euler
---

### Leonhard Euler, *Elements of Algebra* (*Vollständige Anleitung zur Algebra*)

#### Section IV. "Of Algebraic Equations, and the Resolution of Them." Chapter 4. "Of the Resolution of two or more Equations of the First Degree."

> **605.** It frequently happens that we are obliged to introduce into algebraic calculations
> two or more unknown quantities, represented by the letters $$x$$, $$y$$, $$z$$: and if the question
> is determinate, we are brought to the same number of equations as there are unknown quantities;
> from which it is then required to deduce those quantities. As we consider, at present, those
> equations only, which contain no powers of an unknown quantity higher than the first, and no
> products of two or more unknown quantities, it is evident that all those equations have the
> form $$az+by+cx=d$$.
>
> **606.** Beginning therefore with two equations, we shall
> endeavour to find from them the value of $$x$$ and $$y$$: and, in
> order that we may consider this case in a general manner, let
> the two equations be,
>
> I) $$ax + by = c$$; and II) $$fx + gy = h$$;
>
> in which, $$a$$, $$b$$, $$c$$, and $$f$$, $$g$$, $$h$$, are known numbers. It is
> required, therefore, to obtain, from these two equations, the
> two unknown quantities $$x$$ and $$y$$.
>
> **607.** The most natural method of proceeding will readily
> present itself to the mind; which is, to determine, from both
> equations, the value of one of the unknown quantities, as for
> example $$x$$, and to consider the equality of those two values;
> for then we shall have an equation, in which the unknown
> quantity $$y$$ will be found by itself, and may be determined
> by the rules already given. Then, knowing $$y$$, we shall have
> only to substitute its value in one of the quantities that
> express $$x$$.
>
> **608.** According to this rule, wo obtain from the first
> equation, $$x=\dfrac{c-by}{a}$$, and from the second, $$x=\dfrac{h-gy}{f}$$:
> then putting these vaues equal to each other, we have this
> new equation: $$\dfrac{c-by}{a}=\dfrac{h-gy}{f}$$;
> multiplying by $$a$$, the product is $$c-by=\dfrac{ah-agy}{f}$$; and then by $$f$$,
> the product is $$fc-fby = ah-agy$$; adding $$agy$$, we have $$fc-fby+agy = ah$$; subtracting $$fc$$,
> gives $$-fby+agy = ah-fc$$; or $$(ag-bf)y = ah-fc$$; lastly, dividing by $$ag-bf$$, we have
>
> $$y = \dfrac{ah-fc}{ag-bf}$$.
>
> In order now to substitute this value of $$y$$ in one of the
> two values which we have found of $$x$$, as in the first, where
> $$x=\dfrac{c-by}{a}$$, we shall first have
>
> $$-by = - \dfrac{abh-bcf}{ag-bf}$$;
>
> whence
>
> $$c-by= c- \dfrac{abh-bcf}{ag-bf}=\dfrac{acg-bcf-abh+bcf}{ag-bf}=\dfrac{acg-abh}{ag-bf}$$;
> 
> and dividing by $$a$$,
>
> $$x = \dfrac{c-by}{a} = \dfrac{cg-bh}{ag-bf}$$.
>
> **609.** *Question 1.* To illustrate this method by examples,
> let it be proposed to find two numbers, whose sum may be
> 15, and difference 7.
>
> Let us call the greater number $$x$$, and the less $$y$$: then we shall have
>
> $$x + y = 15$$, and $$x - y =7$$.
>
> The first equation gives
>
> $$x = 15 - y$$
>
> and the second,
>
> $$x = 7 + y$$;
>
> whence results this equation,
>
> $$15-y = 7 + y$$.
>
> So that $$15 = 7 + 2y$$; $$2y = 8$$, and $$y=4$$; by which means we find $$x = 11$$.
>
> So that the less number is 4, and the greater is 11.
>
> **610.** *Question 2.* We may also generalise the preceding
> question, by requiring two numbers, whose sum may be $$a$$,
> and the difference $$b$$.
>
> Let the greater of the two numbers be expressed by $$x$$, and
> the less by $$y$$; we shall then have
>
> $$x+y=a$$, and $$x-y=b$$.
>
> Here the first equation gives $$x = a — y$$, and the second $$x = b + y$$.
>
> Therefore, $$a-y=b+y$$; $$a=b+2y$$; $$2y=a-b$$; lastly,
>
> $$y=\dfrac{a-b}{2}$$,
>
> and, consequently,
>
> $$x=a-y = a-\dfrac{a-b}{2}=\dfrac{a+b}{2}$$.
>
> Thus, we find the greater number, or $$x$$, is $$\dfrac{a+b}{2}$$,
> and the less, or $$y$$, is $$\dfrac{a-b}{2}$$; or, which comes to the same,
>
> $$x= \frac{1}{2}a+\frac{1}{2}b$$, and $$y=\frac{1}{2}a-\frac{1}{2}b$$.
>
> Hence we derive the following
> theorem: When the sum of any two numbers is $$a$$, and their
> difference is $$b$$, the greater of the two numbers will be equal
> to half the sum plus half the difference; and the less of the
> two numbers will be equal to half the sum minus half the
> difference.
>
> **611.** We may resolve the same question in the following manner:
>
> Since the two equations are,
>
> $$x+y=a$$, and $$x-y=b$$;
>
> if we add the one to the other, we have
>
> $$2x=a+b$$.
>
> Therefore $$x=\dfrac{a+b}{2}$$.
>
> Lastly, subtracting the same equations from each other,
> we have
>
> $$2y=a-b$$;
>
> and therefore
>
> $$y=\dfrac{a-b}{2}$$.
>
> **612.** *Question 3.* A mule and an ass were carrying
> burdens amounting to several hundred weight. The ass
> complained of his, and said to the mule, I need only one
> hundred weight of your load, to make mine twice as heavy
> as yours; to which the mule answered, But if you give
> me a hundred weight of yours, I shall be loaded three times
> as much you will be. How many hundred weight did each
> carry?
>
> Suppose the mule's load to be $$x$$ hundred weight, and that
> of the ass to be $$y$$ hundred weight. If the mule gives one
> hundred weight to the ass, the one will have $$y + 1$$, and there
> will remain for the other $$x - 1$$; and since, in this case,
> the ass is loaded twice as much as the mule, we have $$y + 1 = 2x - 2$$.
>
> Farther, if the ass gives a hundred weight to the mule,
> the latter has $$x + 1$$, and the ass retains $$y — 1$$; but the
> burden of the former being now three times that of the
> latter, we have $$x + 1 = 3y - 3$$.
>
> Consequently our two equations will be,
>
> $$y + 1 = 2x-2$$, and $$x+1=3y-3$$.
>
> From the first, $$x=\dfrac{y+3}{2}$$, and the second gives
> $$x = 3y-4$$; whence we have the new equation $$\dfrac{y+3}{2}=3y-4$$,
> which gives $$y=\dfrac{11}{5}$$; this also determines the value
> of $$x$$, which becomes $$2\dfrac{3}{5}$$.
>
> The mule therefore carried $$2\frac{3}{5}$$ hundred weight,
and the ass $$2 \frac{1}{5}$$ hundred weight.
>
> **613.** When there are three unknown numbers, and as
> many equations; as, for example,



#### References

1. Leonhard Euler, *Elements of Algebra*, Translated by Rev. John Hewlett. Longmans, Hurst, Rees, Orme, and Co., London, 1822.
    - [Chapter 4. "Of the Resolution of two or more Equations of the First Degree."](/assets/euler/chap4.pdf)
    - [Archive.org](https://archive.org/details/elementsofalgebr00euleuoft/)
2. Leonhard Euler, *Vollständige Anleitung zur Algebra. Zweyter Theil. Von Auflösung algebraischer Gleichungen und der unbestimmten Analytic*, Kays. Acad. der Wissenschaften, St. Petersburg, 1770.
    - [Deutsches Textarchiv](https://www.deutschestextarchiv.de/euler_algebra02_1770)
3. Leonhard Euler. *Vollständige Anleitung zur Algebra. Mit den Zusätzen von Joseph Louis Lagrange.* Herausgegeben von Heinrich Weber. B. G. Teubner. Leipzig and Berlin. 1911. Leonhardi Euleri Opera omnia. Series prima. Opera mathematica. Volumen primum.
    - [Capitel 4. Von Auflösung zweyer oder mehr Gleichungen vom ersten Grad.](/assets/euler/cap4.pdf)
    - [Springer](https://link.springer.com/book/9783764314002)
5. [Ian Bruce: Euler's Algebra](https://www.17centurymaths.com/contents/euleralgebra.htm)