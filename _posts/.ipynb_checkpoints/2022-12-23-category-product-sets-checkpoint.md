---
layout: post
title: Products in the category of sets
---

For any sets $$X$$ and $$Y$$, let $$Y^X$$ denote the set of all functions with domain $$X$$ and image
contained in $$Y$$.[^1]

[^1]: Indeed, this makes sense when one or both of $$X$$ or $$Y$$ is the empty set.

Let sets $$A$$ and $$B$$ be given.

For sets $$Q$$ and functions $$q_A$$ and $$q_B$$, we define the predicate

<div class="bubblebox_white">
\(\mathtt{Compatible}_{A,B}(Q,q_A,q_B)\): \(q_A \in A^Q\) and \(q_B \in B^Q\)
</div>

If $$\mathtt{Compatible}_{A,B}(P,p_A,p_B)$$ is true, define the predicate[^2]

[^2]: [Site copy of quiver diagram](/LaTeX/quiver/product.png)

<div class="bubblebox_white">
\(\mathtt{Prod}_{A,B}(P,p_A,p_B)\): If \(\mathtt{Compatible}_{A,B}(Q,q_A,q_B)\) is true, then there 
exists a unique function \(f \in P^Q\) such that \(p_A \circ f = q_A\) and \(p_B \circ f = q_B\).
</div>
  

<!-- https://q.uiver.app/?q=WzAsNCxbMCwyLCJBIl0sWzQsMiwiQiJdLFsyLDMsIlAiXSxbMiwwLCJRIl0sWzIsMCwicF9BIiwyXSxbMiwxLCJwX0IiXSxbMywwLCJxX0EiXSxbMywxLCJxX0IiLDJdLFszLDIsIlxcZXhpc3RzICEgZiIsMSx7InN0eWxlIjp7ImJvZHkiOnsibmFtZSI6ImRhc2hlZCJ9fX1dXQ== -->
<iframe class="quiver-embed" src="https://q.uiver.app/?q=WzAsNCxbMCwyLCJBIl0sWzQsMiwiQiJdLFsyLDMsIlAiXSxbMiwwLCJRIl0sWzIsMCwicF9BIiwyXSxbMiwxLCJwX0IiXSxbMywwLCJxX0EiXSxbMywxLCJxX0IiLDJdLFszLDIsIlxcZXhpc3RzICEgZiIsMSx7InN0eWxlIjp7ImJvZHkiOnsibmFtZSI6ImRhc2hlZCJ9fX1dXQ==&embed" width="688" height="560" style="border-radius: 8px; border: none;"></iframe>

A **product** of $$A$$ and $$B$$ is a set $$P$$, a function $$p_A \in A^P$$,
and a function $$p_B \in B^P$$ such that $$\mathtt{Prod}_{A,B}(P,p_A,p_B)$$ is true.

Suppose that $$\mathtt{Prod}_{A,B}(P,p_A,p_B)$$ is true and $$\mathtt{Prod}_{A,B}(Q,q_A,q_B)$$ is true.
Because $$\mathtt{Prod}_{A,B}(P,p_A,p_B)$$ is true and $$\mathtt{Compatible}_{A,B}(Q,q_A,q_B)$$ is true,
there is a unique function
$$f \in P^Q$$ such that $$p_A \circ f = q_A$$ and $$p_B \circ f = q_B$$.

Likewise, because $$\mathtt{Prod}_{A,B}(Q,q_A,q_B)$$ is true and
$$\mathtt{Compatible}_{A,B}(P,p_A,p_B)$$ is true,
there is a unique function
$$g \in Q^P$$ such that $$q_A \circ g = p_A$$ and $$q_B \circ g = p_B$$.

From $$f \in P^Q$$ and $$g \in Q^P$$, it follows $$f \circ g \in P^P$$.
Let

$$
\phi = f \circ g, \qquad \phi \in P^P.
$$

$$\mathtt{Compatible}_{A,B}(P,p_A \circ \phi,p_B \circ \phi)$$ is true, so
there is a unique function $$h \in P^P$$ such that 

$$p_A \circ h = p_A \circ \phi, \qquad p_B \circ h = p_B \circ \phi.$$




---

[Category Theory: a concise course. 5. Product, Coproduct, Exponential](https://categorytheory.gitlab.io/product_coproduct_exponential.html)

[Basic categorial constructions](https://www-users.cse.umn.edu/~garrett/m/fun/Notes/06_categories.pdf)