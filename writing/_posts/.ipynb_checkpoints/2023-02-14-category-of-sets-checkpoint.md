---
layout: post
title: The category of sets
---

Paul R. Halmos. *Naive Set Theory*. Van Nostrand Reinhold Company. 1960.

# Section 1, "The Axiom of Extension" {#section1}

p. 2:

> **Axiom of extension.** Two sets are equal if and only if they have the same elements.

# Section 2, "The Axiom of Specification" {#section2}

p. 6:

> **Axiom of specification.** To every set $$A$$ and to every condition $$S(x)$$
> there corresponds a set $$B$$ whose elements are exactly those elements $$x$$ of
> $$A$$ for which $$S(x)$$ holds.
>
> A "condition" here is just a sentence. The symbolism is intended to 
> indicate that the letter $$x$$ is *free* in the sentence $$S(x)$$; that means that $$x$$ occurs in
> $$S(x)$$ at least once without being introduced by one of the phrases
> "for some $$x$$" or "for all $$x$$." It is an immediate consequence of the axiom of extension
> that the axiom of specification determines the set $$B$$ uniquely. To indicate
> the way $$B$$ is obtained from $$A$$ and from $$S(x)$$ it is customary to write
>
> $$B = \{x \in A : S(x) \}.$$

In other words, in the above $$S(x)$$ is a **predicate**.

# Section 3, "Unordered Pairs" {#section3}

p. 9:

> **Axiom of pairing.** For any two sets there exists a set that they both belong to.

p. 10:

> If a is a set, we may form the unordered pair $$\{a, a\}$$. That unordered pair is
> denoted by $$\{a\}$$ and is called the *singleton* of $$a$$; it is uniquely characterized by
> the statement that it has $$a$$ as its only element. Thus, for instance, $$\emptyset$$ and $$\{\emptyset\}$$
> are very different sets; the former has no elements, whereas the latter has
> the unique element $$\emptyset$$. To say that $$a \in A$$ is equivalent to saying that $$\{a\} \subset A$$.

# Section 4, "Unions and Intersections" {#section4}

p. 12:

> **Axiom of unions.** For every collection of sets there exists a set that contains
> all the elements that belong to at least one set of the given collection.

# Section 5, "Complements and Powers" {#section5}

p. 19:

> **Axiom of powers.** For each set there exists a collection of sets that contains
> among its elements all the subsets of the given set.

For a set $$A$$, denote by $$\mathscr{P}(A)$$ the **power set of** $$A$$, the set whose elements are
the subsets of $$A$$.

# Section 6, "Ordered Pairs" {#section6}

p. 23:

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

pp. 23-24:

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

p. 25:

> The charge of artificiality is true, but it is not too high a price to pay for conceptual economy. The concept of an ordered pair could have been introduced as an
> additional primitive, axiomatically endowed with just the right properties, no more
> and no less. In some theories this is done. The mathematician’s choice is between
> having to remember a few more axioms and having to forget a few accidental facts;
> the choice is pretty clearly a matter of taste. Similar choices occur frequently in
> mathematics; in this book, for instance, we shall encounter them again in connection with the definitions of numbers of various kinds.

p. 25:

> *Exercise.* If either $$A=\emptyset$$ or $$B=\emptyset$$, then
> $$A \times B = \emptyset$$, and conversely. If $$A \subset X$$ and
> $$B \subset Y$$, then $$A \times B \subset X \times Y$$, and (provided
> $$A \times B \neq \emptyset$$) conversely.

# Section 7, "Relations" {#section7}

pp. 26-27:

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

p.27:

> In the preceding section we saw that associated with every set $$R$$ of ordered pairs
> there are two sets called the projections of $$R$$ onto the first and second coordinates.
> In the theory of relations these sets are known as the *domain* and the *range* of $$R$$
> (abbreviated dom $$R$$ and ran $$R$$); we recall that they are defined by
>
> $$\textrm{dom} R = \{x :  \textrm{for some} \; y \; (x R y)\}$$
>
> and
>
> $$\textrm{ran} R = \{y: \textrm{for some} \; x \; (x R y)\}.$$

p. 27:

