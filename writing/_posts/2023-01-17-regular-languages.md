---
layout: post
title: Regular languages
---

# Category theory and strings

Let $$\mathbb{N}=\{0,1,2,\ldots\}$$. For $$n \in \mathbb{N}$$, define

$$[n] = \{i \in \mathbb{N} : i < n\}$$.

For sets $$X$$ and $$Y$$,
let $$Y^X$$ be the set of functions with domain $$X$$ and image contained in $$Y$$.

The empty set $$\emptyset$$ is an **initial object** in the category of sets:
for any set $$Y$$ there is a unique function $$\emptyset_Y:\emptyset \to Y$$.[^1]

[^1]: [empty function in nLab](https://ncatlab.org/nlab/show/empty+function)

Let $$A$$ be a finite set, which we call **an alphabet**.
We write $$\epsilon_A$$ for the unique function $$\emptyset_A:\emptyset \to A$$, in other words, $$\epsilon_A=\emptyset_A$$. 

A **string over** $$A$$ **of length** $$n$$, $$n \in \mathbb{N}$$, is an element
of $$A^{[n]}$$.

A string over $$A$$ of length 0 is an element of $$A^{[0]}=\{\epsilon_A\}$$. That is,
a string over $$A$$ of length 0 is $$\epsilon_A$$. We call $$\epsilon_A$$ the **empty string** over $$A$$.











<https://opendsa-server.cs.vt.edu/OpenDSA/Books/PIFLAS22/html/index.html>

<https://www.csm.ornl.gov/~sheldon/ds/>

<https://ncatlab.org/nlab/show/free+monoid>

<https://encyclopediaofmath.org/wiki/Formal_languages_and_automata>

<https://introcs.cs.princeton.edu/java/51language/>


<https://icsatkcc.github.io/Discrete-Math-for-Computer-Science/s-free-monoids-and-languages.html>