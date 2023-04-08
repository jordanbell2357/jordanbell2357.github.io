---
layout: post
title: Erasmus Econometrics Training Exercise 2.3
---

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
&=y^Ty-y^TXb-b^T X^Ty+b^TX^TXb\\
&=
\end{align*}
$$