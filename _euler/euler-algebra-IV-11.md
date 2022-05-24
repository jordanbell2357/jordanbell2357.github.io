---
layout: post
title: Euler, "Elements of Algebra", Section IV, Chapter 11
---

### Leonhard Euler, *Elements of Algebra* (*Vollständige Anleitung zur Algebra*)

#### Section IV. "Of Algebraic Equations, and the Resolution of Them." Chapter 11. "Of the Resolution of Complete Equations of the Third Degree."

**719.** An equation of the third degree is called complete,
when, beside the cube of the unknown quantity, it contains
that unknown quantity itself, and its square: so that the
general formula for these equations, bringing all the terms
to one side, is

$$ax^3 \pm bx^2 \pm cx \pm d = 0.$$

And the purpose of this chapter is to show how we are to
derive from such equations the values of $$x$$, which are also
called the roots of the equation. We suppose, in the first
place, that every such an equation has three roots; since it
has been seen, in the last chapter, that this is true even with
regard to pure equations of the same degree.

**720.** We shall first consider the equation
$$x^3-6x^2+11x-6=0$$; and, since an equation of the second degree
may be considered as the product of two factors, we may
also represent an equation of tlie third degree by the product
of three tactors, which are in the present instance,

$$(x-1)(x-2)(x-3)=0;$$

since, by actually multiplying them, we obtain the given
equation; for $$(x-1)(x-2)$$ gives $$x^2-3x+2$$< and multiplying
this by $$x-3$$, we obtain $$x^3-6x^2+11x-6$$, which are the given
quantities, and which must be =0. Now, this happens, when the product
$$(x-1)(x-2)(x-3)=0$$; and, as it is sufficient for this purpose, that
one of the factors become =0, three different cases may give
this result, namely, when $$x-1=0$$, or $$x=1$$; secondly,
when $$x-2=0$$, or $$x=2$$; and thirdly, when $$x-3=0$$, or $$x=3$$.

We see immediately also, that if we substituted for $$x$$,
any number whatever beside one of the above three,
none of the three factors would become equal to 0; and,
consequently, the product would no longer be 0: which
proves that our equation can have no other root than these
three.

**721.** If it were possible, in every other case, to assign
the three factors of such an equation in the same manner,
we should immediately have its three roots. Let us, therefore, consider,
in a more general manner, these three factors, $$x-p$$, $$x-q$$, $$x-r$$.
Now, if we seek their product, the
first, multiplied by the second, gives
$$x^2-(p+q)x+pq$$, and this product, multiplied by $$x-r$$, makes

$$x^3-(p+q+r)x^2+(pq+pr+qr)x-pqr.$$

Hence, if this formula must become =0, it may happen in three cases:
the first is that in, in which $$x-p=0$$, or $$x=p$$;
and second is, when $$x-q=0$$, or $$x=q$$; the third is, when $$x-r=0$$,
or $$x=r$$.

**722.** Let us now represent the quantity found, by the
equation $$x^3-ax^2+bx-c=0$$. It is evident, in order that its
three roots may be $$x=p$$, $$x=q$$, $$x=r$$, that we must have,

1. $$a=p+q+r$$,
2. $$b=pq+pr+qr$$, and
3. $$c=pqr$$.

We perceive, from this, that the second term of the equation contains the sum of the three roots; that the third term
contains the sum of the products of the roots taken two by
two; and lastly, that the fourth term consists of the product
of all the three roots multiplied together.

From this last property we may deduce an important
truth, which is, that an equation of the third degree can
have no other rational roots than the divisors of the last
term; for, since that term is the product of the three roots,
it must be divisible by each of them: so that when we wish
to find a root by trial, we immediately see what numbers
we are to use.

For example, let us consider the equation,
$$x^3=x+6$$, or $$x^3-x-6=0$$. Now, as this equation can have no
other rational roots than numbers which are factors of the
last term 6, we have only 1, 2, 3, 6, to try with, and the
result of these trials will be as follows:

If $$x=1$$, we have 1-1-6=-6.  
If $$x=2$$, we have 8-2-6=0.  
If $$x=3$$, we have 26-3-6=18.  
If $$x=6$$, we have 216-6-6=204.

Hence we see, that $$x=2$$ is one of the roots of the given equation;
and, showing this, it is easy to find the other two;
for $$x=2$$ being one of the roots $$x-2$$ is a factor of the equation,
adn as we have only to see the other factor by means of division as follows:

