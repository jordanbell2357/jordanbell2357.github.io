---
layout: post
title: LaTeXML
---

[LaTeXML \| NIST](https://math.nist.gov/~BMiller/LaTeXML/)

```bash
latexml --destination=diophantine.xml diophantine.tex
```

<samp>
Conversion complete 3 warnings (See /mnt/c/Users/jorda/Documents/GitHub/LaTeX/diophantine/diophantine.latexml.log) (reqd. 1m 46.07s)
</samp>

```bash
latexmlpost diophantine.xml --destination=index.html --javascript="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js?config=MML_HTMLorMML" --navigationtoc=context --css=LaTeXML-navbar-left.css
```

<samp>
Postprocessing complete No obvious problems (reqd. 22.31s)
</samp>

[Sums, series, and products in Diophantine approximation \| Jordan Bell](https://jordanbell.info/LaTeX/diophantine/)