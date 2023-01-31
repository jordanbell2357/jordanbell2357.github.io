---
layout: post
title: bc
---

> *DESCRIPTION*  
> The *bc* utility shall implement an arbitrary precision calculator. It shall take input from any files given,
> then read from the standard input. If the standard input and standard output to *bc* are attached to a terminal,
> the invocation of *bc* shall be considered to be interactive, causing behavioral constraints described in
> the following sections.
>
> *OPTIONS*  
>
> The following option shall be supported:
>
> **-l**  
> (The letter ell.) Define the math functions and initialize *scale* to 20, instead of the default zero; see the EXTENDED DESCRIPTION section. [^1]

> Each expression or named expression has a *scale*, which is the number of decimal digits that shall be maintained as the fractional portion of the expression.


[Advanced Bash-Scripting Guide \| LDP](https://tldp.org/LDP/abs/html/index.html)

[bc: an arbitrary precision calculator language \| GNU](https://www.gnu.org/software/bc/manual/html_mono/bc.html)

[^1]: [The Open Group Base Specifications Issue 7, 2018 edition](https://pubs.opengroup.org/onlinepubs/9699919799/)

