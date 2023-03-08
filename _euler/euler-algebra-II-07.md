---
layout: page
title: Chapter 7. "Of a particular Method, by which the Formula 𝑎𝑛𝑛+1 becomes a Square in Integers."
part: II
chapter: 7
---

### Part {{ page.part}}. {{ page.title }}

<span class="art">96</span> That which has been taught in the last chapter, cannot be completely performed, unless we are able to assign for
any number $$a$$, a number $$n$$, such that $$an^2+1$$ may become a square; or that we may have
$$m^2=an^2+1$$.

This equation would be easy to resolve, if we were satisfied with fractional numbers, since we should have only to
make $$m=1+\dfrac{np}{q}$$; for, by this supposition, we have

$$m^2=1+\dfrac{2np}{q}+\dfrac{n^2p^2}{q^2} = an^2+1;$$

in which equation, we
may expunge 1 from both sides, and divide the other terms
by $$n$$: then multiplying by $$q^2$$, we obtain $$2pq+np^2=anq^2$$;
and this equation, giving $$n=\dfrac{2pq}{aq^2-p^2}$$, would furnish an
infinite number of values for $$n$$: but as $$n$$ must be an integer
number, this method will be of no use, and therefore very
different means must be employed in order to accomplish
our object.

<span class="art">97</span> We must begin with observing, that if we wished
to have $$an^2+1$$ a square, in integer numbers, (whatever be
the value of $$a$$), the thing required would not be possible.

For, in the first place, it is necessary to exclude all the
cases, in which a would be negative; next, we must exclude
those also, in which $$a$$ would be itself a square; because
then $$an^2$$ would be a square, and no square can become a
square, in integer numbers, by being increased by unity. We
are obliged, therefore, to restrict our formula to the condition,
that $$a$$ be neither negative, nor a square;
but whenever $$a$$ is a positive number, without being a square, it is
possible to assign such an integer value of $$n$$, that $$an^2 + 1$$
may become a square: and when one such value has been
found, it will be easy to deduce from it an infinite number
of others, as was taught in the last chapter: but for our
purpose it is sufficient to know a single one, even the least;
and this, Pell, an English writer, has tauglit us to find bv
an ingenious method, which we shall here explain.

<span class="art">98</span> This method is not such as may be employed generally, for any number $$a$$ whatever; it is apphcable only to
each particular case.

We shall therefore begin with the easiest cases, and shall
first seek such a value of $$n$$, that $$2n^2+1$$ may be a square,
or that $$\surd(2n^2+1)$$ may become rational.

We immediately see that this square root becomes greater
than $$n$$, and less than $$2n$$. If, therefore, we express this root
by $$n+p$$, it is obvious that $$p$$ must be less than $$n$$; and we
shall have $$\surd(2n^2+1)=n+p$$; then, by squaring,
$$2n^2+1=n^2+2np+p^2$$; therefore

$$n^2=2np+p^2-1,\quad \textrm{and} \quad n=p+\surd(2p^2-1).$$

The whole is reduced, therefore, to the condition of $$2p^2-1$$
being a square; now, this is the case if $$p=1$$, which gives
$$n=2$$, and $$\surd(2n+1)=3$$.

If this case had not been immediately obvious, we should
have gone farther; and since $$\surd(2p^2-1)>p$$, and consequently,
$$n>2p$$, we should have made $$n=2p+q$$; and should thus have had

$$2p+q=p+\surd(2p^2-1),\quad \textrm{or} \quad p+q=\surd(2p^2-1),$$

and, squaring, $$p^2+2pq+q^2=2p^2-1$$, whence

$$p^2=2pq+q^2+1,$$

which would have given $$p=q+\surd(2q^2+1)$$; so that it
would have been necessary to have $$2q^2+1$$ a square;
and as this is the case, if we make $$q = 0$$, we shall have $$p = 1$$,
and $$n = 2$$, as before. This example is sufficient to give an
idea of the method; but it will be rendered more clear and
distinct from what follows.

