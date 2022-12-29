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
\(\mathtt{Compatible}_{A,B}(Q,q_A,q_B)\): \(q_A \in A^Q\) and \(q_B \in B^Q\).
</div>

If $$\mathtt{Compatible}_{A,B}(P,p_A,p_B)$$ is true, define the predicate

<div class="bubblebox_white">
\(\mathtt{Prod}_{A,B}(P,p_A,p_B)\): If \(\mathtt{Compatible}_{A,B}(Q,q_A,q_B)\) is true, then there 
exists a unique function \(f \in P^Q\) such that \(p_A \circ f = q_A\) and \(p_B \circ f = q_B\).
</div>

<!-- https://q.uiver.app/?q=WzAsNCxbMCwyLCJBIl0sWzQsMiwiQiJdLFsyLDMsIlAiXSxbMiwwLCJRIl0sWzIsMCwicF9BIiwyXSxbMiwxLCJwX0IiXSxbMywwLCJxX0EiXSxbMywxLCJxX0IiLDJdLFszLDIsIlxcZXhpc3RzICEgZiIsMSx7InN0eWxlIjp7ImJvZHkiOnsibmFtZSI6ImRhc2hlZCJ9fX1dXQ== -->
<iframe class="quiver-embed" src="https://q.uiver.app/?q=WzAsNCxbMCwyLCJBIl0sWzQsMiwiQiJdLFsyLDMsIlAiXSxbMiwwLCJRIl0sWzIsMCwicF9BIiwyXSxbMiwxLCJwX0IiXSxbMywwLCJxX0EiXSxbMywxLCJxX0IiLDJdLFszLDIsIlxcZXhpc3RzICEgZiIsMSx7InN0eWxlIjp7ImJvZHkiOnsibmFtZSI6ImRhc2hlZCJ9fX1dXQ==&embed" width="688" height="560" style="border-radius: 8px; border: none;"></iframe>

<div class="proof">
<div class="topleft">Proof</div>
<h2>➡ \(f \in P^Q\) and \(g \in Q^P\)</h2>
<p>
Suppose that \(\mathtt{Prod}_{A,B}(P,p_A,p_B)\) is true and \(\mathtt{Prod}_{A,B}(Q,q_A,q_B)\) is true.
</p>
  
<p>Because \(\mathtt{Prod}_{A,B}(P,p_A,p_B)\) is true and \(\mathtt{Compatible}_{A,B}(Q,q_A,q_B)\) is true,
there is a unique function \(f \in P^Q\) such that

\(
\begin{equation}
p_A \circ f = q_A
\label{qA}
\end{equation}
\)

and

\(
\begin{equation}
\quad p_B \circ f = q_B.
\label{qB}
\end{equation}
\)
</p>

<p>
Because \(\mathtt{Prod}_{A,B}(Q,q_A,q_B)\) is true and
\(\mathtt{Compatible}_{A,B}(P,p_A,p_B)\) is true,
there is a unique function
\(g \in Q^P\) such that

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
</p>

<h2>➡ \(\phi \in P^P\)</h2>
<p>
From \(f \in P^Q\) and \(g \in Q^P\), it follows that \(f \circ g \in P^P\).
Define

$$\phi = f \circ g, \qquad \phi \in P^P.$$
</p>

<p>
From \(\phi \in P^P\) and \(p_A \in A^P\), it follows that
\(p_A \circ \phi \in A^P\). From \(\phi \in P^P\) and
\(p_B \in B^P\), it follows that \(p_B \circ \phi \in B^P\).
Therefore,
\(\mathtt{Compatible}_{A,B}(P,p_A \circ \phi,p_B \circ \phi)\) is true.
</p>

<p>
Because \(\mathtt{Prod}_{A,B}(P,p_A,p_B)\) is true and \(\mathtt{Compatible}_{A,B}(P,p_A \circ \phi,p_B \circ \phi)\)
is true,
there is a unique function \(h \in P^P\) such that 

$$
\begin{equation}
p_A \circ h = p_A \circ \phi
\label{pAphi}
\end{equation}
$$

and

$$
\begin{equation}
p_B \circ h = p_B \circ \phi.\label{pBphi}
\end{equation}
$$
</p>

<p>
Then

