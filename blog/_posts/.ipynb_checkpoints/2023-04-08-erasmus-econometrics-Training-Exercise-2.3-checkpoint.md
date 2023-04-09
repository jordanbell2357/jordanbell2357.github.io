---
layout: post
title: Erasmus Econometrics Training Exercise 2.3
---

For real finite dimensional vector spaces $$V$$ and $$W$$, let $$\mathscr{L}(V,W)$$
be the set of linear transformations $$V \to W$$, which is itself a real finite dimensional vector space.

$$\dim \mathscr{L}(V,W) = \dim V \cdot \dim W.$$

In particular,

$$\dim \mathscr{L}(\mathbb{R}^k,\mathbb{R}^n) = \dim \mathbb{R}^k \cdot \dim \mathbb{R}^n = k\cdot n.$$

An $$n \times k$$ matrix is an element of $$\mathscr{L}(\mathbb{R}^k,\mathbb{R}^n)$$.

Let $$V^* = \mathscr{L}(V,\mathbb{R})$$, the dual space of $$V$$.

A column vector of length $$n$$ is an element of $$\mathbb{R}^n$$. A row vector of length $$k$$ is an
element of $$(\mathbb{R}^k)^*$$.

Observed data: $$y \in \mathbb{R}^n$$, $$X:\mathbb{R}^k \to \mathbb{R}^n$$

Unobserved data: $$\beta \in \mathbb{R}^k$$, $$\epsilon \in \mathbb{R}^n$$

Model: $$y = X\beta + \epsilon$$

Estimate $$\beta$$ by $$b$$ so that $$Xb$$ is close to $$y$$, i.e. $$y-Xb$$ is close to $$0 \in \mathbb{R}^n$$.

$$e=y-Xb$$

$$y \in \mathbb{R}^n$$, $$X:\mathbb{R}^k \to \mathbb{R}^n$$, $$b \in \mathbb{R}^k$$, $$e \in \mathbb{R}^n$$

Ordinary Least Squares (OLS): minimize $$S(b) = e^T e = \sum_{i=1}^n e_i^2$$.

$$
\begin{align*}
S(b)&=e^Te\\
&=(y-Xb)^T(y-Xb)\\
&=(y^T-(Xb)^T)(y-Xb)\\
&=(y^T-b^T X^T)(y-Xb)\\
&=y^Ty-y^TXb-b^T X^Ty+b^TX^TXb.
\end{align*}
$$

$$y^T X b \in \mathbb{R}$$, thus $$y^TXb = (y^TXb)^T = b^T X^T y$$. Then

$$
\begin{align*}
S(b)&=y^T y - y^T Xb - y^TXb + b^T X^T Xb\\
&=y^T y - 2y^TXb + b^TX^TXb
\end{align*}
$$

[Fréchet derivatives and Gâteaux derivatives](https://jordanbell.info/LaTeX/mathematics/frechetderivatives/)

[Gradients and Hessians in Hilbert spaces](https://jordanbell.info/LaTeX/mathematics/gradienthilbert/)