<span class="art">99</span> Let $$a = 3$$, that is to say, let it be required to transform the formula
$$3n^2+1$$ into a square. Here we shall make $$\surd(3n^2+1)=n+p$$, which gives

$$3n^2+1=n^2+2np+p^2,\quad 2n^2=2np+p^2-1;$$

whence we obtain $$n=\dfrac{p+\surd(3p^2-2)}{2}$$. Now, since
$$\surd(3p^2-2)$$ exceeds $$p$$, and, consequently, $$n$$ is greater
than $$\dfrac{2p}{2}$$, or than $$p$$, let us suppose $$n=p+q$$, and we shall have

$$
\begin{align}
2p+2q&=p+\surd(3p^2-2), \; \textrm{or}\\
p+2q&=\surd(3p^2-2);
\end{align}
$$

then, by squaring, $$p^2+4pq+4q^2=3p^2-2$$; so that

$$2p^2=4pq+4q^2+2,\quad \textrm{or} \quad p^2=2pq+2q^2+1,$$

and

$$p=q+\surd(3q^2+1).$$

Now, this formula being similar to the one proposed, we may make
$$q=0$$, and shall thus obtain $$p=1$$, and $$n=1$$; whence
$$\surd(3n^2+1)=2$$.

<span class="art">100</span> Let $$a = 5$$, that we may have to make a square of
the formula $$5n^2+1$$, the root of which is greater than $$2n$$.
We shall therefore suppose

$$\surd(5n^2+1)=2n+p,\quad \textrm{or} \quad 5n^2+1=4n^2+4np+p^2;$$

whence we obtain

$$n^2=4np+p^2-1,\quad \textrm{and} \quad n=2p+\surd(5p^2-1).$$

Now, $$\surd(5p^2-1)>2p$$; whence it follows that $$n>4p$$; for which reason,
we shall make $$n=4p+q$$, which gives
$$2p+q=\surd(5p^2-1)$$, or $$4p^2+4pq+q^2=5p^2-1$$, and
$$p^2=4pq+q^2+1$$; so that $$p=2q+\surd(5q^2+1)$$; and as
$$q=0$$ satisfies the terms of this equation, we shall have
$$p=1$$, and $$n=4$$; therefore $$\surd(5n^2+1)=9$$.

<span class="art">101</span> Let us now suppose $$a = 6$$, that we may have to
consider the formula $$6n^2+1$$, whose root is likewise
contained between $$2n$$ and $$3n$$. We shall, therefore, make
$$\surd(6n^2+1)=2n+p$$, and shall have

$$6n^2+1 = 4n^2 + 4np + p^2, \quad \textrm{or} \quad 2n^2=4np+p^2-1;$$

and, thence,

$$n=p+\dfrac{\surd(6p^2-2)}{2},\quad \textrm{or} \quad n=\dfrac{2p+\surd(6p^2-2)}{2};$$

so that $$n>2p$$.

If, therefore, we make $$n=2p+q$$, we shall have

$$
\begin{align}
4p+2q&=2p+\surd(6p^2-2),\; \textrm{or}\\
2p+2q&=\surd(6p^2-2);
\end{align}
$$

the squares of which are $$4p^2+8pq+4q^2=6p^2-2$$; so that
$$2p^2=8pq+4q^2+2$$, and $$p^2=4pq+2q^2+1$$. Lastly,
$$p=2q+\surd(6q^2+1)$$. Now, this formula resembling the
first, we have $$q=0$$; wherefore $$p=1$$, $$n=2$$, and
$$\surd(6n^2+1)=5$$.

<span class="art">102</span> Let us proceed farther, and take $$a = 7$$, and
$$7n^2+1=m^2$$; here we see that $$m>2n$$; let us therefore make 
$$m=2n+p$$, and we shall have

