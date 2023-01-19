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
> However convincing the motivation of this definition may be, we must still prove
> that the result has the main property that an ordered pair must have to deserve its
> name. We must show that if $$(a, b)$$ and $$(x, y)$$ are ordered pairs and if
> $$(a,b)=(x,y)$$, 
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

Paul R. Halmos. *Naive Set Theory*. Van Nostrand Reinhold Company. 1960. Section 5. "Complements and Powers." p. 19:

> **Axiom of powers.** For each set there exists a collection of sets that contains
> among its elements all the subsets of the given set.

For a set $$A$$, denote by $$\mathscr{P}(A)$$ the **power set of** $$A$$, the set whose elements are
the subsets of $$A$$.

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
> $$A \times B = \{x : x=(a,b) \; \textrm{for some} \; a \; \textrm{in} \; A \; \textrm{and for some} \; b \; \textrm{in} \; B\}.$$

Paul R. Halmos. *Naive Set Theory*. Van Nostrand Reinhold Company. 1960. Section 6. "Ordered Pairs." p. 20:

> The charge of artificiality is true, but it is not too high a price to pay for conceptual economy. The concept of an ordered pair could have been introduced as an
> additional primitive, axiomatically endowed with just the right properties, no more
> and no less. In some theories this is done. The mathematician’s choice is between
> having to remember a few more axioms and having to forget a few accidental facts;
> the choice is pretty clearly a matter of taste. Similar choices occur frequently in
> mathematics; in this book, for instance, we shall encounter them again in connection with the definitions of numbers of various kinds.

If either $$A$$ or $$B$$ is an empty set, then it follows that the Cartesian product $$A \times B$$ is an
empty set.

# Relations

Paul R. Halmos. *Naive Set Theory*. Van Nostrand Reinhold Company. 1960. Section 7. "Relations." p. 22:

> We may not know what a relation is, but we do know what a set is, and the
> preceding considerations establish a close connection between relations and sets.
> The precise set-theoretic treatment of relations takes advantage of that heuristic
> connection; the simplest thing to do is to define a relation to be the corresponding
> set. This is what we do; we hereby define a *relation* as a set of ordered pairs.
> Explicitly: a set $$R$$ is a relation if each element of $$R$$ is an ordered pair; this means, of course, that if
> $$z \in R$$, then there exist $$x$$ and $$y$$ so that $$z=(x,y)$$. If $$R$$ is a relation, it is sometimes
> convenient to express the fact that $$(x,y) \in R$$ by writing
>
> $$xRy$$
>
> and saying, as in everyday language, that $$x$$ stands in the relation $$R$$ to $$y$$.

Paul R. Halmos. *Naive Set Theory*. Van Nostrand Reinhold Company. 1960. Section 7. "Relations." p. 23:

> In the preceding section we saw that associated with every set $$R$$ of ordered pairs
> there are two sets called the projections of $$R$$ onto the first and second coordinates.
> In the theory of relations these sets are known as the domain and the range of $$R$$
> (abbreviated dom $$R$$ and ran $$R$$); we recall that they are defined by
>
> $$\textrm{dom} R = \{x :  \textrm{for some} \; y \; (x R y)\}$$
>
> and
>
> $$\textrm{ran} R = \{y: \textrm{for some} \; x \; (x R y)\}.$$

Paul R. Halmos. *Naive Set Theory*. Van Nostrand Reinhold Company. 1960. Section 7. "Relations." p. 23:

> If $$R$$ is a relation included in a Cartesian product $$X \times Y$$
> (so that $$\textrm{dom} R \subset X$$ and $$\textrm{ran} R \subset Y$$),
> it is sometimes convenient to say that $$R$$ is a relation *from* $$X$$ *to* $$Y$$;
> instead of a relation from $$X$$ to $$X$$ we may speak of a relation *in* $$X$$.

# Functions

Paul R. Halmos. *Naive Set Theory*. Van Nostrand Reinhold Company. 1960. Section 8. "Functions." p. 25:

> If $$X$$ and $$Y$$ are sets, a *function from* (or *on*) $$X$$ *to* (or *into*) $$Y$$ is a relation $$f$$ such
> that $$\textrm{dom} f = X$$ and such that for each $$x$$ in $$X$$ there is a unique element $$y$$ in $$Y$$ with
> $$(x,y) \in f$$. The uniqueness condition can be formulated explicitly as follows:
> if $$(x,y) \in f$$ and $$(x,z) \in f$$, then $$y=z$$. For each $$x$$ in $$X$$, the unique $$y$$ in $$Y$$ such that
> $$(x,y) \in f$$ is denoted by $$f(x)$$. For functions this notation and its minor variants supersede
> the others used for more general relations; from now on, if $$f$$ is a function, we shall write $$f(x)=y$$
> instead of $$(x,y) \in f$$ or $$x f y$$. The element $$y$$ is called the *value* that the function *sends* or
> *maps* or *transforms* $$x$$ onto $$y$$. The words *map* or *mapping*, *transformation*, *correspondence*,
> and *operator* are among some of the many that are sometimes used as synonyms for *function*. The symbol
>
> $$f:X \to Y$$
>
> is sometimes used as an abbreviation for "$$f$$ is a function from $$X$$ to $$Y$$."
> The set of all functions from $$X$$ to $$Y$$ is a subset of the power set
> $$\mathscr{P}(X \times Y)$$; it will be denoted by $$Y^X$$.


Paul R. Halmos. *Naive Set Theory*. Van Nostrand Reinhold Company. 1960. Section 8. "Functions." p. 27:

> *Exercise.* (i) $$Y^\emptyset$$ has exactly one element, namely $$\emptyset$$,
> whether $$Y$$ is empty or not, and (ii) if $$X$$ is not empty, then $$\emptyset^X$$
> is empty.


# **Sets** is a category

Let $$\textrm{Obj}(\mathbf{Sets})$$ be the class of sets.

$$\mathbf{Sets}$$ is a category.