---
layout: post
title: Integrals of Products of Sines and Cosines
---

## Desmos plots

[product of sin(kx)](https://www.desmos.com/calculator/ve6lbmxkhr)

<iframe src="https://www.desmos.com/calculator/ve6lbmxkhr?embed" width="500" height="500" style="border: 1px solid #ccc" frameborder=0></iframe>

## Mathematica plots

Bell, Jordan. “Estimates for the Norms of Products of Sines and Cosines.” *Journal of Mathematical Analysis and Applications* 405, no. 2 (2013): 530–45. <https://doi.org/10.1016/j.jmaa.2013.04.010>.

$$
P_n(\theta) = \prod_{k=1}^n (1-e^{ik\theta})
$$

$$
Q_n(\theta) = \prod_{k=1}^n (1+e^{ik\theta})
$$

Let \\( N=\frac{n(n+1)}{2} \\).
$$
P_n(\theta)=(-2i)^n e^{\frac{iN\theta}{2}} \prod_{k=1}^n \sin\big(\frac{k\theta}{2} \big)
$$
and
$$
Q_n(\theta)=2^n e^{\frac{iN\theta}{2}} \prod_{k=1}^n \cos\big(\frac{k\theta}{2} \big)
$$

Define
$$
\widehat{f}(n) = \int_0^{2\pi} f(\theta) e^{-in\theta} d\theta
$$

For \\(1 \leq p < \infty\\), define
$$
|f|_{L^p} = \Big( \frac{1}{2\pi} \int_0^{2\pi} |f(\theta)|^p d\theta \Big)^{\frac{1}{p}}
$$
and
$$
|\widehat{f}|_{\ell^p} = \Big( \sum_{k \in \mathbb{Z}} |\widehat{f}(k)|^p \Big)^{\frac{1}{p}}
$$


<figure>
    <img src="/Python/sineproduct/sine10plot.png" alt="Plot of sine product for n=10" style="display:block;margin-left:auto;margin-right:auto;">
    <figcaption align="center">
        \(\prod_{k=1}^{10} 2|\sin(k \theta)|\) for \(0 \leq \theta \leq \frac{\pi}{2}\)
    </figcaption>
</figure>

<figure>
    <img src="/Python/sineproduct/cosine10plot.png" alt="Plot of sine product for n=10" style="display:block;margin-left:auto;margin-right:auto;">
    <figcaption align="center">
        \(\prod_{k=1}^{10} 2|\sin(k \theta)|\) for \(0 \leq \theta \leq \frac{\pi}{2}\)
    </figcaption>
</figure>

<figure>
    <img src="/Python/sineproduct/ell1Pn1to500.png" alt="Plot of sine product for n=10" style="display:block;margin-left:auto;margin-right:auto;">
    <figcaption align="center">
        \(\prod_{k=1}^{10} 2|\sin(k \theta)|\) for \(0 \leq \theta \leq \frac{\pi}{2}\)
    </figcaption>
</figure>

<figure>
    <img src="/Python/sineproduct/ell3Qn1to400.png" alt="Plot of sine product for n=10" style="display:block;margin-left:auto;margin-right:auto;">
    <figcaption align="center">
        \(\prod_{k=1}^{10} 2|\sin(k \theta)|\) for \(0 \leq \theta \leq \frac{\pi}{2}\)
    </figcaption>
</figure>

<figure>
    <img src="/Python/sineproduct/L1plot1to400.png" alt="Plot of sine product for n=10" style="display:block;margin-left:auto;margin-right:auto;">
    <figcaption align="center">
        \(\prod_{k=1}^{10} 2|\sin(k \theta)|\) for \(0 \leq \theta \leq \frac{\pi}{2}\)
    </figcaption>
</figure>

<figure>
    <img src="/Python/sineproduct/L2plot1to400.png" alt="Plot of sine product for n=10" style="display:block;margin-left:auto;margin-right:auto;">
    <figcaption align="center">
        \(\prod_{k=1}^{10} 2|\sin(k \theta)|\) for \(0 \leq \theta \leq \frac{\pi}{2}\)
    </figcaption>
</figure>