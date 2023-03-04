---
layout: post
title: Tate's thesis
---

Let $$p$$ be a prime and let $$N_p=\{0,\ldots,p-1\}$$.

Define the $$p$$-adic rationals $$\mathbb{Q}_p$$ to be the set of functions $$x:\mathbb{Z} \to N_p$$
for which there exists some $$k_x$$ such that $$x(k)=0$$ for all $$k<k_x$$.

For $$x \in \mathbb{Q}_p$$, define the $$p$$-adic valuation

$$v_p(x)=\inf \{k \in \mathbb{Z}: x(k) \neq 0\}$$

If $$x(k)=0$$ for all $$k \in \mathbb{Z}$$, then $$v_p(x) = \infty$$.

Define the $$p$$-adic integers

$$\mathbb{Z}_p = \{x \in \mathbb{Q}_p : v_p(x) \geq 0\}$$

Define the $$p$$-adic absolute value for $$x \in \mathbb{Q}_p$$ by

$$|x|_p = p^{-v_p(x)}$$

The $$p$$-adic absolute value satisfies the ultrametric property, for $$x,y \in \mathbb{Q}_p$$,

$$|x+y|_p \leq \max\{|x|_p,|y|_p\}$$

Expressed using the $$p$$-adic absolute value,

$$\mathbb{Z}_p = \{x \in \mathbb{Q}_p: |x|_p \leq 1\}$$

that is, the $$p$$-adic integers are a closed ball of radius 1 in the $$p$$-adic rationals.

$$\mathbb{Q}_p$$ is a field and $$\mathbb{Z}_p$$ is a ring. The multiplicative group of units
of $$\mathbb{Z}_p$$ is

$$\mathbb{Z}_p^\times  = \{x \in \mathbb{Z}_p: |x|_p = 1\}$$

The additive group $$\mathbb{Q}_p$$ is a locally compact abelian group. $$\mathbb{Z}_p$$ is a compact set
in $$\mathbb{Q}_p$$ so it has finite Haar measure, and it is an open set in $$\mathbb{Q}_p$$ so it has positive Haar measure.
Therefore there is a unique unique Haar measure $$\mu_p$$ on
$$\mathbb{Q}_p$$ such that $$\mu_p(\mathbb{Z}_p)=1$$.

For $$x \in \mathbb{Q}_p$$ and for $$k \in \mathbb{Z}$$,
define $$p^k x \in \mathbb{Q}_p$$ by

$$(p^k x)(j) = x(j-k). \qquad j \in \mathbb{Z}$$

In particular, expressed using $$p$$-adic valuations,

$$p^k \mathbb{Z}_p = \{x \in \mathbb{Q}_p: v_p(x) \geq k\}$$

and expressed using $$p$$-adic absolute values,

$$p^k \mathbb{Z}_p = \{x \in \mathbb{Q}_p: |x|_p \leq p^{-k}\}$$

$$\mu_p(p^k \mathbb{Z}_p)=p^{-k}$$

For a Borel set $$A$$ in $$\mathbb{Q}_p$$ and for $$x \in \mathbb{Q}_p$$,

$$\mu_p(x \cdot A) = |x|_p \mu_p(A)$$

For $$f \in L^1(\mathbb{Q}_p)$$ and $$x \in \mathbb{Q}_p \setminus \{0\}$$,

$$\int_{\mathbb{Q}_p} f(x^{-1}y)d\mu_p(y) = |x|_p \int_{\mathbb{Q}_p} f(y) d\mu_p(y)$$


The multiplicative group

$$\mathbb{Q}_p^\times = \{x \in \mathbb{Q}_p : x \neq 0\} = \mathbb{Q}_p \setminus \{0\}$$

is a locally compact abelian group

The restriction of $$\mu_p$$ to the Borel $$\sigma$$-algebra of $$\mathbb{Q}_p^\times$$
is a Borel measure on $$\mathbb{Q}_p^\times$$.

One then proves that

$$d\nu_p(x) = \frac{p}{p-1} \dfrac{1}{|x|_p} d\mu_p(x)$$

is a Haar measure on $$\mathbb{Q}_p^\times$$ with $$\nu_p(\mathbb{Z}_p^\times)=1$$.

One then proves that for $$s \in \mathbb{C}$$ with $$\mathrm{Re}(s)>-1$$,

$$\int_{\mathbb{Z}_p^\times} |x|_p^s d\mu_p(x) = \dfrac{p-1}{p(1-p^{-1-s})}$$

and then that for $$\mathrm{Re}(x)>0$$,

$$\int_{\mathbb{Z}_p^\times} |x|_p^s d\mu_p(x) = \dfrac{1}{1-p^{-s}}$$


For each $$x \in \mathbb{Q}_p$$, the collection

$$\{x + p^k \mathbb{Z}_p : k \ in \mathbb{Z}\}$$

is a local base for the topology of $$\mathbb{Q}_p$$.