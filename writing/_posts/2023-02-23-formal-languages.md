---
layout: post
title: Formal languages
---

# Formal languages

The empty set $$\emptyset$$ is an **initial object** in the category of sets **Set**:
for any set $$Y$$ there is a unique function $$\emptyset_Y:\emptyset \to Y$$. [^1]

[^1]: [empty function in nLab](https://ncatlab.org/nlab/show/empty+function)

For sets $$X$$ and $$Y$$, let

$$\mathrm{hom}_{\mathbf{Set}}(X,Y)=Y^X$$

be the set of functions with domain $$X$$ and image contained in $$Y$$.
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

If $$N$$ is an empty set, then as we have stated above, $$\emptyset^N = \{\emptyset\}$$.
If $$N$$ is a nonempty set, then $$\emptyset^N = \emptyset$$. Thus, if the alphabet $$A$$ is empty, then
$$A^{[n]}=\emptyset$$ for $$n > 0$$.

If $$x \in A^{[m}]$$ and $$y \in A^{[n]}$$, define the **concatenation** $$x*y \in A^{[m+n]}$$ by

$$(x*y)(i) = \begin{cases}
x(i)&i \in [m]\\
y(i-m)&i \in [m,m+n]
\end{cases},
\quad i \in [m+n].$$

Define

$$A^* = \bigcup_{n \in \mathbb{N}} A^{[n]}.$$

The sets in this union are pairwise disjoint; this is true whether or not the alphabet $$A$$ is empty,
according to separate reasons.
If the alphabet $$A$$ is empty,
then $$A^{[0]}=\{\epsilon_A\}$$, and $$A^{[n]}=\emptyset$$ for $$n>0$$; and in this case
the sets are indeed pairwise disjoint. If the alphabet $$A$$ is nonempty, then
a word of some length is not a word of any other length, so in this case the sets are
pairwise disjoint.

$$(A^*,*,\epsilon_A)$$ is the **free monoid on** $$A$$. [^2] (This is also called the **Kleene star of** $$A$$. [^Kleene])

[^Kleene]: [Kleene star \| Wikipedia](https://en.wikipedia.org/wiki/Kleene_star)

For $$x \in A^*$$, define $$\mathrm{len}(x)$$ to be the unique $$n \in \mathbb{N}$$ such that $$x \in A^{[n]}$$,
the **length** of a word. [^3]

[^3]: [list in nLab](https://ncatlab.org/nlab/show/list)

If $$A$$ is an empty set, then $$A^*=\{\epsilon_A\}$$.

If $$A$$ is a set with one element, say $$A=\{a\}$$, then for each $$n>0$$, the unique
function $$[n] \to A$$ is $$i \mapsto a$$ for $$i \in [n]$$. Thus when $$A=\{a\}$$,
it is the case that for $$n>0$$ the set $$A^{[n]}$$ has exactly one element, function

$$i \mapsto a, \quad i \in [n],$$

that is, the unique word of length $$n$$ over $$A=\{a\}$$,

$$\underbrace{a \cdots a}_{n}.$$

If $$A=\{a\}$$ then $$x \mapsto \mathrm{len}(x)$$ is an isomorphism of monoids
$$A^* \to \mathbb{N}$$.

A **language over the alphabet** $$A$$ is any subset of $$A^*$$,
the free monoid on $$A$$. [^4]

[^4]: [Formal languages and automata. *Encyclopedia of Mathematics*](https://encyclopediaofmath.org/wiki/Formal_languages_and_automata)

# Operations on languages

**Union.** For $$L_1, L_2 \subset A^*$$, the union $$L_1 \cup L_2 \subset A^*$$.

**Concatenation.** For $$L_1, L_2 \subset A^*$$,

$$L_1 * L_2 = \{x*y : x \in L_1, y \in L_2\} \subset A^*.$$

**Kleene star.** For $$L \subset A^*$$, the Kleene star of $$L$$ is

$$L^* = \bigcup_{n \in \mathbb{N}} L^{[n]} \subset A^*.$$


---

<https://cs.lmu.edu/~ray/notes/languagetheory/>


<https://opendsa-server.cs.vt.edu/OpenDSA/Books/PIFLAS22/html/index.html>


<https://icsatkcc.github.io/Discrete-Math-for-Computer-Science/s-free-monoids-and-languages.html>