> If $$R$$ is a relation included in a Cartesian product $$X \times Y$$
> (so that $$\textrm{dom} R \subset X$$ and $$\textrm{ran} R \subset Y$$),
> it is sometimes convenient to say that $$R$$ is a relation *from* $$X$$ *to* $$Y$$;
> instead of a relation from $$X$$ to $$X$$ we may speak of a relation *in* $$X$$.

# Section 8, "Functions" {#section8}

p. 30:

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

p. 33:

> *Exercise.* (i) $$Y^\emptyset$$ has exactly one element, namely $$\emptyset$$,
> whether $$Y$$ is empty or not, and (ii) if $$X$$ is not empty, then $$\emptyset^X$$
> is empty.

# Section 10, "Inverses and Composites" {#section10}

pp. 38-39:

> A correspondence between the elements of $$X$$ and the elements of $$Y$$
> does always induce a well-behaved correspondence between the subsets of
> $$X$$ and the subsets of $$Y$$, not forward, by the formation of images, but
> backward, by the formation of inverse images. Given a function $$f$$ from
> $$X$$ to $$Y$$, let $$f^{-1}$$, the *inverse* of $$f$$, be the function from
> $$\mathscr{P}(Y)$$ to $$\mathscr{P}(X)$$ such
> that if $$B \subset Y$$, then
>
> $$f^{-1}(B) = \{x \in X: f(x) \in B\}.$$
>
> In words: $$f^{-1}(B)$$ consists of exactly those elements of X that $$f$$ maps into $$Y$$;
> the set $$f^{-1}(B)$$ is called the *inverse image* of $$B$$ under $$f$$.
> A necessary and sufficient condition that $$f$$ map X onto $$Y$$ is that the inverse image
> under $$f$$ of each non-empty subset of $$Y$$ be a non-empty subset of $$X$$. (Proof?)
> A necessary and sufficient condition that $$f$$ be one-to-one is that the inverse
> image under $$f$$ of each singleton in the range of $$f$$ be a singleton in $$X$$.
>
> If the last condition is satisfied, then the symbol $$f^{-1}$$ is frequently 
> assigned a second interpretation, namely as the function whose domain is
> the range of $$f$$, and whose value for each $$y$$ in the range of $$f$$ is the unique
> $$x$$ in $$X$$ for which $$f(x) = y$$. In other words, for one-to-one functions $$f$$ we may write
> $$f^{-1}(y)=x$$ if and only if $$f(x) = y$$. This use of the notation is
> mildly inconsistent with our first interpretation of $$f^{-1}$$, but the double
> meaning is not likely to lead to any confusion.

pp. 39-40:

> The discussion of inverses shows that what a function does can in a certain sense be undone;
> the next thing we shall see is that what two functions
> do can sometimes be done in one step. If, to be explicit, $$f$$ is a function
> from $$X$$ to $$Y$$ and $$g$$ is a function from $$Y$$ to $$Z$$, then every element in the
> range of $$f$$ belongs to the domain of $$g$$, and, consequently, $$g(f(x))$$ makes
> sense for each $$x$$ in $$X$$. The function $$h$$ from $$X$$ to $$Z$$, defined by
> $$h(x) = g(f(x))$$ is called the *composite* of the functions $$f$$ and $$g$$; it is denoted by
> $$g \circ f$$ or, more simply, by $$gf$$. (Since we shall not have occasion to consider
> any other kind of multiplication for functions, in this book we shall use
> the latter, simpler notation only.)
>
> Observe that the order of events is important in the theory of functional
> composition. In order that $$gf$$ be defined, the range of $$f$$ must be included
> in the domain of $$g$$, and this can happen without it necessarily happening
> in the other direction at the same time. Even if both $$fg$$ and $$gf$$ are defined,
> which happens if, for instance, $$f$$ maps $$X$$ into $$Y$$ and $$g$$ maps $$Y$$ into $$X$$, the
> functions $$fg$$ and $$gf$$ need not be the same; in other words, functional 
> composition is not necessarily commutative.
>
> Functional composition may not be commutative, but it is always
> associative. If $$f$$ maps $$X$$ into $$Y$$, if $$g$$ maps $$Y$$ into $$Z$$, and if
> $$h$$ maps $$Z$$ into $$U$$, then we can form the composite of $$h$$ with $$gf$$
> and the composite of $$hg$$ with $$f$$; it is a simple exercise to show that the result is the same in either case.
>
> The connection between inversion and composition is important; 
> something like it crops up all over mathematics. If $$f$$ maps $$X$$ into $$Y$$
> and $$g$$ maps $$Y$$ into $$Z$$, then $$f^{-1}$$ maps $$\mathscr{P}(Y)$$ into $$\mathscr{P}(X)$$
> and $$g^{-1}$$ maps $$\mathscr{P}(Z)$$ into $$\mathscr{P}(Y)$$. In this situation, the composites that
> are formable are $$gf$$ and $$f^{-1}g^{-1}$$; the assertion is that the latter is the inverse of the former.
> Proof: if $$x \in (gf)^{-1}(C)$$, where $$x \in X$$ and $$C \subset Z$$, then
> $$g(f(x)) \in C$$, so that $$f(x) \in g^{-1}(C)$$, and therefore
> $$x \in f^{-1}(g^{-1}(C))$$; the steps of the argument are reversible.

