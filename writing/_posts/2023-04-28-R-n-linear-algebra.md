---
layout: post
title: ℝⁿ
---

# $$\mathbb{R}^n$$

Let $$\mathbb{N}$$ be the nonnegative integers and let $$n \in \mathbb{N}$$.

Define $$[n]=\{i \in \mathbb{N}: i < n\}$$.

Let $$\mathbb{R}^n=\mathbb{R}^{[n]}$$,
the set of functions $$[n] \to \mathbb{R}$$.

## $$n=0$$

$$[0]=\emptyset$$.

$$\mathbb{R}^0 = \mathbb{R}^\emptyset = \{\emptyset\}$$. [^1]

[^1]: [empty function in nLab](https://ncatlab.org/nlab/show/empty+function)

$$\mathbb{R}^0$$ is an $$\mathbb{R}$$-linear space, with one element.

## $$n \geq 1$$

Let $$n \in \mathbb{N}_{\geq 1}$$.
For $$x,y \in \mathbb{R}^n$$,
we define $$x+y \in \mathbb{R}^n$$ by
$$(x+y)(i)=x(i)+y(i)$$, $$i \in [n]$$.

For $$x \mathbb{R}^n$$ and $$c \in \mathbb{R}$$, we define
$$cx \in \mathbb{R}^n$$
by $$(cx)(i)=cx(i)$$, $$i \in [n]$$.
Then $$\mathbb{R}^n$$ is an $$\mathbb{R}$$-linear space.

For $$i,j \in \mathbb{N}$$, define

$$
\delta_{i,j} = \begin{cases}1&i = j\\
0&i \neq j
\end{cases}
$$

For $$k \in [n]$$ define $$e_k \in \mathbb{R}^n$$ by 

$$e_k(i) = \delta_{i,k}, \qquad i \in [n].$$

$$\{e_k: k \in [n]\}$$ is a basis for $$\mathbb{R}^n$$.

## Dual space $$(\mathbb{R}^n)^*$$

Let $$(\mathbb{R}^n)^*$$ be the set of linear maps $$\mathbb{R}^n \to \mathbb{R}$$, the **dual space**
of $$\mathbb{R}^n$$.

For $$x \in \mathbb{R}^n$$, define $$x^T \in (\mathbb{R}^n)^*$$ by

$$x^T y = \sum_{i \in [n]} x(i)y(i),\qquad y \in \mathbb{R}^n.$$

We call $$x^T$$ the **transpose** of $$x$$: $$x$$ is a vector/column vector and $$x^T$$ is a covector/row vector.

$$\{e_k^T: k \in [n]\}$$ is a basis for $$(\mathbb{R}^n)^*$$.

The map $$x \mapsto x^T$$ is a linear isomorphism $$\mathbb{R}^n \to (\mathbb{R}^n)^*$$.

## Basis expansion

For $$x \in \mathbb{R}^n$$ and for $$k \in [n]$$, we have

$$x^T e_k = \sum_{i \in [n]} x(i) e_k(i) =
\sum_{i \in [n]} x(i) \delta_{i,k} = x(k)$$

and

$$e_k^T x = \sum_{i \in [n]} e_k(i) x(i) =
\sum_{i \in [n]} \delta_{i,k} x(i)= x(k)$$.

Using this, one then works out that

$$
x = \sum_{k \in [n]} (e_k^T x)e_k.
$$

# Linear algebra

For real finite dimensional vector spaces $$V$$ and $$W$$, let $$\mathscr{L}(V,W)$$
be the set of linear transformations $$V \to W$$, which is itself a real finite dimensional vector space.

$$(\mathbb{R}^n)^* = \mathscr{L}(\mathbb{R}^n,\mathbb{R}).$$

An $$m \times n$$ matrix is an element of $$\mathscr{L}(\mathbb{R}^n,\mathbb{R}^m)$$ and a choice of basis for $$\mathbb{R}^n$$.

$$\dim \mathscr{L}(V,W) = \dim V \cdot \dim W.$$

In particular,

$$\dim \mathscr{L}(\mathbb{R}^m,\mathbb{R}^n) = \dim \mathbb{R}^m \cdot \dim \mathbb{R}^n = m\cdot n.$$

# Transposes of linear maps

Let $$A \in \mathscr{L}(\mathbb{R}^n,\mathbb{R}^m)$$.

Define $$A^T \in \mathscr{L}((\mathbb{R}^m)^*,(\mathbb{R}^n)^*)$$ by

$$A^T f x = f(Ax),\qquad f \in (\mathbb{R}^m)^*, x \in \mathbb{R}^n,$$

called the **transpose** of $$A$$.

# Transposes of matrices

We remind ourselves that $$\{e_k^T: k \in [m]\}$$ is a basis for $$(\mathbb{R}^m)^*$$
and $$\{e_j^T: j \in [n]\}$$ is a basis for $$\mathbb{R}^n$$.
Thus, $$A^T \in \mathscr{L}((\mathbb{R}^m)^*,(\mathbb{R}^n)^*)$$ is also defined by

$$A^T e_k^T e_j = e_k^T(Ae_j),\qquad j \in [n], k \in [m].$$

# Bilinear maps



# Tenosr products




# Determinants



# Fréchet derivative



# Ordinary Least Squares (OLS)

