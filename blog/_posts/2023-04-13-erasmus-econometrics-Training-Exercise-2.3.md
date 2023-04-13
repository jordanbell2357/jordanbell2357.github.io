---
layout: post
title: Erasmus Econometrics Training Exercise 2.3
---

# Ordinary Least Squares (OLS)

Observed data: $$y \in \mathbb{R}^n$$, $$X \in \mathscr{L}(\mathbb{R}^k,\mathbb{R}^n)$$

Unobserved data: $$\beta \in \mathbb{R}^k$$, $$\epsilon \in \mathbb{R}^n$$

Model: $$y = X\beta + \epsilon$$

Estimate $$\beta$$ by $$b$$ so that $$Xb$$ is close to $$y$$, i.e. $$y-Xb$$ is close to $$0 \in \mathbb{R}^n$$.

Define $$e=y-Xb$$

$$y \in \mathbb{R}^n$$, $$X \in \mathscr{L}(\mathbb{R}^k,\mathbb{R}^n)$$, $$b \in \mathbb{R}^k$$, $$e \in \mathbb{R}^n$$

Ordinary Least Squares (OLS): minimize $$S:\mathbb{R}^n \to \mathbb{R}$$ defined by

$$S(b) = e^T e = \sum_{i=1}^n e_i^2$$

For a finite dimensional real vector space $$V$$, we define the dual space $$V^*$$ to be the 
set of linear maps $$V \to \mathbb{R}$$, which is itself a finite dimensional real vector space, with the
same dimension.

We remark that $$e^T \in (\mathbb{R}^n)^*$$. There is a canonical isomorphism between
$$\mathbb{R}^n$$ and  $$(\mathbb{R}^n)^{**}$$, but there is not a **canonical** isomorphism
between $$\mathbb{R}^n$$ and $$(\mathbb{R}^n)^*$$.

Elements of $$(\mathbb{R}^n)^*$$ are called **row vectors** in some settings and **covectors** in some settings.
In the intersection of these settings, row vector is a synonym for covector (and column vector is a synonym for vector).

