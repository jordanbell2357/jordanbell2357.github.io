---
layout: post
title: The category of sets
---

A category $$\mathbf{C}$$ comprises the following data:[^3] [^2]

[^3]: [4.2 Definitions \| The Stacks project](https://stacks.math.columbia.edu/tag/0013)

[^2]: [category in nLab](https://ncatlab.org/nlab/show/category)

1. A class of **objects** $$\textrm{Obj}(\mathbf{C})$$.

2. For each pair of objects $$X,Y$$, a class of **morphisms** $$\textrm{hom}_{\mathbf{C}}(X,Y)$$. A morphism $$f \in \textrm{hom}_{\mathbf{C}}(X,Y)$$ has **domain** $$\textrm{dom}(f)=X$$ and **codomain** $$\textrm{cod}(f)=Y$$.

3. For each triple of objects $$X,Y,Z$$, a map
$$
\begin{equation}
\textrm{hom}_{\mathbf{C}}(Y,Z) \times \textrm{hom}_{\mathbf{C}}(X,Y) \to \textrm{hom}_{\mathbf{C}}(X,Z)
\end{equation}
$$
called **composition** and denoted by $$(g,f) \mapsto g \circ f$$.

4. For each object $$X$$, a morphism in $$\textrm{hom}_{\mathbf{C}})(X,X)$$, denoted $$\textrm{id}_X$$, called the **identity morphism**.

The data has to satisfy the following rules:

1. For each morphism $$f$$, it holds that $$f \circ 1_{\textrm{dom}(f)} = f$$, called the **right unit law**
2. For each morphism $$f$$, it holds that $$1_{\textrm{cod}(f)} \circ f = f$$, called the **left unit law**
3. For each triple of morphisms $$f,g,h$$, if $$\textrm{cod}(f)=\textrm{dom}(g)$$ and $$\textrm{cod}(g)=\textrm{dom}(h)$$ then
$$
\begin{equation}
h \circ (g \circ f) = (h \circ g) \circ f
\end{equation}
$$
called the **associative law**.






[^1]



[^1]: [*Category Theory: a concise course.* 2. Basic Definitions \| Charlotte Aten, Venanzio Capretta, and William DeMeo](https://categorytheory.gitlab.io/basic_definitions.html)

