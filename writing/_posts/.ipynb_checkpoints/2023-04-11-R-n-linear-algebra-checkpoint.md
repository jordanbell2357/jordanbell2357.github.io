---
layout: post
title: ℝⁿ
---

# $$\mathbb{R}^n$$

Let $$\mathbb{N}$$ be the nonnegative integers and let $$n$$ be a positive integer.

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
