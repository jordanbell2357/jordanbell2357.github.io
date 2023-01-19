---
layout: post
title: The category of sets
---

# Categories

A category $$\mathbf{C}$$ comprises the following data: [^1] [^2]

[^1]: [category in nLab](https://ncatlab.org/nlab/show/category)

[^2]: [4.2 Definitions \| The Stacks project](https://stacks.math.columbia.edu/tag/0013)

1. A class of **objects** $$\textrm{Obj}(\mathbf{C})$$.

2. For each pair of objects $$X,Y$$, a class of **morphisms** $$\textrm{hom}_{\mathbf{C}}(X,Y)$$. A morphism $$f \in \textrm{hom}_{\mathbf{C}}(X,Y)$$ has **domain** $$\textrm{dom}(f)=X$$ and **codomain** $$\textrm{cod}(f)=Y$$.

3. For each triple of objects $$X,Y,Z$$, a map
$$
\begin{equation}
\circ_{X,Y,Z}:\textrm{hom}_{\mathbf{C}}(X,Y) \times \textrm{hom}_{\mathbf{C}}(Y,Z) \to \textrm{hom}_{\mathbf{C}}(X,Z)
\end{equation}
$$
called **composition** and denoted by $$\circ_{X,Y,Z}:(f,g) \mapsto g \circ f$$. [^3]

4. For each object $$X$$, a morphism $$\textrm{id}_X \in \textrm{hom}_{\mathbf{C}}(X,X)$$, called the **identity morphism**.

[^3]: [composition in nLab](https://ncatlab.org/nlab/show/composition)

The data has to satisfy the following rules:

1. For each morphism $$f$$, it holds that $$f \circ \textrm{id}_{\textrm{dom}(f)} = f$$, called the **right identity law**.

2. For each morphism $$f$$, it holds that $$\textrm{id}_{\textrm{cod}(f)} \circ f = f$$, called the **left identity law**.

3. For each triple of morphisms $$f,g,h$$, if $$\textrm{cod}(f)=\textrm{dom}(g)$$ and $$\textrm{cod}(g)=\textrm{dom}(h)$$ then

$$
h \circ (g \circ f) = (h \circ g) \circ f
$$

called the **associative law**.

When for each pair of objects $$X,Y$$ it holds that the class of morphisms $$\textrm{hom}_{\mathbf{C}}(X,Y)$$
is a **set**, the category is called **locally small**. [^4] [^5]

[^4]: [locally small category in nLab](https://ncatlab.org/nlab/show/locally+small+category)

[^5]: When the class of objects and the class of morphisms are both sets, the category is called **small**. For doing algebraic geometry my impression is that one works with small categories. See [The Stacks project](https://stacks.math.columbia.edu/)

# Ordered pairs

Paul R. Halmos. *Naive Set Theory*. Van Nostrand Reinhold Company. 1960. Section 6. "Ordered Pairs." p. 19:

> The *ordered pair* of $$a$$ and $$b$$, with *first coordinate* $$a$$ and *second coordinate* $$b$$, is the set 
> $$(a,b)$$ defined by
>
> $$(a,b) = \{\{a\},\{a,b\}\}.$$
>
> However convincing the motivation of this definition may be, we must 
> that the result has the main property that an ordered pair must have to deserve its
> name. We must show that if $$(a, b)$$ $$(x, y)$$ are ordered pairs and if
> $$(a,b)=(x,y)$$, then
> then $$a = x$$ and $$b = y$$. To prove this, we note first that if $$a$$ and $$b$$ happen to be equal,
> then the ordered pair $$(a,b)$$ is the same as the singleton $$\{\{a\}\}$$. If, conversely, $$(a, b)$$
> is a singleton, then $$\{a\}=\{a,b\}$$, so that $$b \in \{a\}$$, and therefore $$a=b$$. Suppose
> now that $$(a,b)=(x,y)$$. If $$a = b$$, then both $$(a, b)$$ and $$(x, y)$$ are singletons, so that
> $$x = y$$; since $$\{x\} \in (a,b)$$ and $$\{a\} \in (x,y)$$, it follows that
> $$a$$, $$b$$, $$x$$, and $$y$$ are all equal.
> If $$a \neq b$$, then both $$(a, b)$$ and $$(x, y)$$ contain exactly one singleton, namely $$\{a\}$$ and
> $$\{x\}$$ respectively, so that $$a = x$$. Since in this case it is also true that both $$(a, b)$$
> and $$(x, y)$$ contain exactly one unordered pair that is not a singleton,
> namely $$\{a, b\}$$
> and $$\{x, y\}$$ respectively, it follows that $$\{a,b\}=\{x,y\}$$, and therefore,
> in particular,
> $$b \in \{x,y\}$$. Since $$b$$ cannot be $$x$$ (for then we should have $$a = x$$
> and $$b = x$$, and,
> therefore, $$a = b$$), we must have $$b = y$$, and the proof is complete.

# Cartesian products

Paul R. Halmos. *Naive Set Theory*. Van Nostrand Reinhold Company. 1960. Section 6. "Ordered Pairs." p. 19:

> If $$A$$ and $$B$$ are sets, does there exist a set that contains all the ordered pairs $$(a,b)$$ with $$a$$ in
> $$A$$ and $$b$$ in $$B$$? It is quite easy to see that the
> answer is yes. Indeed, if $$a \in A$$ and $$b \in B$$, then $$\{a\} \subset A$$
> and $$\{b\} \subset B$$, and therefore $$\{a,b\} \subset A \cup B$$. Since also
> $$\{a\} \subset A \cup B$$, it follows that both $$\{a\}$$ and $$\{a,b\}$$ are
> elements of $$\mathscr{P}(A \cup B)$$. This implies that $$\{\{a\},\{a,b\}\}$$
> is a subset of $$\mathscr{P}(A \cup B)$$, and hence that it is an element of
> $$\mathscr{P}(\mathscr{P}(A \cup B))$$; in other words $$(a,b) \in \mathscr{P}(\mathscr{P}(A \cup B))$$
> whenever $$a \in A$$ and $$b \in B$$. Once this is known, it is a routine matter to apply the axiom of
> specification and the axiom of extension to produce the unique set $$A \times B$$ that consists exactly
> of the ordered pairs $$(a,b)$$ with $$a$$ in $$A$$ and $$b$$ in $$B$$. This set is called the
> *Cartesian product* of $$A$$ and $$B$$; it is characterized by the fact that
>
> $$A \times B = \{x : x=(a,b) \textrm{for some} \, a \, \textrm{in} \, A \, \textrm{and for some} \, b \, \textrm{in} \, B\}.$$

Define $$\pi_A(a,b) = a$$, the first coordinate, and $$\pi_B(a,b)=b$$, the second coordinate.

For a set $$A$$, denote by $$\mathscr{P}(A)$$ the **power set of** $$A$$, the set whose elements are
the subsets of $$A$$.


# 

# Relations

# Functions

# **Sets** is a category

Let $$\textrm{Obj}(\mathbf{Sets})$$ be the class of sets.

$$\mathbf{Sets}$$ is a category.