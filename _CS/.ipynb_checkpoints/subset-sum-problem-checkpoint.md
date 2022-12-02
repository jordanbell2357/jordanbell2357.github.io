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

While $$t \neq k$$,

- $$t=s_i+s_j$$.
- 




# Tuple sum problem

Let $$X$$ and $$Y$$ be sets of integers and let $$k$$ be an integer.

Define the predicate $$R(X,Y,k)$$ to be true if there




