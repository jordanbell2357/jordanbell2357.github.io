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