$$7n^2+1=4n^2+4np+p^2,\quad \textrm{or} \quad 3n^2 = 4np+p^2-1;$$

which gives $$n=\dfrac{2p+\surd(7p^2-3)}{3}$$. At present, since $$n>\frac{4}{3}p$$,
and, consequently, greater than $$p$$, let us make $$n=p+q$$,
and we shall have $$p+3q=\surd(7p^2-3)$$; then, squaring
both sides, $$p^2+6pq+9q^2=7p^2-3$$, so that

$$6p^2=6pq+9q^2+3,\quad \textrm{or} \quad 2p^2 = 2pq+3q^2+1;$$

whence we get $$p=\dfrac{q+\surd(7q^2+2)}{2}$$. Now, we have here $$p>\dfrac{3q}{2}$$;
and, consequently, $$p>q$$; so that making $$p=q+r$$, we shall have $$q+2r=\surd(7q^2+2)$$;
the squares of which are $$q^2+4qr+4r^2=7q^2+2$$; then
$$6q^2=4qr+4r^2-2$$, or $$3q^2=2qr+2r^2-1$$; and, lastly,
$$q=\dfrac{r+\surd(7r^2-3)}{3}$$.
Since now $$q>r$$, let us suppose $$q=r+s$$, and we shall have

$$
\begin{align}
2r+3s&=\surd(7r^2-3); \; \textrm{then}\\
4r^2+12rs+9s^2&=7r^2-3, \; \textrm{or}\\
3r^2&=12rs+9s^2+3, \; \textrm{or}\\
r^2&=4rs+3s^2+1, \; \textrm{and}\\
r&=2s+\surd(7s^2+1).
\end{align}
$$

Now, this formula is like the first; so that making $$s = 0$$,
we shall obtain $$r = 1$$, $$g = 1$$, $$p = 2$$, and $$n = 3$$, or
$$m = 8$$.

But this calculation may be considerably abridged in
the following manner, which may be adopted also in other
cases.

Since $$7n^2+1=m^2$$, it follows that $$m<3n$$.

If, therefore, we suppose $$m=3n-p$$, we shall have

$$7n^2+1=9n^2-6np+p^2,\quad \textrm{or} \quad 2n^2 = 6np-p^2+1;$$

whence we obtain $$n=\dfrac{3p+\surd(7p^2+2)}{2}$$; so that $$n<3p$$;
for this reason we shall write $$n=3p-2q$$; and, squaring, we shall have
$$9p^2-12pq+4q^2=7p^2+2$$; or

$$2p^2=12pq-4q^2+2,\quad \textrm{and} \quad p^2=6pq-2q^2+1,$$

whence results $$p=3q+\surd(7q^2+1)$$. Here, we can at once make
$$q=0$$, which gives $$p=1$$, $$n=3$$, and $$m=8$$, as before.

<span class="art">103</span> Let $$a=8$$, so that $$8n^2+1=m^2$$, and $$m<3n$$.
Here, we must make $$m = 3n - p$$, and shall have

$$8n^2+1=9n^2-6np+p^2,\quad \textrm{or} \quad n^2=6np-p^2+1;$$

whence $$n=3p+\surd(8p^2+1)$$, and this formula being already
similar to the one proposed, we may make $$p = 0$$,
which gives $$n = 1$$, and $$m = 3$$.

<span class="art">104</span> We may proceed, in the same manner, for every
otlier number, $$a$$, provided it be positive and not a square,
and we shall always be led, at last, to a radical quantity,
such as $$\surd(at^2+1)$$; similar to the first, or given formula,
and then we have only to suppose $$t = 0$$; for the irrationality will disappear,
and by tracing back the steps, we
shall necessarily find such a value of $$n$$, as will make $$an^2+1$$
a square.

