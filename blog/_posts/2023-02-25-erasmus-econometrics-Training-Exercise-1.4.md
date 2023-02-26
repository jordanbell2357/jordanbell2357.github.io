---
layout: post
title: Erasmus Econometrics Training Exercise 1.4
---

# Erasmus Econometrics Training Exercise 1.4

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
> where $$\sigma_*^2$$ is the variance of $$x^*$$ and $$\sigma_v^2$$ that of $$v$$.
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

# (a)

## Unbiased sample variance

$$s_x^2 = \frac{1}{n-1} \sum_{i=1}^n (x_i - \overline{x})^2$$

$$s_y^2 = \frac{1}{n-1} \sum_{i=1}^n (y_i - \overline{y})^2$$

## Sample covariance

$$\mathrm{cov}(x,y) = \frac{1}{n-1} \sum_{i=1}^n (x_i-\overline{x})(y_i-\overline{y})$$

## Sample correlation coefficient

Let $$A=\frac{1}{n-1}$$.

$$
\begin{align*}
\rho_{x,y} &= \dfrac{\mathrm{cov}(x,y)}{s_x s_y}\\
&=\dfrac{A \sum_{i=1}^n (x_i-\overline{x})(y_i-\overline{y})}{\sqrt{A \sum_{i=1}^n (x_i - \overline{x})^2}\sqrt{\sum_{i=1}^n (y_i - \overline{y})^2}}\\
&=\dfrac{\sum_{i=1}^n (x_i-\overline{x})(y_i-\overline{y})}{\sqrt{\sum_{i=1}^n (x_i - \overline{x})^2} \sqrt{\sum_{i=1}^n (y_i - \overline{y})^2}}
\end{align*}
$$

## Estimator $$b$$ of $$\beta$$

$$
\begin{align*}
b=&\dfrac{\sum_{i=1}^n (x_i-\overline{x})(y_i-\overline{y})}{\sum_{i=1}^n (x_i-\overline{x})^2}\\
&= \dfrac{(n-1) \textrm{cov}(x,y)}{(n-1) s_x^2}\\
&=\dfrac{\mathrm{cov}(x,y)}{s_x^2}
\end{align*}
$$

$$x_i = x_i^*+v_i$$, and $$v_i$$ are uncorrelated with $$x_i^*$$. It follows that

$$s_x^2 = s_{x^*}^2 + 2 \mathrm{cov}(x,v) + s_v^2 = s_{x^*}^2 + s_v^2$$

Thus

$$
b = \dfrac{\mathrm{cov}(x,y)}{s_{x^*}^2+s_v^2}
$$

is the way that $$b$$ depends on the variance of the measurement errors.

# (b)


$$
\begin{align*}
\epsilon_i &= y_i - \alpha - \beta x_i\\
&=\alpha + \beta x_i^* + \epsilon_i^* - \alpha - \beta x_i\\
&=\beta(x_i^* - x_i)+\epsilon_i^*\\
&=\beta(-v_i) + \epsilon_i^*\\
&=-\beta v_i + \epsilon_i^*
\end{align*}
$$

