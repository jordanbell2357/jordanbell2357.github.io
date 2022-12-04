---
layout: page
title: Subset sum problem
---

Let $$S$$ be a set of integers, with $$n \geq 1$$ elements, and let $$k$$ be an integer.

Define the predicate
$$P(S,k)$$: There is a subset $$T$$ of $$S$$ such that $$\sum_{t \in T} t = k$$.

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