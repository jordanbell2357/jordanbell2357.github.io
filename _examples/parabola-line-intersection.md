---
layout: post
title: Intersections of parabolas and lines
topic: directrix
---

$$f(x)=ax^2$$.

Let $$A=(x_A,y_A)$$ be a point on the parabola. Then

$$
\begin{align*}
y_A&=f(x_A)\\
&=ax_A^2
\end{align*}
$$

Let

$$
\begin{align*}
f_m(x)&=m(x-x_A)+y_A\\
&=m(x-x_A)+ax_A^2
\end{align*}
$$

Let

$$
\begin{align*}
g_m(x)&=f(x)-f_m(x)\\
&=ax^2-\left(m(x-x_A)+y_A\right)\\
&=ax^2-mx+mx_A-y_A\\
&=ax^2-mx+mx_A-ax_A^2
\end{align*}
$$

Let $$D_m$$ be the discriminant of $g_m(x)$$:

$$
\begin{align*}
D_m &= (-m)^2 - 4(a)(mx_A-ax_A^2)\\
&=m^2 -4amx_A+4a^2x_A^2\\
&=(m-2ax_A)^2
\end{align*}
$$

On the one hand, $$D_m=0$ is equivalent to the line and parabola having intersection multiplicity 2 at point $$A$$.

On the other hand, $$D_m=0$$ is equivalent to $$m=2ax_A$$.

Thus for

$$m_A=2ax_A$$

the line

$$
\begin{align*}
f_A(x)=f_{m_A}(x)\\
&=m_A(x-x_A)+ax_A^2\\
&=2ax_A(x-x_A)+ax_A^2
\end{align*}
$$

is tangent to the parabola $$f$$ at the point $$A$$.

[Intersection of parabola and line](https://www.desmos.com/calculator/rhbzxqn8lx)

<iframe src="https://www.desmos.com/calculator/rhbzxqn8lx?embed" width="500" height="500" style="border: 1px solid #ccc" frameborder=0></iframe>
