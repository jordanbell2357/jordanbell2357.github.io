---
layout: post
title: Products in the category of sets
---

For any sets $$X$$ and $$Y$$, let $$Y^X$$ denote the set of all functions with domain $$X$$ and image
contained in $$Y$$.

Let $$A$$ and $$B$$ be sets.
For sets $$Q$$ and functions $$q_A$$ and $$q_B$$, we define the following predicate:

> $$\mathbf{Compatible}_{A,B}(Q,q_A,q_B)$$: $$q_A \in A^Q$$ and $$q_B \in B^Q$$ 

If $$\mathbf{Compatible}_{A,B}(P,p_A,p_B)$$ is true, define the predicate:

> $$\mathbf{Prod}_{A,B}(P,p_A,p_B)$$: if 
> $$\mathbf{Compatible}_{A,B}(Q,q_A,q_B)$$ is true, then there 
> exists a unique
> function $$f:Q \to P$$ such that $$p_A \circ f = q_A$$ and $$p_B \circ f = q_B$$.[^1]

[^1]: [Site copy of quiver diagram](/LaTeX/quiver/product.png)

<!-- https://q.uiver.app/?q=WzAsNCxbMCwyLCJBIl0sWzQsMiwiQiJdLFsyLDMsIlAiXSxbMiwwLCJRIl0sWzIsMCwicF9BIiwyXSxbMiwxLCJwX0IiXSxbMywwLCJxX0EiXSxbMywxLCJxX0IiLDJdLFszLDIsIlxcZXhpc3RzICEgZiIsMSx7InN0eWxlIjp7ImJvZHkiOnsibmFtZSI6ImRhc2hlZCJ9fX1dXQ== -->
<iframe class="quiver-embed" src="https://q.uiver.app/?q=WzAsNCxbMCwyLCJBIl0sWzQsMiwiQiJdLFsyLDMsIlAiXSxbMiwwLCJRIl0sWzIsMCwicF9BIiwyXSxbMiwxLCJwX0IiXSxbMywwLCJxX0EiXSxbMywxLCJxX0IiLDJdLFszLDIsIlxcZXhpc3RzICEgZiIsMSx7InN0eWxlIjp7ImJvZHkiOnsibmFtZSI6ImRhc2hlZCJ9fX1dXQ==&embed" width="688" height="560" style="border-radius: 8px; border: none;"></iframe>


A **product** of $$A$$ and $$B$$ is (a) a set $$P$$ and
functions (b) $$p_A:P \to A$$ and (c) $$p_B:P \to B$$ such
(d) $$\mathbf{Prod}_{A,B}(P,p_A,p_B)$$ is true.


Suppose that $$P,p_A,f_B$$ and $$Q,q_A,q_B$$ are products of $$A$$ and $$B$$.
Because $$P,p_A,f_B$$ is a product of $$A$$ and $$B$$, there is a unique function
$$f:Q \to P$$ such that $$p_A \circ f = q_A$$ and $$p_B \circ f = q_B$$.

Likewise, because $$Q,q_A,q_B$$ is a product of $$A$$ and $$B$$, there is a unique function
$$g:P \to Q$$ such that $$q_A \circ g = p_A$$ and $$q_B \circ g = p_B$$.



On the one hand, because $$\mathbf{Prod}_{A,B}(P,p_A,p_B)$$ is true, there exists a unique function
$$h:P \to P$$ such that $$p_A \circ h = q_A$$ and $$p_B \circ h = q_B$$.




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

<table>
  <tr>
    <th>\(p_A \circ \phi\)</th>
    <th>\(p_B \circ \phi\)</th>
  </tr>
  <tr>
    <td>\(=(p_A \circ f) \circ g\)</td>
    <td>\(=(p_B \circ f) \circ g\)</td>
  </tr>
  <tr>
    <td>\(=q_A \circ g\)</td>
    <td>\(=q_B \circ g\)</td>
  </tr>
  <tr>
    <td>\(=p_A\)</td>
    <td>\(=p_B\)</td>
  </tr>
</table>
  

 
On the one hand:
Define $$\phi=f \circ g$$.
Because
$$g:P \to Q$$ and $$f:Q \to P$$, we have (i) $$\phi:P \to P$$, (ii) $$p_A \circ \phi:P \to A$$,
and (iii) $$p_B \circ \phi:P \to B$$.




Define $$\psi=g \circ f$$, and we have $$\psi:Q \to Q$$ and 
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

[Basic categorial constructions](https://www-users.cse.umn.edu/~garrett/m/fun/Notes/06_categories.pdf)