Sometimes we quickly obtain our end; but, frequently
also, we are obliged to go through a great number of
operations. This depends on the nature of the number
$$a$$; but we have no principles, by which we can foresee
the number of operations that it will be necessary to perform.
The process is not very long for numbers below 13,
but when $$a = 13$$, the calculation becomes much more
prolix; and, for this reason, it will be proper here to resolve
that case.

<span class="art">105</span> Let therefore $$a = 13$$, and let it be required to
find $$13n^2+1=m^2$$. Here, as $$m^2>9n^2$$, and, consequently,
$$m>3n$$, let us suppose $$m=3n+p$$; we shall then have

$$13n^2+1=9n^2+6np+p^2,\quad \textrm{or} \quad 4n^2=6np+p^2-1,$$

and $$n=\dfrac{3p+\surd(13p^2-4)}{4}$$, which shows that $$n>\frac{6}{4}p$$,
and therefore much greater than $$p$$. If, therefore, we make $$n=p+q$$, we shall
have $$p+4q=\surd(13p^2-4)$$; and, taking the squares,

$$13p^2-4=p^2+8pq+16q^2;$$

so that

$$12p^2=8pq+16q^2+4,\quad \textrm{or} \quad 3p^2=2pq+4q^2+1,$$

and $$p=\dfrac{q+\surd(13q^2+3)}{3}$$. Here, $$p>\dfrac{q+3p}{3}$$, or $$p>q$$;
we shall proceed, therefore, by making $$p=q+r$$, and shall thus obtain
$$2q+3r=\surd(13q^2+3)$$; then

$$
\begin{align}
13q^2+3&=4q^2+12qr+9r^2, \; \textrm{or}\\
9q^2&=12qr+9r^2-3, \; \textrm{or}\\
3q^2&=4qr+3r^2-1;
\end{align}
$$

which gives $$p=\dfrac{2r+\surd(13r^2-3)}{3}$$.

Again, since $$q>\dfrac{2r+3r}{3}$$, and thus $$q>r$$, we shall make
$$q=r+s$$, and we shall thus have $$r+3s=\surd(13r^2-3)$$;
or $$13r^2-3=r^2+6rs+9s^2$$, or $$12r^2=6rs+9s^2+s$$, or
$$4r^2=2rs+3s^2+1$$; whence we obtain $$r=\dfrac{s+\surd(13s^2+4)}{4}$$. But here
$$r>\dfrac{3+3s}{4}$$, or $$r>s$$; wherefore let $$r=s+t$$, and we shall have
$$3s+4t=\surd(13s^2+4)$$, and 

$$13s^2+4=9s^2+24st+16t^2;$$

so that $$4s^2=24st+16t^2-4$$, and $$s^2=6ts+4t^2-1$$;
therefore $$s=3t+\surd(13t^2-1)$$. Here we have

$$s>3t+3t,\quad \textrm{or} \quad s>6t;$$

we must therefore make $$s=6t+u$$; whence

$$3t+u=\surd(13t^2-1),\quad \textrm{and} \quad 13t^2-1=9t^2+6tu+u^2;$$

then $$4t^2=6tu+u^2+1$$; and, lastly,

$$t=\dfrac{3u+\surd(13u^2+4)}{4},\quad \textrm{or} \quad t>\dfrac{6u}{4}>u.$$

If, therefore, we make $$t = u + v$$, we shall have

$$u+4v=\surd(13u^2+4),\quad \textrm{and} \quad 13u^2+4=u^2+8uv+16v^2;$$

therefore

$$12u^2=8uv+16v^2-4,\quad \textrm{or} \quad 3u^2=2uv+4v^2-1;$$

lastly, $$u=\dfrac{v+\surd(13v^2-3)}{3}$$, thus $$u>\dfrac{4v}{3}$$, and thus $$u>v$$.

Let us, therefore, make $$u=v+x$$, and we shall have $$2v+3x=\surd(13v^2-3)$$, and $$13v^2-3=4v^2+12vx+9x^2$$; or