$$
\begin{align*}
p_A \circ \phi&= p_A \circ (f \circ g)\\
&=(p_A \circ f) \circ g \quad \textrm{by associativity}\\
&=q_A \circ g \quad \textrm{by \eqref{qA}}\\
&=p_A \quad \textrm{\eqref{pA}}
\end{align*}
$$

and

$$
\begin{align*}
p_B \circ \phi&=p_B \circ (f \circ g)\\
&=(p_B \circ f) \circ g \quad \textrm{by associativity}\\
&=q_B \circ g \quad \textrm{by \eqref{qB}}\\
&=p_B \quad \textrm{by \eqref{pB}}.
\end{align*}
$$
</p>

<h2>➡ \(\psi \in Q^Q\)</h2>
<p>
From \(g \in Q^P\) and \(f \in P^Q\), it follows that \(g \circ f \in Q^Q\).
Define

$$\psi = g \circ f, \qquad \psi \in Q^Q.$$
</p>

<p>
From \(\psi \in Q^Q\) and \(q_A \in A^Q\), it follows that 
\(q_A \circ \psi \in A^Q\).
From \(\psi \in Q^Q\) and \(q_B \in B^Q\), it follows that
\(q_B \circ \psi \in B^Q\). Therefore,
\(\mathtt{Compatible}_{A,B}(Q,q_A \circ \psi,q_B \circ \psi)\) is true.
</p>

<p>
Because \(\mathtt{Prod}_{A,B}(Q,q_A,q_B)\) is true and
\(\mathtt{Compatible}_{A,B}(Q,q_A \circ \psi,q_B \circ \psi)\) is true,
there is a unique function \(k \in Q^Q\)
such that

$$
\begin{equation}
q_A \circ k = q_A \circ \psi
\label{qApsi}
\end{equation}
$$

and

$$
\begin{equation}
q_B \circ k = q_B \circ \psi.
\label{qBpsi}
\end{equation}
$$
</p>

<p>
Then
      
$$
\begin{align*}
q_A \circ \psi&=q_A \circ (g \circ f)\\
&=(q_A \circ g) \circ f \quad \textrm{by associativity}\\
&=p_A \circ f \quad \textrm{by \eqref{pA}}\\
&=q_A \quad \textrm{by \eqref{qA}}
\end{align*}
$$

and

$$
\begin{align*}
q_B \circ \psi&=q_B \circ (g \circ f)\\
&=(q_B \circ g) \circ f \quad \textrm{by associativity}\\
&=p_B \circ f \quad \textrm{by \eqref{pB}}\\
&=q_B \quad \textrm{by \eqref{qB}}.
\end{align*}
$$
</p>

<h2>➡ \(\textrm{id}_P \in P^P\)</h2>
<p>
\(p_A \circ \textrm{id}_P \in A^P\) and \(p_B \circ \textrm{id}_P \in B^P\),
which means that \(\mathtt{Compatible}_{A,B}(P,p_A \circ \textrm{id}_P,p_B \circ \textrm{id}_P)\) is true.
</p>
  
<p>
Because \(\mathtt{Prod}_{A,B}(P,p_A,p_B)\) is true and \(\mathtt{Compatible}_{A,B}(P,p_A \circ \textrm{id}_P,p_B \circ \textrm{id}_P)\)
is true, there exists a unique function \(h \in P^P\) such that \(

<h2>➡ \(\textrm{id}_Q \in Q^Q\)</h2>
<p>
\(q_A \circ \textrm{id}_Q \in A^Q\) and \(p_B \circ \textrm{id}_Q \in B^Q\),
which means that \(\mathtt{Compatible}_{A,B}(Q,q_A \circ \textrm{id}_Q,p_B \circ \textrm{id}_Q)\) is true.
</p>
  

  
<div class="bottomright">∎</div>
</div>

References[^2] [^3] [^4]



[^2]: [product.png](/LaTeX/quiver/product.png)



[^3]: [Category Theory: a concise course. 5. Product, Coproduct, Exponential](https://categorytheory.gitlab.io/product_coproduct_exponential.html)



[^4]: [Basic categorial constructions](https://www-users.cse.umn.edu/~garrett/m/fun/Notes/06_categories.pdf)

<script>
  MathJax = {
    tex: {
      tags: 'ams'  // should be 'ams', 'none', or 'all'
    }
  };
</script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js"></script>