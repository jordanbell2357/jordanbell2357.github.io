---
layout: post
title: Erasmus Econometrics Training Exercise 2.2
---

> In the wage database, education is measured in terms of a single variable ‘Educ’ with values 1, 2, 3, and 4. The
> multiple regression model (with Educ as 4-th explanatory factor) assumes a constant marginal effect:
>
> $$
> \dfrac{\partial \mathrm{log(Wage)}}{\partial \mathrm{Educ}} = \beta_4.
> $$
>
> This means that increasing education by one level always leads to the same relative wage increase. This effect may,
> however, depend on the education level, for example, if the effect is smaller for a shift from eduction level 1 to 2 as
> compared to a shift from 3 to 4.

# (a)

> (a) The wage equation presented at the start of Lecture 2.2 contains four explanatory factors (apart from the
> constant term). Formulate the null hypothesis that none of these four factors has effect on wage in the form
> $$R\beta=r$$, that is, determine $$R$$ and $$r$$.

$$
\mathrm{log(Wage)} = \beta_1 + \beta_2 \mathrm{Female} + \beta_3 \mathrm{Age} + \beta_4 \mathrm{Education}
+\beta_5 \mathrm{parttime} + \epsilon 
$$

Let

$$
\beta=
\begin{pmatrix}
\beta_1\\
\beta_2\\
\beta_3\\
\beta_4\\
\beta_5
\end{pmatrix} \in \mathbb{R}^5
$$

Then

$$
\begin{pmatrix}
0&0&0&0&0\\
0&1&0&0&0\\
0&0&1&0&0\\
0&0&0&1&0\\
0&0&0&0&1
\end{pmatrix}
\beta = 0 \in \mathbb{R}^5
$$

or

$$
\underbrace{
\begin{pmatrix}
0&1&0&0&0\\
0&0&1&0&0\\
0&0&0&1&0\\
0&0&0&0&1
\end{pmatrix}
}_{R}
\beta = \underbrace{0}_{r} \in \mathbb{R}^4
$$

for $$R:\mathbb{R}^5 \to \mathbb{R}^4$$ and $$r \in \mathbb{R}^4$$.

# (b)

> (b) Extend the wage equation presented at the start of Lecture 2.2 by allowing for education effects that depend on the education level.
>
> Hint: Use dummy variables for education levels 2, 3, and 4.

$$
D_k = \begin{cases}
1&\mathrm{Education} \in \{k\}\\
0&\mathrm{Education} \in \{1,2,3,4\} \setminus \{k\}
\end{cases}
$$


$$
\begin{align*}
\mathrm{log(Wage)} &= \gamma_1 + \gamma_2 \mathrm{Female} + \gamma_3 \mathrm{Age}\\
&+ \gamma_4 D_2 + \gamma_5 D_3 + \gamma_6 D_4\\
&+\gamma_7 \mathrm{parttime} + \epsilon
\end{align*}
$$



# (c)

> (c) The model of part (b) is more general than the original wage equation. The original model can be obtained
> from the model in part (b) by imposing linear restrictions of the type $$R \beta = r$$. Derive the number of restrictions
> ($$g$$) and determine $$R$$ and $$r$$.

$$
\begin{gather*}
\beta_4=\gamma_4\\
\beta_4 = \gamma_5-\gamma_4\\
\beta_4 = \gamma_6-\gamma_5
\end{gather*}
$$

$$
\gamma_5=2\gamma_4, \qquad \gamma_6=3\gamma_4
$$

$$
\begin{pmatrix}
0&0&0&-2&1&0&0\\
0&0&0&-3&0&1&0
\end{pmatrix}
\gamma=
\begin{pmatrix}
0\\
0
\end{pmatrix}
$$