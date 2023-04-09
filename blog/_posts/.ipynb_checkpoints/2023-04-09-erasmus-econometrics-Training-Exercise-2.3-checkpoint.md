---
layout: post
title: Erasmus Econometrics Training Exercise 2.3
---

# Linear algebra

For real finite dimensional vector spaces $$V$$ and $$W$$, let $$\mathscr{L}(V,W)$$
be the set of linear transformations $$V \to W$$, which is itself a real finite dimensional vector space.

$$\dim \mathscr{L}(V,W) = \dim V \cdot \dim W.$$

In particular,

$$\dim \mathscr{L}(\mathbb{R}^k,\mathbb{R}^n) = \dim \mathbb{R}^k \cdot \dim \mathbb{R}^n = k\cdot n.$$

An $$n \times k$$ matrix is an element of $$\mathscr{L}(\mathbb{R}^k,\mathbb{R}^n)$$.

Let $$V^* = \mathscr{L}(V,\mathbb{R})$$, the **dual space** of $$V$$.

A column vector of length $$n$$ is an element of $$\mathbb{R}^n$$. A row vector of length $$k$$ is an
element of $$(\mathbb{R}^k)^*$$.

For $$v \in \mathbb{R}^n$$, the transpose $$v^T$$ belongs to $$(\mathbb{R}^n)^*$$, and for
$$v^T \in (\mathbb{R}^n)^*$$, the transpose $$(v^T)^T = v$$ belongs to $$((\mathbb{R}^n)^*)^*=\mathbb{R}^n$$.

Let $$[\cdot,\cdot]:(\mathbb{R}^n)^* \times \mathbb{R}^n \to \mathbb{R}$$ be the **dual pairing**:

$$[v^T,w] = v^T w, \qquad v^T \in (\mathbb{R}^n)^*, w \in \mathbb{R}^n.$$

# Ordinary Least Squares (OLS)

Observed data: $$y \in \mathbb{R}^n$$, $$X:\mathbb{R}^k \to \mathbb{R}^n$$

Unobserved data: $$\beta \in \mathbb{R}^k$$, $$\epsilon \in \mathbb{R}^n$$

Model: $$y = X\beta + \epsilon$$

Estimate $$\beta$$ by $$b$$ so that $$Xb$$ is close to $$y$$, i.e. $$y-Xb$$ is close to $$0 \in \mathbb{R}^n$$.

$$e=y-Xb$$

$$y \in \mathbb{R}^n$$, $$X:\mathbb{R}^k \to \mathbb{R}^n$$, $$b \in \mathbb{R}^k$$, $$e \in \mathbb{R}^n$$

Ordinary Least Squares (OLS): minimize $$S(b) = e^T e = \sum_{i=1}^n e_i^2$$.

$$
\begin{align*}
S(b)&=[e^T,e]\\
&=[(y-Xb)^T,y-Xb]\\
&=[y^T - (Xb)^T, y- Xb]\\
&=[y^T,y-Xb] - [(Xb)^T,y-Xb]\\
&=[y^T,y]-[y^T,Xb] - [(Xb)^T,y] + [(Xb)^T,Xb].
\end{align*}
$$

Because $$[v^T,w] = [v,w^T]$$,

$$
S(b)=[y^T,y] - 2[y^T,Xb]+ [(Xb)^T,Xb]
$$

[Fréchet derivatives and Gâteaux derivatives](https://jordanbell.info/LaTeX/mathematics/frechetderivatives/) [^1]

[^1]: cf. [Gradients and Hessians in Hilbert spaces](https://jordanbell.info/LaTeX/mathematics/gradienthilbert/)

For $$b_0 \in \mathbb{R}^k$$ and $$b \in \mathbb{R}^k$$,

$$
\begin{align*}
S(b)-S(b_0)&=[y^T,y] - 2[y^T,Xb]+ [(Xb)^T,Xb]-([y^T,y] - 2[y^T,Xb_0]+ [(Xb_0)^T,Xb_0])\\
&=- 2[y^T,Xb]+ [(Xb)^T,Xb]+2[y^T,Xb_0]-[(Xb_0)^T,Xb_0]\\
&=
\end{align*}
$$