---
layout: post
title: Formal language theory
---

The empty set $$\emptyset$$ is an **initial object** in the category of sets:
for any set $$Y$$ there is a unique function $$\emptyset_Y:\emptyset \to Y$$.[^1]

[^1]: [empty function in nLab](https://ncatlab.org/nlab/show/empty+function)

For sets $$X$$ and $$Y$$, let $$Y^X$$ be the set of functions with domain $$X$$ and image contained in $$Y$$.
In particular, $$Y^\emptyset = \{\emptyset_Y\}$$.



Let $$\mathbb{N}=\{0,1,2,\ldots\}$$. For $$n \in \mathbb{N}$$, define

$$[n] = \{i \in \mathbb{N} : i < n\}$$.

<table>
  <tr>
    <th>\(n\)</th>
    <th>\([n]\)</th>
  </tr>
  <tr>
    <td>0</td>
    <td>\(\emptyset\)</td>
  </tr>
  <tr>
    <td>1</td>
    <td>\(\{0\}\)</td>
  </tr>
  <tr>
    <td>2</td>
    <td>\(\{0,1\}\)</td>
  </tr>
  <tr>
    <td>3</td>
    <td>\(\{0,1,2\}\)</td>
  </tr>
  <tr>
    <td>4</td>
    <td>\(\{0,1,2,3\}\)</td>
  </tr>
  <tr>
    <td>etc.</td>
    <td>etc.</td>
  </tr>
</table>

Let $$A$$ be a finite set that we shall call **an alphabet**.

Write $$\epsilon_A=\emptyset_A$$, the unique function
$$\emptyset \to A$$. Thus $$A^\emptyset = \{\epsilon_A\}$$.

A **word over the alphabet** $$A$$ **of length** $$n$$, $$n \in \mathbb{N}$$, is an element
of $$A^{[n]}$$.

A word over $$A$$ of length 0 is an element of $$A^{[0]}$$, and

$$A^{[0]} = A^\emptyset = \{\epsilon_A\}.$$

We call $$\epsilon_A$$ the **empty word** over the alphabet $$A$$.





<https://royalsocietypublishing.org/doi/10.1098/rstb.2012.0077>


<https://cs.lmu.edu/~ray/notes/languagetheory/>


<https://opendsa-server.cs.vt.edu/OpenDSA/Books/PIFLAS22/html/index.html>

<https://www.csm.ornl.gov/~sheldon/ds/>

<https://ncatlab.org/nlab/show/free+monoid>


<https://introcs.cs.princeton.edu/java/51language/>


<https://icsatkcc.github.io/Discrete-Math-for-Computer-Science/s-free-monoids-and-languages.html>