<a href="https://artofproblemsolving.com/texer/uptzquhb">
<img src="/assets/euler/uptzquhb.png" alt="Polynomial long division" width="255" height="212" style="display:block;margin-left:auto;margin-right:auto;">
</a>

Since, therefore, the formula is represented by the product
$$(x-2)(x^2+2x+3)$$, it will become =0, not only when $$x-2=0$$,
or $$x=2$$, but also when $$x^2+2x+3=0$$;
and, this last
factor gives $$x^2+2x=-3$$; consequently,
$$x=-1 \pm \surd -2$$; and these are the other two roots of our equation, which are
evidently impossible, or imaginary.

**723.** The method which we have explained, is applicable
only when the first term $$x^3$$ is multiplied by 1, and the other
terms of the equation have integer coefficients; therefore, when this is not the case, we must begin by a preparation, which consists in transforming the equation into
another form having the condition required; after which, we
make the trial that has been already mentioned.

Let there be given, for example, the equation

$$x^3-3x^2+\frac{11}{4}x-\frac{3}{4}=0;$$

as it contains fourth parts, let us make $$x=\dfrac{y}{2}$$,
which will give

$$\dfrac{y^3}{8}-\dfrac{3y^2}{4}+\dfrac{11y}{8}-\dfrac{3}{4}=0,$$

and, multiplying by 8, we shall obtain the equation

$$y^3-6y^2+11y-6=0,$$

the roots of which are, as we have already seen, $$y=1$$, $$y=2$$, $$y=3$$;
whence it follows, that in the given equation, we have 
$$x=\frac{1}{2}$$, $$x=1$$, $$x=\frac{3}{2}$$.

**724.** Let there be an equation, where the coefficient of
the first term is a whole number but not 1, and whose last
term is 1; for example,

$$6x^3-11x^2+6x-1=0.$$

Here, if we divide by 6, we shall have
$$x^3-\frac{11}{6}x^2+x-\frac{1}{6}=0$$;
which equation we may clear of fractions, by the method
just explained.

First, by making $$x=\dfrac{y}{6}$$, we shall have

$$\dfrac{y^3}{216}-\dfrac{11y^2}{216}+\dfrac{y}{6}-\dfrac{1}{6}=0;$$

and multiplying by 216, the equation will become

$$y^3-11y^2+36y-36=0.$$

But as it would be tedious
to make trial of all the divisors of the number 36, and
as the last term of the original equation is 1, it is better
to suppose, in this equation, $$x=\dfrac{1}{z}$$;
for we shall then have
$$\dfrac{6}{z^3}-\dfrac{11}{z^2}+\dfrac{6}{z}-1=0$$,
which, multiplied by $$z^2$$, gives $$6-11z+6z^2-z^3=0$$,
and transposing all the terms,

$$z^3-6z^2+11z-6=0;$$

where the roots are $$z=1$$, $$z=2$$, $$z=3$$;
whence it follows that in our equation
$$x=1$$, $$x=\frac{1}{2}$$, $$x=\frac{1}{3}$$.

**725.** It has been observed in the preceding articles, that
in order to have all the roots in positive numbers, the signs
plus and minus must succeed each other alternately; by
means of which the equation takes this form,
$$x^3-ax^2+bx-c=0$$,
the signs changing as many times
as there are positive roots. If all the three roots had been
negative, and we had multiplied together the three factors
$$x+p$$, $$x+q$$, $$x+r$$,
all the terms would have had the
sign plus, and the form of the equation would have been
$$x^3+ax^2+bx+c=0$$,
in which the same signs follow
each other three times; that is, the number of negative
roots.

We may conclude, therefore, that as often as the signs
change, the equation has positive roots; and that as often as
the same signs follow each other, the equation has negative
roots. This remark is very important, because it teaches us
whether the divisors of the last term are to be taken affirmatively
or negatively, when we wish to make the trial which
has been mentioned.

726. In order to illustrate what has been said by an example, let us consider the equation
$$x^3+x^2-34x+56=0$$,
in which the signs are changed twice, and in which the same
sign returns but once. Here we conclude that the equation
has two positive roots, and one negative root; and as these
roots must be divisors of the last terra 56, they must be included
in the numbers ±1, 2, 4, 7, 8, 14, 28, 56.

