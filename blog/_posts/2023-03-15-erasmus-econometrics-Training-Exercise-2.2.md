---
layout: post
title: Erasmus Econometrics Training Exercise 2.2
---

> In the wage database, education is measured in terms of a single variable ‘Educ’ with values 1, 2, 3, and 4. The
> multiple regression model (with Educ as 4-th explanatory factor) assumes a constant marginal effect:
>
> $$
> \dfrac{\partial \log(\mathrm{Wage})}{\partial \mathrm{Educ}} = \beta_4.
> $$
>
> This means that increasing education by one level always leads to the same relative wage increase. This effect may,
> however, depend on the education level, for example, if the effect is smaller for a shift from eduction level 1 to 2 as
> compared to a shift from 3 to 4.

# (a)

> (a) The wage equation presented at the start of Lecture 2.2 contains four explanatory factors (apart from the
> constant term). Formulate the null hypothesis that none of these four factors has effect on wage in the form
> $$R\beta=r$$, that is, determine $$R$$ and $$r$$.

- Wage = W
- Female = F
- Age = A
- Education = E
- Parttime = P

$$
\log W = \beta_1 + \beta_2 F + \beta_3 A + \beta_4 E +\beta_5 P + \epsilon 
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
\beta = 
\begin{pmatrix}
0\\
0\\
0\\
0\\
0
\end{pmatrix}
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
\beta = \underbrace{\begin{pmatrix}
0\\
0\\
0\\
0
\end{pmatrix}}_{r}
$$

for $$R:\mathbb{R}^5 \to \mathbb{R}^4$$ and $$r \in \mathbb{R}^4$$.

# (b)

> (b) Extend the wage equation presented at the start of Lecture 2.2 by allowing for education effects that depend on the education level.
>
> Hint: Use dummy variables for education levels 2, 3, and 4.

$$
D_k = \begin{cases}
1&E \in \{k\}\\
0&E \in \{1,2,3,4\} \setminus \{k\}
\end{cases}
$$


$$
\log W = \gamma_1 + \gamma_2 F + \gamma_3 A+ \gamma_4 D_2 + \gamma_5 D_3 + \gamma_6 D_4 + \gamma_7 P + \epsilon
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
\gamma = \begin{pmatrix}
\gamma_1\\
\gamma_2\\
\gamma_3\\
\gamma_4\\
\gamma_5\\
\gamma_6\\
\gamma_7
\end{pmatrix}
=
\begin{pmatrix}
\gamma_1\\
\gamma_2\\
\gamma_3\\
\gamma_4\\
2\gamma_4\\
3\gamma_4\\
\gamma_7
\end{pmatrix}
=
\gamma_1 \begin{pmatrix}
1\\
0\\
0\\
0\\
0\\
0\\
0
\end{pmatrix}
+ \gamma_2 \begin{pmatrix}
0\\
1\\
0\\
0\\
0\\
0\\
0
\end{pmatrix}
+ \gamma_3 \begin{pmatrix}
0\\
0\\
1\\
0\\
0\\
0\\
0
\end{pmatrix}
+ \gamma_4 \begin{pmatrix}
0\\
0\\
0\\
1\\
2\\
3\\
0
\end{pmatrix}
+\gamma_7 \begin{pmatrix}
0\\
0\\
0\\
0\\
0\\
0\\
1
\end{pmatrix}
$$

$$
\underbrace{
\begin{pmatrix}
0&0&0&-2&1&0&0\\
0&0&0&-3&0&1&0
\end{pmatrix}
}_{R}
\gamma=
\underbrace{\begin{pmatrix}
0\\
0
\end{pmatrix}}_{r}
$$

$$g=2$$