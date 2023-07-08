---
layout: post
title: Jaccard similarity
---

https://deepai.org/machine-learning-glossary-and-terms/jaccard-index

https://en.wikipedia.org/wiki/MinHash

https://scikit-learn.org/stable/modules/generated/sklearn.metrics.jaccard_score.html

Let there be given nonempty sets $$A$$ and $$B$$. Define

$$
\begin{equation}
J(A,B) = \dfrac{|A \cup B|}{|A \cap B|}.
\label{J}
\end{equation}
$$

$$\eqref{J}$$

$$
A \triangle B = (A \cup B) \setminus (A \cap B).
$$

$$
|A \triangle B| = |A \cup B| - |A \cap B|,
$$

so

$$
|A \cup B| = |A \cap B| + |A \triangle B|.
$$
