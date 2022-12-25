---
layout: pag
title: Subset sum problem
---

Let $$S$$ be a set of integers, with $$n \geq 1$$ elements, and let $$k$$ be an integer.

Define the predicate
$$P(S,k)$$: There is a subset $$T$$ of $$S$$ such that $$\sum_{t \in T} t = k$$.

Let $$S=\{s_i : 1 \leq i \leq n\}$$, and for $$1 \leq m \leq n$$ define

$$S_m=\{s_i : 1 \leq i \leq m\}$$

according to which, $$S=S_n$$.

Let $$T_P(n)$$ worst case number of operations taken to compute $$P(S,k)$$.

If $$T$$ is a subset of $$S$$ such that
$$\sum_{t \in T} t = k$$,
either (i) $$s_n \in T$$ in which case 
$$\sum_{t \in T \setminus \{s_n\}} t = k - s_n$$, or
(ii) $$s_n \not \in T$$ in which case
$$T \subset S_{n-1}$$.
Thus

$$
\begin{align*}
P(S,k)&=P(S_n,k)\\
&=P(S_{n-1},k-s_n) \vee P(S_{n-1},k)
\end{align*}
$$

Then

$$
\begin{align*}
T_P(n) &= 2T_P(n-1)+d\\
&=2[2T_P(n-2)+d]+d\\
&=4T_P(n-2)+2d+d\\
&=4[2T_P(n-3)+d]+2d+d\\
&=8T_P(n-3)+4d+2d+d\\
&\vdots\\
&=2^{n-1} T_P(1) + \sum_{k=1}^{n-1} 2^k \cdot d\\
&=2^{n-1} T_P(1) + d \cdot \dfrac{2^n-1}{2-1}\\
&=2^{n-1} \cdot T_P(1) + (2^n-1) \cdot d\\
&=2^{n-1} (T_P(1) + d)
\end{align*}
$$