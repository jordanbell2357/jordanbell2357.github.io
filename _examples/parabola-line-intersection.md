---
layout: post
title: Intersections of parabolas and lines
topic: directrix
---

\\(
\newcommand{\A}[1]{\colorbox{CornflowerBlue}{$\displaystyle #1$}}
\newcommand{\B}[1]{\colorbox{lightgray}{$\displaystyle #1$}}
\newcommand{\C}[1]{\colorbox{BurntOrange}{$\displaystyle #1$}}
\\)

Let 

$$f(x)=ax^2$$

Let $$A=(x_A,y_A)$$ be a point on the parabola $$f$$. Then

$$
\begin{align*}
y_A&=f(x_A)\\
y_A&=ax_A^2
\end{align*}
$$

Let

$$
f_m(x)=m(x-x_A)+y_A
$$

Let

$$
\begin{align*}
g_m(x)&=f(x)-f_m(x)\\
g_m(x)&=ax^2-\left(m(x-x_A)+y_A\right)\\
g_m(x)&=ax^2-mx+mx_A-y_A
\end{align*}
$$

Let $$D_m$$ be the discriminant of $$g_m(x)$$:

$$
\begin{align*}
D_m &= (-m)^2 - 4(a)(mx_A-y_A)\\
D_m &= (-m)^2 - 4(a)(mx_A-ax_A^2)\\
D_m&=m^2 -4amx_A+4a^2x_A^2\\
D_m&=(m-2ax_A)^2
\end{align*}
$$

On the one hand, $$D_m=0$$ is equivalent to $$m=2ax_A$$.

On the other hand, $$D_m=0$$ is equivalent to the line $$f_m$$ and parabola $$f$$ having intersection multiplicity 2 at point $$A=(x_A,y_A)$$.

Thus for

$$\B{m_A=2ax_A}$$

the line

$$
\begin{gather*}
f_A(x)=f_{m_A}(x)\\
f_A(x)=m_A(x-x_A)+y_A
\end{gather*}
$$

in other words

$$
\A{f_A(x)=2ax_A(x-x_A)+y_A}
$$

is tangent to the parabola $$f(x)=ax^2$$ at the point $$A=(x_A,y_A)$$.

[Intersection of parabola and line](https://www.desmos.com/calculator/m9ioqdzi2e)

<iframe src="https://www.desmos.com/calculator/m9ioqdzi2e?embed" width="500" height="500" style="border: 1px solid #ccc" frameborder=0></iframe>