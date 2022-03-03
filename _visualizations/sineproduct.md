---
layout: post
title: Integrals of Products of Sines and Cosines
---

- [Mathematica plots](#mathematica)
- [Desmos](#desmos)

## Mathematica plots {#mathematica}

Bell, Jordan. “Estimates for the Norms of Products of Sines and Cosines.” *Journal of Mathematical Analysis and Applications* 405, no. 2 (2013): 530–45. <https://doi.org/10.1016/j.jmaa.2013.04.010>.

$$
P_n(\theta) = \prod_{k=1}^n (1-e^{ik\theta})
$$

$$
P_n(\theta)=(-2i)^n e^{\frac{iN\theta}{2}} \prod_{k=1}^n \sin\bigg(\frac{k\theta}{2} \bigg), \qquad N=\frac{n(n+1)}{2}
$$

<figure>
    <img src="/Python/sineproduct/sine10plot.png" alt="Plot of sine product for n=1 to 10" style="display:block;margin-left:auto;margin-right:auto;">
    <figcaption align="center">
        \(\prod_{k=1}^{10} 2|\sin(k \theta)|\) for \(0 \leq \theta \leq \frac{\pi}{2}\)
    </figcaption>
</figure>



$$
|f|_{L^1} = \frac{1}{2\pi} \int_0^{2\pi} |f(\theta)|^p d\theta
$$

$$
|f|_{L^2} = \left(\frac{1}{2\pi} \int_0^{2\pi} |f(\theta)|^p d\theta\right)^{\frac{1}{2}}
$$

$$
|f|_{L^3} = \left(\frac{1}{2\pi} \int_0^{2\pi} |f(\theta)|^3 d\theta\right)^{\frac{1}{3}}
$$

$$
K = \log 2 + \max_{0 < w < 1} \Bigg( \frac{1}{w} \int_0^w \log \sin(\pi t) dt \Bigg)
$$

<figure>
    <img src="/Python/sineproduct/L1plot1to400.png" alt="Plot of sine product L1 norms for n=1 to 400" style="display:block;margin-left:auto;margin-right:auto;">
    <figcaption align="center">
        \(\frac{|P_n|_{L^1}}{e^{nK} n^{-1}}\) for \(n=1,\ldots,400\)
    </figcaption>
</figure>

<figure>
    <img src="/Python/sineproduct/L2plot1to400.png" alt="Plot of sine product L2 norms for n=1 to 400" style="display:block;margin-left:auto;margin-right:auto;">
    <figcaption align="center">
        \(\frac{|P_n|_{L^2}}{e^{nK}n^{-1/4}}\) for \(n=1,\ldots,400\)
    </figcaption>
</figure>

$$
\widehat{f}(n) = \int_0^{2\pi} f(\theta) e^{-in\theta} d\theta
$$

$$
\widehat{f}|_{\ell^1} = \sum_{k \in \mathbb{Z}} |\widehat{f}(k)|
$$

<figure>
    <img src="/Python/sineproduct/cosine10plot.png" alt="Plot of cosine product for n=1 to 10" style="display:block;margin-left:auto;margin-right:auto;">
    <figcaption align="center">
        \(\prod_{k=1}^{10} 2|\cos(k \theta)|\) for \(0 \leq \theta \leq \frac{\pi}{2}\)
    </figcaption>
</figure>

<figure>
    <img src="/Python/sineproduct/ell1Pn1to500.png" alt="Plot of l1 norms of Fourier series for sine product for n=1 to 500" style="display:block;margin-left:auto;margin-right:auto;">
    <figcaption align="center">
        \(\prod_{k=1}^{10} 2|\sin(k \theta)|\) for \(0 \leq \theta \leq \frac{\pi}{2}\)
    </figcaption>
</figure>

<figure>
    <img src="/Python/sineproduct/ell3Qn1to400.png" alt="Plot of l3 norms of Fourier series for cosine product for n=1 to 400" style="display:block;margin-left:auto;margin-right:auto;">
    <figcaption align="center">
        \(\frac{|\widehat{Q}_n|_3}{2^n n^{-1}}\) for \(n=1,\ldots,400\)
    </figcaption>
</figure>





$$
Q_n(\theta) = \prod_{k=1}^n (1+e^{ik\theta})
$$

$$
Q_n(\theta)=2^n e^{\frac{iN\theta}{2}} \prod_{k=1}^n \cos\big(\frac{k\theta}{2} \big), N=\frac{n(n+1)}{2}
$$

## Desmos plots {#desmos}

[product of sin(kx)](https://www.desmos.com/calculator/ve6lbmxkhr)

<iframe src="https://www.desmos.com/calculator/ve6lbmxkhr?embed" width="500" height="500" style="border: 1px solid #ccc" frameborder=0></iframe>