$$9v^2=12vx+9x^2+3,\quad \textrm{or} \quad 3v^2 = 4vx+3x^2+1,$$

and $$v=\dfrac{2x+\surd(13x^2+3)}{3}$$; so that $$v>\frac{5}{3}x$$, and thus $$>x$$.

Let us now suppose $$v=x+y$$, and we shall have

$$
\begin{align}
x+3y&=\surd(13x^2+3),\; \textrm{and}\\
13x^2+3&=x^2+6xy+9y^2,\; \textrm{or}\\
12x^2&=6xy+9y^2-3,\; \textrm{and}\\
4x^2&=2xy+3y^2-1; \; \textrm{whence}\\
x&=\dfrac{y+\surd(13y^2-4)}{4},
\end{align}
$$

and, consequently, $$x>y$$. We shall, therefore, make $$x=y+z$$, which gives

$$
\begin{align}
3y+4z&=\surd(13y^2-4),\; \textrm{and}\\
13y^2-4&=9y^2+24zy+16z^2, \; \textrm{or}\\
4y^2&=24zy+16z^2+4; \; \textrm{therefore}\\
y^2&=6yz+4z^2+1, \; \textrm{and}\\
y&=3z+\surd(13z^2+1).
\end{align}
$$

This formula being at length similar to the first, we may
take $$z=0$$, and go back as follows:

$$
\begin{array}{l|l|l}
z=0,&u=v+x=3,&q=r+s=71,\\
y=1,&t=u+v=5,&p=q+r=109,\\
x=y+z=1,&s=6t+u=33,&n=p+q=180,\\
v=x+y=2,&r=s+t=38,&m=3n+p=649.
\end{array}
$$

So that 180 is the least number, after 0, which we can
substitute for $$n$$, in order that $$13n^2+1$$ may become a square.

<span class="art">106</span> This example sufficiently shews how prolix these
calculations may be in particular cases;
and when the numbers in question are greater, we are often obliged to go
through ten times as many operations as we had to perform
for the number 13.

As we cannot foresee the numbers that will require such
tedious calculations, we may with propriety avail ourselves
of the trouble which others have taken; and, for this purpose, a Table is subjoined to the present chapter, in which
the values of $$m$$ and $$n$$ are calculated for all numbers, $$a$$, between 2 and 100;
so that in the cases which present themselves, we may take from it the values of $$m$$ and $$n$$, which
answer to the given number $$a$$.

<span class="art">107</span> It is proper, however, to remark, that, for certain
numbers, the letters $$m$$ and $$n$$ may be determined generally;
this is the case when $$a$$ is greater, or less than a square, by
1 or 2; it will be proper, therefore, to enter into a particular
analysis of these cases.

<span class="art">108</span> In order to this, let $$a=e^2-2$$;
and since we must have $$(e^2-2)n^2+1=m^2$$,
it is clear that $$m<en$$;
therefore we shall make $$m = en - p$$, from which we have

$$(e^2-2)n^2+1=e^2n^2-2enp+p^2,$$

or $$2n^2=2enp-p^2+1$$; therefore $$n=\dfrac{ep+\surd(e^2p^2-2p^2+2)}{2}$$;
and it is evident that if we make $$p=1$$, this quantity becomes rational, and
we have $$n=e$$, and $$m=e^2-1$$.

For example, let $$a=23$$, so that $$e=5$$; we shall then have
$$23n^2+1=m^2$$, if $$n=5$$, and $$m=24$$. The reason of which
is evident from another consideration; for if, in
the case of $$a=e^2-2$$, we make $$n=e$$, we shall have
$$an^2+1=e^4-2e^2+1$$; which is the square of $$e^2-1$$.

<span class="art">109</span> Let $$a=e^2-1$$, or less than a square by unity.
First, we must have $$(e^2-1)n^2+1=m^2$$; then, because,
as before, $$m<en$$, we shall make $$m=en-p$$; and this
being done, we have

