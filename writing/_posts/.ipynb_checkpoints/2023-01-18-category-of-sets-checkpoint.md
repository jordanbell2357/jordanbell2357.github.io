---
layout: post
title: Category of sets
---

A category $$\mathbf{C}$$ is

1. a class of **objects** $$A,B,C,\ldots$$
2. a class of **morphisms** $$f,g,h,\ldots$$
3. for each morphism $$f$$, an object $$\textrm{dom}(f)$$ called the domain of $$f$$ and an object $$\textrm{cod}(f)$$ called the **codomain** of $f$$.
4. if $$f$$ and $$g$$ are morphisms and $$\textrm{cod}(f)=\textrm{dom}(g)$$, there is a distinguished morphism denoted $$g \circ f$$ with $$\textrm{dom}(g\circ f)=\textrm{dom}(f)$$ and $$\textrm{cod}(g\circ f)=\textrm{cod}(g)$$, called the **composition of the morphisms** $$f$$ **and** $$g$$
5. for each object $$A$$ there is a distinguished morphism denoted $$1_A$$ with $$\textrm{dom}(1_A)=A$$ and $$\textrm{cod}(1_A)=A$$, called the **identity morphism**
6. if $$f,g,h$$ are morphisms with $$\textrm{cod}(f)=\textrm{dom}(g)$$ and $$\textrm{cod}(g)=\textrm{dom}(h)$$, then 

  $$h \circ (g \circ f) = (h \circ g) \circ f$$

7. for each morphism $$f$$, $$f \circ 1_{\textrm{dom}(f)} = f$$
8. for each morphism $$f$$, $$1_{\textrm{cod}(f)} \circ f = f$$
