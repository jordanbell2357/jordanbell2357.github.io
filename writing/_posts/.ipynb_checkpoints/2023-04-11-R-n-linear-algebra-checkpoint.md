---
layout: post
title: \(\mathbb{R}^n\)
---

# Linear algebra

For real finite dimensional vector spaces $$V$$ and $$W$$, let $$\mathscr{L}(V,W)$$
be the set of linear transformations $$V \to W$$, which is itself a real finite dimensional vector space.

$$\dim \mathscr{L}(V,W) = \dim V \cdot \dim W.$$

In particular,

$$\dim \mathscr{L}(\mathbb{R}^k,\mathbb{R}^n) = \dim \mathbb{R}^k \cdot \dim \mathbb{R}^n = k\cdot n.$$

An $$n \times k$$ matrix is an element of $$\mathscr{L}(\mathbb{R}^k,\mathbb{R}^n)$$.

Let $$V^* = \mathscr{L}(V,\mathbb{R})$$, the **dual space** of $$V$$.

Define $$[\cdot,\cdot]:V \times V^* \to \mathbb{R}$$ by

$$[v,\phi] = \phi(v), \qquad v \in V, \phi \in V^*.$$

# $$\mathbb{R}^d$$

Let $$\mathbb{N}$$ be the nonnegative integers and let $$d$$ be a positive integer.

Define $$[d]=\{i \in \mathbb{N}: 1 \leq i \leq d\}$$.

Let $$\mathbb{R}^d$$ be the set of functions $$[d] \to \mathbb{R}$$. This is a real vector space.

Define $$e_i \in \mathbb{R}^d$$ by $$e_i(j) = \delta_{i,j}$$. $$\{e_i: 1 \leq i \leq d\}$$
is a basis for $$\mathbb{R}^d$$.

For $$v, w \in \mathbb{R}^d$$, define

$$\langle v,w \rangle = \sum_{i \in [d]\} v(i)w(i).$$

For $$v \in \mathbb{R}^d$$,

$$
v = \sum_{i \in [d]} \langle v,e_i \rangle e_i.
$$

For $$v \in \mathbb{R}^d$$, define $$v^T \in (\mathbb{R}^d)^*$$ by

$$v^T(w) = \langle v, w \rangle =\sum_{i \in [d]\} v(i)w(i), \qquad w \in \mathbb{R}^d.$$

In particular,

$$v^T(e_i) = \langle v, e_i \rangle.$$

The map $$v \mapsto v^T$$ is a linear isomorphism $$\mathbb{R}^d \to (\mathbb{R}^d)^*$$. (In particular, it is onto because $$\mathbb{R}^d$$ is finite dimensional.)

For $$w \in \mathbb{R}^d$$ and $$v^T \in (\mathbb{R}^d)^*$$,

$$[w,v^T] = v^T(w) = \langle v, w \rangle=\sum_{i \in [d]\} v(i)w(i).$$

# Ordinary Least Squares (OLS)

Observed data: $$y \in \mathbb{R}^n$$, $$X \in \mathscr{L}(\mathbb{R}^k,\mathbb{R}^n)$$

Unobserved data: $$\beta \in \mathbb{R}^k$$, $$\epsilon \in \mathbb{R}^n$$

Model: $$y = X\beta + \epsilon$$

Estimate $$\beta$$ by $$b$$ so that $$Xb$$ is close to $$y$$, i.e. $$y-Xb$$ is close to $$0 \in \mathbb{R}^n$$.

Define $$e=y-Xb$$

$$y \in \mathbb{R}^n$$, $$X \in \mathscr{L}(\mathbb{R}^k,\mathbb{R}^n)$$, $$b \in \mathbb{R}^k$$, $$e \in \mathbb{R}^n$$

Ordinary Least Squares (OLS): minimize $$S:\mathbb{R}^n \to \mathbb{R}$$ defined by

$$S(b) = [e, e^T] = \sum_{i=1}^n \langle e, e_i \rangle^2$$



[Fréchet derivatives and Gâteaux derivatives](https://jordanbell.info/LaTeX/mathematics/frechetderivatives/) [^1]

[^1]: cf. [Gradients and Hessians in Hilbert spaces](https://jordanbell.info/LaTeX/mathematics/gradienthilbert/)
