---
layout: post
title: Products in the category of sets
---

Let $$A$$ and $$B$$ be sets. A product of $$A$$ and $$B$$ is a set $$P$$ and
functions $$p_A:P \to A$$ and $$p_B:P \to B$$ such that if $$Q$$ is a set and
$$q_A:Q \to A$$ and $$q_B:Q \to B$$ are functions, then there exists a unique
function $$f:Q \to P$$ such that $$p_A \circ f = q_A$$ and $$p_B \circ f = q_B$$.[^1]

[^1]: [Site copy of quiver diagram](/LaTeX/quiver/product.png)

<!-- https://q.uiver.app/?q=WzAsNCxbMCwyLCJBIl0sWzQsMiwiQiJdLFsyLDMsIlAiXSxbMiwwLCJRIl0sWzIsMCwicF9BIiwyXSxbMiwxLCJwX0IiXSxbMywwLCJxX0EiXSxbMywxLCJxX0IiLDJdLFszLDIsIlxcZXhpc3RzICEgZiIsMSx7InN0eWxlIjp7ImJvZHkiOnsibmFtZSI6ImRhc2hlZCJ9fX1dXQ== -->
<iframe class="quiver-embed" src="https://q.uiver.app/?q=WzAsNCxbMCwyLCJBIl0sWzQsMiwiQiJdLFsyLDMsIlAiXSxbMiwwLCJRIl0sWzIsMCwicF9BIiwyXSxbMiwxLCJwX0IiXSxbMywwLCJxX0EiXSxbMywxLCJxX0IiLDJdLFszLDIsIlxcZXhpc3RzICEgZiIsMSx7InN0eWxlIjp7ImJvZHkiOnsibmFtZSI6ImRhc2hlZCJ9fX1dXQ==&embed" width="688" height="560" style="border-radius: 8px; border: none;"></iframe>

Suppose that $$P,p_A,f_B$$ and $$Q,q_A,q_B$$ are products of $$A$$ and $$B$$.
Because $$P,p_A,f_B$$ is a product of $$A$$ and $$B$$, there is a unique function
$$f:Q \to P$$ such that $$p_A \circ f = q_A$$ and $$p_B \circ f = q_B$$.

Likewise, because $$Q,q_A,q_B$$ is a product of $$A$$ and $$B$$, there is a unique function
$$g:P \to Q$$ such that $$q_A \circ g = p_A$$ and $$q_B \circ g = p_B$$.

Define $$\phi=f \circ g$$. Because
$$g:P \to Q$$ and $$f:Q \to P$$, we have $$\phi:P \to P$$.
We have

$$
\begin{align}
p_A \circ \phi&=p_A \circ (f \circ g)\\
&=(p_A \circ f) \circ g\\
&=q_A \circ g\\
&=p_A
\end{align}
$$

and, similarly, 

$$
\begin{align}
p_B \circ \phi&=p_B \circ (f \circ g)\\
&=(p_B \circ f) \circ g\\
&=q_B \circ g\\
&=p_B
\end{align}
$$

Define $$\psi=g \circ f$$, and we have $$\psi:Q \to Q$$.
Like above with $$\phi$$, we have

$$
\begin{align}
q_A \circ \phi&=q_A \circ (g \circ f)\\
&=(q_A \circ g) \circ f\\
&=p_A \circ f\\
&=q_A
\end{align}
$$

and

$$
\begin{align}
q_B \circ \psi&=q_B \circ (g \circ f)\\
&=(q_B \circ g) \circ f\\
&=q_B \circ f\\
&=q_B
\end{align}
$$


---

[Category Theory: a concise course. 5. Product, Coproduct, Exponential](https://categorytheory.gitlab.io/product_coproduct_exponential.html)

<https://arbital.com/p/empty_set_universal_property/>