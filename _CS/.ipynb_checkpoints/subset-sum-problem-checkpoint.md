---
layout: page
title: Subset sum problems
---

# Subset sum problem

Let $$S$$ be a set of integers, with $$n \geq 1$$ elements, and let $$k$$ be an integer.

Define the predicate
$$P(S,k)$$ to be true if there is a subset $$T$$ of $$S$$ such that
$$\sum_{t \in T} = k$$ (i.e., if $$T=\{t_1,\ldots,t_n\}$$, then
$$t_1+\cdots+t_n = k$$), and false otherwise.

Let $$S=\{s_1,\ldots,s_n\}$$, and for $$1 \leq m \leq n$$ define

$$S_m=\{s_1,\ldots,s_m\}$$

Let $$T_P(n)$$ be the worst case runtime to compute $$P(S,k)$$.

$$
\begin{align*}
P(S,k)&=P(S_n,k)\\
&=P(S_{n-1},k-s_n) \vee P(S_{n-1},k)
\end{align*}
$$

Thus

$$
\begin{align*}
T_P(n) &= 2T_P(n-1)+d\\
&=2[2T_P(n-2)+d]+d\\
&=4T_P(n-2)+2d+d\\
&=4[2T_P(n-3)+d]+2d+d\\
&=8T_P(n-3)+4d+2d+d\\
&\vdots\\
&=\Theta(2^n)
\end{align*}
$$


# Pair sum problem

Let $$S$$ be a set of integers, with $$n \geq 1$$ elements, and let $$k$$ be an integer.

Define the predicate $$Q(S,k)$$ to be true if there are $$x,y \in S$$, $$x \neq y$$, such that $$x+y=k$$, and false
otherwise.

We loop $$x$$ over $$S$$, and for each of these $$x$$ loops, we loop $$y$$ over $$S \setminus \{x\}$$.
The worst case time complexity is $$\Theta(n^2)$$.

# Worst case analysis of solution of pair sum problem

Sort $$S$$ in ascending order, as $$S=[s_1,\ldots,s_n]$$, where 

$$s_1<\cdots<s_n$$

For $$0 \leq i,j < n$$, define

$$
S_{i,j} = [s_i,\ldots,s_j]
$$

So, $$S_{1,n} = S$$. And if $$j>i$$ then $$S_{i,j}=\emptyset$$.

Entering the loop, $$i=1$$ and $$j=n$$.

$$t=s_i+s_j$$

While $$t \neq k$$ and $$i < j$$, for $$i_0,j_0,t_0$$ at the start of a loop execution:

- If $$t_0>k$$, then $$i_1=i_0$$ and $$j_1 = j_0 - 1$$.
- If $$t_0<k$$, then $$i_1 = i_0 + 1$$ and $$j_1=j_0$$.
- $$t_1 = s_{i_1} + s_{j_1}$$.

This loop executes at most $$n$$ times. Each execution of the loop has worst case time complexity $$d$$, so

$$T(n)=\Theta(n \log n) + dn + c$$

Therefore $$T(n)=\Theta(n\log n)$$, that is, the sorting of the list dominates the time taken by all the other steps.

# Tuple sum problem

Let $$X$$ and $$Y$$ be sets of integers and let $$k$$ be an integer.

Define the predicate $$R(X,Y,k)$$ to be true if there is some $$x \in X$$, $$y \in Y$$ such that
$$x+y=k$$, and false otherwise.

Let $$n=\max\{|X|,|Y|\}$$; to be specific, say $$X$$ has $$n$$ elements and $$Y$$ has at most $$n$$ elements.
Then sorting $$X$$ takes $$\Theta(n)$$ operations, while sorting $$Y$$ can only be concluded to take
$$O(n)$$ operations, because we do not have a lower bound on its size. But
$$\Theta(n) + O(n) = \Theta(n)$$, so sorting both $$X$$ and $$Y$$ takes $$\Theta(n)$$ operations.

The argument then works in the same pattern as the previous part; I'll write out the details when I'm more awake.


# Divide-and-conquer solution of subset sum problem

...
