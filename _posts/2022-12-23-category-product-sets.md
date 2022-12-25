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

Suppose that $$\mathtt{Prod}_{A,B}(P,p_A,p_B)$$ is true and $$\mathtt{Prod}_{A,B}(Q,q_A,q_B)$$ is true.
Because $$\mathtt{Prod}_{A,B}(P,p_A,p_B)$$ is true and $$\mathtt{Compatible}_{A,B}(Q,q_A,q_B)$$ is true,
there is a unique function $$f \in P^Q$$ such that

$$
\begin{equation}
p_A \circ f = q_A
\label{qA}
\end{equation}
$$

and

$$
\begin{equation}
\quad p_B \circ f = q_B.
\label{qB}
\end{equation}
$$


Likewise, because $$\mathtt{Prod}_{A,B}(Q,q_A,q_B)$$ is true and
$$\mathtt{Compatible}_{A,B}(P,p_A,p_B)$$ is true,
there is a unique function
$$g \in Q^P$$ such that

$$
\begin{equation}
q_A \circ g = p_A
\label{pA}
\end{equation}
$$

and

$$
\begin{equation}
\quad q_B \circ g = p_B.
\label{pB}
\end{equation}
$$

From $$f \in P^Q$$ and $$g \in Q^P$$, it follows that $$f \circ g \in P^P$$.
Let $$\phi = f \circ g$$, $$\phi \in P^P$$.

From $$\phi \in P^P$$ and $$p_A \in A^P$$, it follows that
$$p_A \circ \phi \in A^P$$, and likewise from $$\phi \in P^P$$ and
$$p_B \in B^P$$, it follows that $$p_B \circ \phi \in B^P$$.
Therefore,
$$\mathtt{Compatible}_{A,B}(P,p_A \circ \phi,p_B \circ \phi)$$ is true, and
thus there is a unique function $$h \in P^P$$ such that 

$$
\begin{equation}
p_A \circ h = p_A \circ \phi
\label{pAphi}
\end{equation}
$$

and

$$
\begin{equation}
p_B \circ h = p_B \circ \phi
\label{pBphi}
\end{equation}
$$.

Then[^3]

[^3]: [Category Theory: a concise course. 5. Product, Coproduct, Exponential](https://categorytheory.gitlab.io/product_coproduct_exponential.html)

$$
\begin{align*}
p_A \circ \phi&= p_A \circ (f \circ g)\\
&=(p_A \circ f) \circ g \qquad \textrm{by associativity}\\
&=q_A \circ g \qquad \textrm{by} \eqref{}\\
&=p_A \; \textrm{by} \; q_A \circ g = p_A
\end{align*}
$$

$$
\begin{align*}
p_B \circ \phi&=p_B \circ (f \circ g)\\
&=(p_B \circ f) \circ g \; \textrm{by associativity}\\
&=q_B \circ g \; \textrm{by} \; p_B \circ f = q_B\\
&=p_B \; \textrm{by} \; q_B \circ g = p_B
\end{align*}
$$

From $$g \in Q^P$$ and $$f \in P^Q$$, it follows that $$g \circ f \in Q^Q$$.
Let $$\psi = g \circ f$$, $$\psi \in Q^Q$$.

$$
\begin{align*}
q_A \circ \psi&=q_A \circ (g \circ f)\\
&=(q_A \circ g) \circ f \; \textrm{by associativity}\\
&=p_A \; \textrm{by} \; \eqref{pA}
\end{align*}
$$

---

[Basic categorial constructions](https://www-users.cse.umn.edu/~garrett/m/fun/Notes/06_categories.pdf)

<script>
  MathJax = {
    tex: {
      tags: 'ams'  // should be 'ams', 'none', or 'all'
    }
  };
</script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js"></script>