# Categories {#categories}

A category **C** comprises the following data: [^1] [^2]

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

1. For each morphism $$f$$, it holds that $$f \circ \textrm{id}_{\textrm{dom}(f)} = f$$, called the **right identity law**. [^4]

2. For each morphism $$f$$, it holds that $$\textrm{id}_{\textrm{cod}(f)} \circ f = f$$, called the **left identity law**.

3. For each triple of morphisms $$f,g,h$$, if
$$\textrm{cod}(f)=\textrm{dom}(g)$$ and $$\textrm{cod}(g)=\textrm{dom}(h)$$ then  
$$
h \circ (g \circ f) = (h \circ g) \circ f,
$$
called the **associative law**. [^5]

[^4]: [identity element in nLab](https://ncatlab.org/nlab/show/identity+element)

[^5]: [associativity in nLab](https://ncatlab.org/nlab/show/associativity)

# The category structure of **Set**

$$\textrm{Obj}(\mathbf{Set})$$ is the class of sets.

For each pair of sets $$X,Y$$, the class of morphisms
$$\textrm{hom}_{\mathbf{Set}}(X,Y)$$ is the set of functions $$Y^X$$. [^small]

[Halmos, Section 8, "Functions"](#section8):

> $$Y^\emptyset$$ has exactly one element, namely $$\emptyset$$,
> whether $$Y$$ is empty or not, and (ii) if $$X$$ is not empty, then $$\emptyset^X$$
> is empty.

For each triple of objects $$X,Y,Z$$, the composition

$$\circ_{X,Y,Z}:Y^X \times Z^Z \to Z^X$$

## $$X \neq \emptyset, Y \neq \emptyset, Z \neq \emptyset$$

$$
\circ_{X,Y,Z}(f,g)(x) = g(f(x)),\quad f \in Y^X, g \in Z^Y, \quad x \in X.
$$

## $$X = \emptyset, Y \neq \emptyset, Z \neq \emptyset$$

$$Y^X=\{\emptyset\}$$

$$
\circ_{X,Y,Z}(\emptyset,g) = \emptyset, \quad g \in Z^Y.
$$

## $$X \neq \emptyset, Y = \emptyset, Z \neq \emptyset$$

## $$X \neq \emptyset, Y \neq \emptyset, Z = \emptyset$$

## $$X = \emptyset, Y = \emptyset, Z \neq \emptyset$$

## $$X = \emptyset, Y \neq \emptyset, Z = \emptyset$$

## $$X \neq \emptyset, Y = \emptyset, Z = \emptyset$$

## $$X = \emptyset, Y = \emptyset, Z = \emptyset$$

For each set $$X$$ that is not empty, the identity morphism $$\textrm{id}_X \in X^X$$ is

$$
\textrm{id}_X(x) = x, \quad x \in X.
$$

When $$X$$ is empty,

$$
\id_\emptyset = \emptyset \in \emptyset^\emptyset.
$$



[^small]: When for each pair of objects $$X,Y$$ it holds that the class of morphisms $$\textrm{hom}_{\mathbf{C}}(X,Y)$$ is a **set**, the category **C** is called **locally small**. See [locally small category in nLab](https://ncatlab.org/nlab/show/locally+small+category)
    
    When the class of objects and the class of morphisms are both sets, the category is called **small**. For doing algebraic geometry my impression is that there one works with small categories. See [The Stacks project](https://stacks.math.columbia.edu/)