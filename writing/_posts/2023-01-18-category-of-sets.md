---
layout: post
title: Category of sets
---

A category $$\mathbf{C}$$ comprises the following data:[^1] [^2]

[^1]: [*Category Theory: a concise course.* 2. Basic Definitions \| Charlotte Aten, Venanzio Capretta, and William DeMeo](https://categorytheory.gitlab.io/basic_definitions.html)

[^2]: [category in nLab](https://ncatlab.org/nlab/show/category)

1. a class of **objects** $$X,Y,Z,\ldots$$, denoted $$\mathbf{C}_{\textrm{obj}}$$
2. for all objects $$X$$ and $$Y$$, a class of **morphisms with domain** $$X$$ **and codomain** $$Y$$, denoted $$\textrm{hom}(X,Y)$$
3. for all objects $$X$$, $$Y$$ and $$Z$$ and morphsisms $$f \in \textrm{hom}(X,Y)$$
and $$g \in \textrm{hom}(Y,Z)$$, there is a distinguished morphism $$g \circ f$$ with domain $$A$$ and
codomain $$C$$, called the **composition of** $$f$$ **and** $$g$$.
4. for any morphisms  $$f$$ and $$g$$ with $$\textrm{cod}(f)=\textrm{dom}(g)$$, there is a distinguished morphism denoted $$g \circ f$$ with $$\textrm{dom}(g\circ f)=\textrm{dom}(f)$$ and $$\textrm{cod}(g\circ f)=\textrm{cod}(g)$$, called the **composition of the morphisms** $$f$$ **and** $$g$$
5. for each object $$A$$ there is a distinguished morphism denoted $$1_A$$ with $$\textrm{dom}(1_A)=A$$ and $$\textrm{cod}(1_A)=A$$, called the **identity morphism**
6. for any $$f,g,h$$ are morphisms, if $$\textrm{cod}(f)=\textrm{dom}(g)$$ and $$\textrm{cod}(g)=\textrm{dom}(h)$$ then 

  $$h \circ (g \circ f) = (h \circ g) \circ f$$

7. for each morphism $$f$$, $$f \circ 1_{\textrm{dom}(f)} = f$$ (**unit law**)
8. for each morphism $$f$$, $$1_{\textrm{cod}(f)} \circ f = f$$ (**associative law**)

For any objects $$A$$ and $$B$$, define $$\textrm{hom}(A,B)$$ to be the class
of morphsisms with domain $$A$$ and codomain $$B$$. When for any objects $$A$$ and $$B$$ the class
$$\textrm{hom}(A,B)$$ is a set, the category $$\mathbf{C}$$ is called **locally small**.

Define $$\mathbf{Set}$$ as having objects sets and morphisms functions.