$$(e^2-1)n^2+1=e^2n^2-2enp+p^2,\quad \textrm{or} \quad n^2=2enp-p^2+1;$$

wherefore $$n=ep+\surd(e^2p^2-p^2+1)$$. Now, the irrationality
disappeared by supposing $$p=1$$; so that $$n=2e$$, and
$$m=2e^2-1$$. This also is evident; for, since $$a=e^2-1$$,
and $$n=2e$$, we find

$an^2+1=4e^4-4e^2+1,$$

or equal to the square of $$2e^2-1$$. For example, let $$a=24$$,
or $$e=5$$, we shall have $$n=10$$, and

$$24n^2+1=2401=49^2.$$

<span class="art">110</span> Let us now suppose $$a=e^2+1$$,
or $$a$$ greater than
a square by unity. Here we must have

$$(e^2+1)n^2+1=m^2,$$

and $$m$$ will evidently be greater than $$en$$. Let us, therefore,
write $$m = en + p$$, and we shall have

$$(e^2+1)n^2+1=e^2n^2+2enp+p^2,\quad \textrm{or} \quad n^2=2enp+p^2-1;$$

whence $$n=ep+\surd(e^2p^2+p^2-1)$$. Now, we may make $$p=1$$, and shall then have
$$n=2e$$; therefore, $$m^2=2e^2+1$$;
which is what ought to be the result from the consideration,
that $$a=e^2+1$$, and $$n=2e$$, which gives
$$an^2+1=4e^4+4e^2+1$$, the square of $$2e^2+1$$. For example,
let $$a=17$$, so that $$e=4$$, and we shall have
$$17n^2+1=m^2$$; by making $$n=8$$, and $$m=33$$.

<span class="art">111</span> Lastly, let $$a=e^2+2$$, or greater than a square by 2.
Here, we have $$(e^2+2)n^2+1=m^2$$, and, as before,
$$m>en$$; therefore we shall suppose $$m=en+p$$, and shall
thus have

$$
\begin{align}
c^2n^2+2n^2+1&=e^2n^2+2enp+p^2, \; \textrm{or}\\
2n^2&=2epn+p^2-1, \; \textrm{which gives}\\
n&=\dfrac{ep+\surd(e^2p^2+2p^2-2)}{2}.
\end{align}
$$

Let $$p=1$$, we shall find $$n=e$$, and $$m=e^2+1$$; and, in
fact, since $$a=e^2+2$$, and $$n=e$$, we have $$an^2+1=e^4+2e^2+1$$,
which is the square of $$e^2+1$$.

For example, let $$a=11$$, so that $$e=3$$; we shall find
$$11n^2+1=m^2$$, by making $$n=3$$, and $$m=10$$. If we
supposed $$a=83$$, we should have $$e=9$$, and
$$83n^2+1=m^2$$, where $$n=9$$, and $$m=82$$.

