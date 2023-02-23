---
layout: post
title: Formal languages
---

The empty set $$\emptyset$$ is an **initial object** in the category of sets **Sets**:
for any set $$Y$$ there is a unique function $$\emptyset_Y:\emptyset \to Y$$. [^1]

[^1]: [empty function in nLab](https://ncatlab.org/nlab/show/empty+function)

For sets $$X$$ and $$Y$$, let $$Y^X$$ be the set of functions with domain $$X$$ and image contained in $$Y$$.
In particular, $$Y^\emptyset = \{\emptyset_Y\}$$.



Let $$\mathbb{N}=\{0,1,2,\ldots\}$$. For $$n \in \mathbb{N}$$, define

$$[n] = \{i \in \mathbb{N} : i < n\}.$$

Thus, $$[0]=\{\}=\emptyset$$, $$[1]=\{0\}$$, $$[2]=\{0,1\}$$, $$[3]=\{0,1,2\}$$, etc.

For $$m,n \in \mathbb{N}$$, define

$$[m,n] = \{i \in \mathbb{N}: m \leq i < n\}.$$

If $$m \geq n$$, then $$[m,n]=\emptyset$$.

Let $$A$$ be a finite set that we shall call **an alphabet**.

Write $$\epsilon_A=\emptyset_A$$, the unique function
$$\emptyset \to A$$. Thus $$A^\emptyset = \{\epsilon_A\}$$.

A **word over the alphabet** $$A$$ **of length** $$n$$, $$n \in \mathbb{N}$$, is an element
of $$A^{[n]}$$. [^2]

[^2]: [free monoid in nLab](https://ncatlab.org/nlab/show/free+monoid)

A word over $$A$$ of length 0 is an element of $$A^{[0]}$$, and

$$A^{[0]} = A^\emptyset = \{\epsilon_A\},$$

so the unique word over $$A$$ of length 0 is $$\epsilon_A$$.
We call $$\epsilon_A$$ the **empty word** over the alphabet $$A$$.

If $$x \in A^{[m}]$$ and $$y \in A^{[n]}$$, define the **composition** $$xy \in A^{[m+n]}$$ by

$$(xy)(i) = \begin{cases}
x(i)&i \in [m]\\
y(i-m)&i \in [m,m+n]
\end{cases},
\quad i \in [m+n]$$






<https://cs.lmu.edu/~ray/notes/languagetheory/>


<https://opendsa-server.cs.vt.edu/OpenDSA/Books/PIFLAS22/html/index.html>


<https://introcs.cs.princeton.edu/java/51language/>


<https://icsatkcc.github.io/Discrete-Math-for-Computer-Science/s-free-monoids-and-languages.html>