Let us, therefore, make $$x=2$$, and we shall have
$$8+4-68+56=0$$; whence we conclude that $$x=2$$
is a
positive root, and that therefore $$x-2$$
is a divisor of the
equation, by means of which we easily find the two other
roots; for, actually dividing by $$x-2$$, we have

<a href="https://artofproblemsolving.com/texer/geyfrhwy">
<img src="/assets/euler/geyfrhwy.png" alt="Polynomial long division" width="277" height="212" style="display:block;margin-left:auto;margin-right:auto;">
</a>

And making the quotient $$x^2-3x-28=0$$,
we find the two other roots; which will be

$$x=-\frac{3}{2} \pm \surd\left(\frac{9}{4}+24\right)=-\frac{3}{2} \pm \frac{11}{2};$$

that is, $$x=4$$; or $$x=-7$$;
and taking into account the root found before,
namely, $$x=2$$, we clearly perceive that the equation has
two positive, and one negative root. We shall give some
examples to render this still more evident.


**727.** *Question 1.* There are two numbers, whose difference is 12, and whose product multiplied by their sum
makes 14560. What are those numbers?

Let $$x$$ be the less of the two numbers, then the greater
will be $$x+12$$, and their product will be $$x^2+12x$$,
which multiplied by the sum $$2x+12$$, gives

$$2x^3+36x^2+144x=14560;$$

and dividing by 2, we have

$$x^3+18x^2+72x=7280.$$

Now, the last term 7280 is too great for us to make trial
of all its divisors; but as it is divisible by 8, we shall make
$$x=2y$$, because the new equation,
$$8y^3+72y^2+144y=7280$$, 
after the substitution, being divided by 8, will become
$$y^3+9y^2+18y=910$$; 

to solve which, we need only
try the divisors 1, 2, 5, 7, 10, 13, etc. of the number 910:
where it is evident, that the three first, 1, 2, 5, are too
small; beginning therefore with supposing $$y=7$$,
we immediately find that number to be one of the roots; for the
substitution gives
343+144+126=910.
It follows, therefore, that $$x=14$$;
and the two other roots will be
found by dividing
$$y^3+9y^2+18y-910$$ by $$y-7$$, thus:





















$$2x^3+36x^2+144x=14560;$$

$$x^3+18x^2+144x=7280.$$

$$8y^3+72y^2+144y=8270$$

$$y^3+9y^3+18y=910$$

$$y=7$$

$$x=14$$

$$y^3+9y^2+18y-910$$

$$y-7$$



<a href="https://artofproblemsolving.com/texer/ncijelkw">
<img src="/assets/euler/ncijelkw.png" alt="Polynomial long division" width="304" height="211" style="display:block;margin-left:auto;margin-right:auto;">
</a>

<a href="https://artofproblemsolving.com/texer/wlbnirku">
<img src="/assets/euler/wlbnirku.png" alt="Polynomial long division" width="309" height="212" style="display:block;margin-left:auto;margin-right:auto;">
</a>


#### References

1. Leonhard Euler, *Elements of Algebra*, Translated by Rev. John Hewlett. Longmans, Hurst, Rees, Orme, and Co., London, 1822.
    - [Section IV. Chapter 11. "Of the Resolution of Complete Equations of the Third Degree."](/assets/euler/en/IV-11.pdf)
    - [Archive.org](https://archive.org/details/elementsofalgebr00euleuoft/)
3. Leonhard Euler. *Vollständige Anleitung zur Algebra. Mit den Zusätzen von Joseph Louis Lagrange.* Herausgegeben von Heinrich Weber. B. G. Teubner. Leipzig and Berlin. 1911. Leonhardi Euleri Opera omnia. Series prima. Opera mathematica. Volumen primum.
    - [Zweyter Theil. Erster Abschnitt. Capitel 11. Von der Auflösung der vollständigen cubischen Gleichungen](/assets/euler/de/II-I-11.pdf)
    - [Springer](https://link.springer.com/book/9783764314002)
2. Leonhard Euler, *Vollständige Anleitung zur Algebra. Zweyter Theil. Von Auflösung algebraischer Gleichungen und der unbestimmten Analytic*, Kays. Acad. der Wissenschaften, St. Petersburg, 1770.
    - [Deutsches Textarchiv](https://www.deutschestextarchiv.de/euler_algebra02_1770)