<table>
<tr>
<th>𝑎</th>
<th>𝑛</th>
<th>𝑚</th>
</tr>
<tr>
<td>2</td>
<td>2</td>
<td>3</td>
</tr>
<tr>
<td>3</td>
<td>1</td>
<td>2</td>
</tr>
<tr>
<td>5</td>
<td>4</td>
<td>9</td>
</tr>
<tr>
<td>6</td>
<td>2</td>
<td>5</td>
</tr>
<tr>
<td>7</td>
<td>3</td>
<td>8</td>
</tr>
<tr>
<td>8</td>
<td>1</td>
<td>3</td>
</tr>
<tr>
<td>10</td>
<td>6</td>
<td>19</td>
</tr>
<tr>
<td>11</td>
<td>3</td>
<td>10</td>
</tr>
<tr>
<td>12</td>
<td>2</td>
<td>7</td>
</tr>
<tr>
<td>13</td>
<td>180</td>
<td>649</td>
</tr>
<tr>
<td>14</td>
<td>4</td>
<td>15</td>
</tr>
<tr>
<td>15</td>
<td>1</td>
<td>4</td>
</tr>
<tr>
<td>17</td>
<td>8</td>
<td>33</td>
</tr>
<tr>
<td>18</td>
<td>4</td>
<td>17</td>
</tr>
<tr>
<td>19</td>
<td>39</td>
<td>170</td>
</tr>
<tr>
<td>20</td>
<td>2</td>
<td>9</td>
</tr>
<tr>
<td>21</td>
<td>12</td>
<td>55</td>
</tr>
<tr>
<td>22</td>
<td>42</td>
<td>197</td>
</tr>
<tr>
<td>23</td>
<td>5</td>
<td>24</td>
</tr>
<tr>
<td>24</td>
<td>1</td>
<td>5</td>
</tr>
<tr>
<td>26</td>
<td>10</td>
<td>51</td>
</tr>
<tr>
<td>27</td>
<td>5</td>
<td>26</td>
</tr>
<tr>
<td>28</td>
<td>24</td>
<td>127</td>
</tr>
<tr>
<td>29</td>
<td>1820</td>
<td>9801</td>
</tr>
<tr>
<td>30</td>
<td>2</td>
<td>11</td>
</tr>
<tr>
<td>31</td>
<td>273</td>
<td>1520</td>
</tr>
<tr>
<td>32</td>
<td>3</td>
<td>17</td>
</tr>
<tr>
<td>33</td>
<td>4</td>
<td>23</td>
</tr>
<tr>
<td>34</td>
<td>6</td>
<td>35</td>
</tr>
<tr>
<td>35</td>
<td>1</td>
<td>6</td>
</tr>
<tr>
<td>37</td>
<td>12</td>
<td>73</td>
</tr>
<tr>
<td>38</td>
<td>6</td>
<td>37</td>
</tr>
<tr>
<td>39</td>
<td>4</td>
<td>25</td>
</tr>
<tr>
<td>40</td>
<td>3</td>
<td>19</td>
</tr>
<tr>
<td>41</td>
<td>320</td>
<td>2049</td>
</tr>
<tr>
<td>42</td>
<td>2</td>
<td>13</td>
</tr>
<tr>
<td>43</td>
<td>531</td>
<td>3482</td>
</tr>
<tr>
<td>44</td>
<td>30</td>
<td>199</td>
</tr>
<tr>
<td>45</td>
<td>24</td>
<td>161</td>
</tr>
<tr>
<td>46</td>
<td>3588</td>
<td>24335</td>
</tr>
<tr>
<td>47</td>
<td>7</td>
<td>48</td>
</tr>
<tr>
<td>48</td>
<td>1</td>
<td>7</td>
</tr>
<tr>
<td>50</td>
<td>14</td>
<td>99</td>
</tr>
<tr>
<td>51</td>
<td>7</td>
<td>50</td>
</tr>
<tr>
<td>52</td>
<td>90</td>
<td>649</td>
</tr>
<tr>
<td>53</td>
<td>9100</td>
<td>66249</td>
</tr>
<tr>
<td>54</td>
<td>66</td>
<td>485</td>
</tr>
<tr>
<td>55</td>
<td>12</td>
<td>89</td>
</tr>
<tr>
<td>56</td>
<td>2</td>
<td>15</td>
</tr>
<tr>
<td>57</td>
<td>20</td>
<td>151</td>
</tr>
<tr>
<td>58</td>
<td>2574</td>
<td>19603</td>
</tr>
<tr>
<td>59</td>
<td>69</td>
<td>530</td>
</tr>
<tr>
<td>60</td>
<td>4</td>
<td>31</td>
</tr>
<tr>
<td>61</td>
<td>226153980</td>
<td>1766319049</td>
</tr>
<tr>
<td>62</td>
<td>8</td>
<td>63</td>
</tr>
<tr>
<td>63</td>
<td>1</td>
<td>8</td>
</tr>
<tr>
<td>65</td>
<td>16</td>
<td>129</td>
</tr>
<tr>
<td>66</td>
<td>8</td>
<td>65</td>
</tr>
<tr>
<td>67</td>
<td>5967</td>
<td>48842</td>
</tr>
<tr>
<td>68</td>
<td>4</td>
<td>33</td>
</tr>
<tr>
<td>69</td>
<td>936</td>
<td>7775</td>
</tr>
<tr>
<td>70</td>
<td>30</td>
<td>251</td>
</tr>
<tr>
<td>71</td>
<td>413</td>
<td>3480</td>
</tr>
<tr>
<td>72</td>
<td>2</td>
<td>17</td>
</tr>
<tr>
<td>73</td>
<td>267000</td>
<td>2281249</td>
</tr>
<tr>
<td>74</td>
<td>430</td>
<td>3699</td>
</tr>
<tr>
<td>75</td>
<td>3</td>
<td>26</td>
</tr>
<tr>
<td>76</td>
<td>6630</td>
<td>57799</td>
</tr>
<tr>
<td>77</td>
<td>40</td>
<td>351</td>
</tr>
<tr>
<td>78</td>
<td>6</td>
<td>53</td>
</tr>
<tr>
<td>79</td>
<td>9</td>
<td>80</td>
</tr>
<tr>
<td>80</td>
<td>1</td>
<td>9</td>
</tr>
<tr>
<td>82</td>
<td>18</td>
<td>163</td>
</tr>
<tr>
<td>83</td>
<td>9</td>
<td>82</td>
</tr>
<tr>
<td>84</td>
<td>6</td>
<td>55</td>
</tr>
<tr>
<td>85</td>
<td>30996</td>
<td>285769</td>
</tr>
<tr>
<td>86</td>
<td>1122</td>
<td>10405</td>
</tr>
<tr>
<td>87</td>
<td>3</td>
<td>28</td>
</tr>
<tr>
<td>88</td>
<td>21</td>
<td>197</td>
</tr>
<tr>
<td>89</td>
<td>53000</td>
<td>500001</td>
</tr>
<tr>
<td>90</td>
<td>2</td>
<td>19</td>
</tr>
<tr>
<td>91</td>
<td>165</td>
<td>1574</td>
</tr>
<tr>
<td>92</td>
<td>120</td>
<td>1151</td>
</tr>
<tr>
<td>93</td>
<td>1260</td>
<td>12151</td>
</tr>
<tr>
<td>94</td>
<td>221064</td>
<td>2143295</td>
</tr>
<tr>
<td>95</td>
<td>4</td>
<td>39</td>
</tr>
<tr>
<td>96</td>
<td>5</td>
<td>49</td>
</tr>
<tr>
<td>97</td>
<td>6377352</td>
<td>62809633</td>
</tr>
<tr>
<td>98</td>
<td>10</td>
<td>99</td>
</tr>
<tr>
<td>99</td>
<td>1</td>
<td>10</td>
</tr>
</table>


#### Editions

1. Leonhard Euler. *Elements of Algebra*. Translated by Rev. John Hewlett. Third Edition. Longmans, Hurst, Rees, Orme, and Co. London. 1822.
    - [Part {{ page.part}}. {{ page.title }}](/EulerAlgebra/en/pt-II-7.pdf)
2. Leonhard Euler. *Vollständige Anleitung zur Algebra. Mit den Zusätzen von Joseph Louis Lagrange.* Herausgegeben von Heinrich Weber. B. G. Teubner. Leipzig and Berlin. 1911. Leonhardi Euleri Opera omnia. Series prima. Opera mathematica. Volumen primum.
    - [Zweyter Theil. Zweyter Abschnitt. Capitel 7. Von einer besondern Methode die Formel $$ann+1$$ zu einem Quadrat in gantzen Zahlen zu machen](/EulerAlgebra/de/II-II-7.pdf)