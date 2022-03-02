---
layout: post
title: Integrals of Products of Sines and Cosines
---

\[
P_n(\theta) = \prod_{k=1}^n (1-e^{ik\theta})
\]

\[
Q_n(\theta) = \prod_{k=1}^n (1+e^{ik\theta})
\]

Let \( N=\frac{n(n+1)}{2} \). Then
\[
P_n(\theta)=(-2i)^n e^{\frac{iN\theta}{2}} \prod_{k=1}^n \sin\big(\frac{k\theta}{2} \big)
\]
and
\[
Q_n(\theta)=2^n e^{\frac{iN\theta}{2}} \prod_{k=1}^n \cos\big(\frac{k\theta}{2} \big)
\]

Define
\[
\widehat{f}(n) = \int_0^{2\pi} f(\theta) e^{-in\theta} d\theta
\]
and for $1 \leq p < \infty$,
\[
|f|_p = \Big( \frac{1}{2\pi} \int_0^{2\pi} |f(\theta)|^p d\theta \Big)^{\frac{1}{p}}
\]
and
\[
|\widehat{f}|_p = \Big( \sum_{k \in \mathbb{Z}} |\widehat{f}(k)|^p \Big)^{\frac{1}{p}}
\]


<figure>
    <img src="/Python/sineproduct/sine10plot.png" alt="Plot of sine product for n=10" style="display:block;margin-left:auto;margin-right:auto;">
    <figcaption align="center">
        \(\prod_{k=1}^{10} 2|\sin(k \theta)|\) for \(0 \leq \theta \leq \frac{\pi}{2}\)
    </figcaption>
</figure>
