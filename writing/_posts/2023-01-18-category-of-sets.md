---
layout: post
title: The category of sets
---

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
\begin{equation}
h \circ (g \circ f) = (h \circ g) \circ f
\end{equation}
$$
called the **associative law**.

When for each pair of objects $$X,Y$$ it holds that the class of morphisms $$\textrm{hom}_{\mathbf{C}}(X,Y)$$
is a **set**, the category is called **locally small**. [^4] [^5]

[^4]: [locally small category in nLab](https://ncatlab.org/nlab/show/locally+small+category)

[^5]: When the class of objects and the class of morphisms are both sets, the category is called **small**.
For doing algebraic geometry my impression is that one works with small categories. See [The Stacks project](https://stacks.math.columbia.edu/)