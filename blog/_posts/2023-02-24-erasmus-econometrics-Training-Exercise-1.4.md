---
layout: post
title: Erasmus Econometrics Training Exercise 1.4
---

> Consider the situation where the $$x$$-variable is observed with measurement error, which is rather common for complex macroeconomic variables like national income.
>
> Let $$x^*$$ be the true, unobserved economic variable, and let the data generating process (DGP) be given by
>
> $$y_i = \alpha + \beta x_i^* + \epsilon_i^*,$$
>
> where $$x_i^*$$ and $$\epsilon_i^*$$ are uncorrelated.
>
> The observed $$x$$-values are $$x_i = x_i^* + v_i$$, with measurement errors $$v_i$$ that are uncorrelated with $$x_i^*$$
> and $$\epsilon_i^*$$. The signal-to-noise ratio is defined as $$SN = \frac{\sigma_*^2}{\sigma_v^2}$$,
> where $$\sigma_*^2$$ is te variance of $$x^*$$ and $$\sigma_v^2$$ that of $$v$$.
>
> The estimated regression model is $$y_i = \alpha + \beta x_i + \epsilon_i$$, and we consider the least squares estimator $$b$$ of $$\beta$$.
>
> **(a)** Do you think that the value of $$b$$ depends on the variance of the measurement errors? Why?
>
> **(b)** Show that
>
> $$b = \beta + \dfrac{\sum_{i=1}^n (x_i-\overline{x})(\epsilon_i-\overline{\epsilon})}{\sum_{i=1}^n (x_i-\overline{x})^2}.$$
>
> **(c)** Show that $$\epsilon_i = \epsilon_i^*-\beta v_i$$.
>
> **(d)** Show that the covariance between $$x_i$$ and $$\epsilon_i$$ is equal to $$-\beta \sigma_v^2$$.
>
> **(e)** Show that for large sample size $$n$$ we get $$b-\beta \approx \dfrac{-\beta \sigma_v^2}{\sigma_*^2+\sigma_v^2}$$
>
> **(f)** Compute the approximate bias $$b-\beta$$ for $$\beta=1$$ in the cases $$SN=1$$, $$SN=3$$, and $$SN=10$$.