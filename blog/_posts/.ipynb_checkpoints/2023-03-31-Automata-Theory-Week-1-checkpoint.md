---
layout: post
title: Stanford Automata Theory Week 1
---

[Automata Theory \| edX](https://www.edx.org/course/automata-theory)

John E. Hopcroft, Rajeev Motwani, and Jeffrey D. Ullman. *Introduction to Automata Theory, Languages, and Computation*. 3rd ed. Pearson. 2007.

2.2.1 Definition of a Deterministic Finite Automaton, p. 45:

A **deterministic finite automaton** comprises

1. A finite set $$Q$$ of **states**
2. A finite set $$\Sigma$$ of **input symbols**
3. A function $$\delta:\Sigma \times Q \to Q$$, the **transition map**
4. An element $$q_0$$ of $$Q$$, the **initial state**
5. A subset $$F$$ of $$Q$$, the **final states**

$$A=(Q,\Sigma,\delta,q_0,F)$$

Let $$a = a_1 \cdots a_n \in \Sigma^n$$, a **string of length** $$n$$.
Define by induction $$q_i = \delta(q_{i-1}, a_i)$$ for $$1 \leq i \leq n$$. (The induction is on $$n$$, not on $$i$$.)
The string is said to be **accepted** by $$A$$ if $$q_n \in F$$, and **rejected** by $$A$$ if $$q_n \not \in F$$.




