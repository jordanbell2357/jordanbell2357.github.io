---
layout: post
title: Formal languages
---

[formal grammar in nLab](https://ncatlab.org/nlab/show/formal+grammar)

[Introduction to Language Theory \| Ray Toal, Loyola Marymount University](https://cs.lmu.edu/~ray/notes/languagetheory/)

[Formal languages and automata. *Encyclopedia of Mathematics*](https://encyclopediaofmath.org/wiki/Formal_languages_and_automata)

<https://opendsa-server.cs.vt.edu/OpenDSA/Books/PIFLAS22/html/index.html>

# Languages over an alphabet 

References: [^language] [^Toal]

[^language]: [Formal languages and automata. *Encyclopedia of Mathematics*](https://encyclopediaofmath.org/wiki/Formal_languages_and_automata)

[^Toal]: [Introduction to Language Theory \| Ray Toal, Loyola Marymount University](https://cs.lmu.edu/~ray/notes/languagetheory/)

The empty set $\emptyset$ is an **initial object** in the category of sets **Set**:
for any set $Y$ there is a unique function $\emptyset_Y:\emptyset \to Y$. [^empty]

[^empty]: [empty function in nLab](https://ncatlab.org/nlab/show/empty+function)

For sets $X$ and $Y$, let

```math
\mathrm{hom}_{\mathbf{Set}}(X,Y)=Y^X
```

be the set of functions with domain $X$ and image contained in $Y$.
In particular, $Y^\emptyset = \{\emptyset_Y\}$.

Let $\mathbb{N}=\{0,1,2,\ldots\}$. For $n \in \mathbb{N}$, define

$[n] = \{i \in \mathbb{N} : i < n\}.$

Thus, $[0]=\{\}=\emptyset$, $[1]=\{0\}$, $[2]=\{0,1\}$, $[3]=\{0,1,2\}$, etc.

For $m,n \in \mathbb{N}$, define

$[m,n] = \{i \in \mathbb{N}: m \leq i < n\}.$

If $m \geq n$, then $[m,n]=\emptyset$.

Let $A$ be a finite set that we shall call **an alphabet**.

Write $\epsilon_A=\emptyset_A$, the unique function
$\emptyset \to A$. Thus $A^\emptyset = \{\epsilon_A\}$.

A **word over the alphabet** $A$ **of length** $n$, $n \in \mathbb{N}$, is an element
of $A^{[n]}$. [^monoid]

[^monoid]: [free monoid in nLab](https://ncatlab.org/nlab/show/free+monoid)

A word over $A$ of length 0 is an element of $A^{[0]}$, and

$A^{[0]} = A^\emptyset = \{\epsilon_A\},$

so the unique word over $A$ of length 0 is $\epsilon_A$.
We call $\epsilon_A$ the **empty word** over the alphabet $A$.

If $N$ is an empty set, then as we have stated above, $\emptyset^N = \{\emptyset\}$.
If $N$ is a nonempty set, then $\emptyset^N = \emptyset$. Thus, if the alphabet $A$ is empty, then
$A^{[n]}=\emptyset$ for $n > 0$.

If $x \in A^{[m]}$ and $y \in A^{[n]}$, define the **concatenation** $x*y \in A^{[m+n]}$ by

```math
(x*y)(i) = \begin{cases}
x(i)&i \in [m]\\
y(i-m)&i \in [m,m+n]
\end{cases},
\quad i \in [m+n].
```

## Free monoid on a set

Define

```math
A^* = \bigcup_{n \in \mathbb{N}} A^{[n]}.
```

The sets in this union are pairwise disjoint; this is true whether or not the alphabet $A$ is empty,
for different reasons.
If the alphabet $A$ is empty,
then $A^{[0]}=\{\epsilon_A\}$, and $A^{[n]}=\emptyset$ for $n>0$; and in this case
the sets are indeed pairwise disjoint. If the alphabet $A$ is nonempty, then
a word of some length is not a word of any other length, so in this case the sets are
pairwise disjoint.

$(A^*,*,\epsilon_A)$ is the **free monoid on** $A$. [^monoid] ($A^*$ is also called the **Kleene star of** $A$.[^Kleene])

[^Kleene]: [Kleene star \| Wikipedia](https://en.wikipedia.org/wiki/Kleene_star)

[^DM4CS]: [Discrete Mathematics for Computer Science \| OpenDSA Project](https://icsatkcc.github.io/Discrete-Math-for-Computer-Science/s-Monoids.html)

For $x \in A^*$, define $\mathrm{len}(x)$ to be the unique $n \in \mathbb{N}$ such that $x \in A^{[n]}$,
the **length** of a word. [^list]

[^list]: [list in nLab](https://ncatlab.org/nlab/show/list)

If $A$ is an empty set, then $A^*=\{\epsilon_A\}$.

If $A$ is a set with one element, say $A=\{a\}$, then for each $n>0$, the unique
function $[n] \to A$ is $i \mapsto a$ for $i \in [n]$. Thus when $A=\{a\}$,
it is the case that for $n>0$ the set $A^{[n]}$ has exactly one element, function

$i \mapsto a, \quad i \in [n],$

that is, the unique word of length $n$ over $A=\{a\}$,

$\underbrace{a \cdots a}_{n}.$

If $A=\{a\}$ then $x \mapsto \mathrm{len}(x)$ is an isomorphism of monoids
$A^* \to \mathbb{N}$.

A **language over the alphabet** $A$ is any subset of $A^*$,
the free monoid on $A$.

## Free semigroup on a set

Define

$A^+ = \bigcup_{n \in \mathbb{N} \setminus\{0\}} A^{[n]}.$

$(A^+,*)$ is the **free semigroup on** $A$. [^semigroup]

$A^+ = A^* \setminus \{\epsilon_A\}.$

[^semigroup]: [Free semi-group. *Encyclopedia of Mathematics*](https://encyclopediaofmath.org/wiki/Free_semi-group)

# Operations on languages 

We remind ourselves that a language over an alphabet $A$ is any subset of the free monoid $A^*$. In other words,
the power set $\mathscr{P}(A^*)$ is the set of all languages over an alphabet $A$.

**Union.** For $L_1, L_2 \subset A^*$, the union $L_1 \cup L_2 \subset A^*$.

**Concatenation.** For $L_1, L_2 \subset A^*$,

$L_1 L_2 = \{x*y : x \in L_1, y \in L_2\} \subset A^*.$

**Kleene star.** For $L \subset A^*$, the Kleene star of $L$ is [^Kleene]

```math
L^* = \bigcup_{n \in \mathbb{N}} L^{[n]} \subset A^*.
```

# Free group on a set

## Words over a set

Let $X$ be a set.

If $X \neq \emptyset$, for $x \in X$ define $I(x)=x$.

Let $Y$ be a set disjoint from $X$ for which there is a bijection $J:X \to Y$.

For $x \in X$, write $x^{-1} = J(x)$.

Let

$$
\begin{align*}
A &= X \cup Y\\
&= \left( \bigcup_{x \in X} \lbrace I(x) \rbrace \right) \cup \left( \bigcup_{x \in X} \lbrace J(x) \rbrace \right)\\
&= \bigcup_{x \in X} \lbrace I(x), J(x) \rbrace,
\end{align*}
$$

elements of which we call **characters**.

The **Kleene star** of $A$ is

$$
A^* = \bigcup_{n \geq 0} A^n.
$$

Elements of $W(X)=A^*$ are called **words over the set** $X$.

$$
A^0 = \lbrace \epsilon \rbrace
$$

We call $\epsilon$ the **empty word**. [^1]

[^1]: <https://arbital.com/p/5zr/empty_set_universal_property/>

For $n \geq 1$ and for  $a \in A^n$, we have

$$
a = a_1 \cdots a_n, \qquad a_i \in A, 1 \leq i \leq n.
$$

## Reduction

If $a_i a_{i+1} = I(x)J(x)$ for some $x \in X$
or $a_i a_{i+1} = J(x)I(x)$ for some $x \in X$,
we call

$$
a_1 \cdots a_i a_{i+1} \cdots a_n \longrightarrow a_1 \cdots a_{i-1} \epsilon a_{i+2} \cdots a_n 
$$

a **reduction**.

If a word $a$ has no reductions, it is called a **reduced word**. [^2]

[^2]: <https://arbital.com/p/freely_reduced_word/>

Let $W_R(X)$ be the set of reduced words over $X$.

## Symmetric group on a set
Let $S(X)$ be the set of bijections $X \to X$.

### $X = \emptyset$

$$S(\emptyset) = \lbrace \emptyset \rbrace$$

[^5]

[^5]: <https://arbital.com/p/empty_set_universal_property/>

### $X \neq \emptyset$

For $\sigma, \tau \in S(X)$, define

$$
(\sigma \tau)(x) = (\sigma \circ \tau)(x) = \sigma(\tau(x)),\qquad x \in X.
$$

$\mathrm{id}_X(x)=x$ is the identity element of $S(X)$.

We call $S(X)$ the **symmetric group on the set** $X$.

## Free group on a set



[^3]

[^3]: [Formal definition of the free group \| Arbital](https://arbital.com/p/free_group/?l=5s1)



## Universal property


[^4]

[^4]: [Free group universal property \| Arbital](https://arbital.com/p/free_group/?l=6gd)


