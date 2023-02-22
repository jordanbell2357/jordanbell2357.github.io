---
layout: post
title: Diophantine approximation sum plots
---

```python3
import math
import matplotlib.pyplot as plt

def int_dist(x):
    return abs(x - round(x))

def f(m, x):
    return 1/(m*math.log(m)) * sum([1 / int_dist(j*x) for j in range(1,m+1)])
```

```python3
X20000_40000 = range(20000,40000+1)

Y20000_40000_g = [f(m,(-1+math.sqrt(5))/2) for m in range(20000,40000+1)]
```

```python3
plt.rcParams['text.usetex'] = True
plt.plot(X20000_40000, Y20000_40000)
plt.xlabel(r'$m$')
plt.title(r'$m \mapsto \frac{1}{m \log m}\displaystyle \sum_{j=1}^m \frac{1}{\vert \vert jx \vert \vert}$ for $x=\frac{-1+\sqrt{5}}{2}$')
plt.savefig('m20000_40000.png', dpi=300)
```

Let $$\vert \vert x \vert \vert$$ be the distance from $$x \in \mathbb{R}$$ to $$\mathbb{Z}$$, that is,
the distance from $$x$$ to the nearest integer.

$$\vert \vert x \vert \vert$$ = `int_dist(x)`

![Golden ratio](/python/m5000_40000_g.png)

![Golden ratio](/python/m20000_40000_g.png)

![√ 5 divided by 2](/python/m5000_40000_sqrt_5_div_2.png)

![√ 5 divided by 2](/python/m20000_40000_sqrt_5_div_2.png)

![√ 2](/python/m5000_40000_sqrt_2.png)

![√ 3](/python/m5000_40000_sqrt_3.png)

![√ 5](/python/m5000_40000_sqrt_5.png)

![√ 5](/python/m20000_40000_sqrt_5.png)

![√ 6](/python/m5000_40000_sqrt_6.png)

![√ 7](/python/m5000_40000_sqrt_7.png)

![√ 10](/python/m5000_40000_sqrt_10.png)

![√ 11](/python/m5000_40000_sqrt_11.png)

![√ 13](/python/m5000_40000_sqrt_13.png)

![√ 15](/python/m5000_40000_sqrt_15.png)

![√ 17](/python/m5000_40000_sqrt_17.png)

![√ 17](/python/m20000_40000_sqrt_17.png)

![√ 19](/python/m5000_40000_sqrt_19.png)

![√ 23](/python/m5000_40000_sqrt_23.png)

![e](/python/m20000_40000_e.png)