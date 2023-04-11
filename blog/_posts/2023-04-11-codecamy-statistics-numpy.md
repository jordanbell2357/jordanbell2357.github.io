---
layout: post
title: Codecamy Learn Statistics with NumPy
---

```
13.89,14.7,13.,11.37,12.1,11.82,13.09,13.78,12.,12.83,12.1,11.09,13.32,11.86,14.35,11.7,12.85,14.,13.83,12.02,12.05,14.1,12.39,11.83,13.18,11.43,14.61,13.12,11.5,11.15,12.64,14.07,12.44,11.21,14.31,14.62,14.67,14.55,12.72,11.19,13.27,12.02,13.79,13.14,14.51,12.37,14.06,14.36,11.24,14.73,13.03,13.86,13.33,11.3,12.18,11.75,14.69,14.18,14.05,12.58,14.53,12.45,14.44,12.76,11.65,14.7,14.54,12.98,13.08,14.63,13.22,12.59,14.62,11.37,14.55,14.7,14.89,11.45,14.74,13.78,13.62,12.36,11.15,11.15,13.1,12.82,12.34,13.25,12.1,14.69,14.58,14.89,14.03,12.29,12.03,11.83,13.57,11.75,13.64,12.42,13.07,12.97,14.89,11.23,13.45,14.11,12.47,12.24,13.9,12.85,14.65,13.54,12.76,12.41,11.61,11.77,11.44,13.85,13.02,14.61,13.68,12.99,11.88,12.48,12.78,12.23,13.88,12.83,13.41,13.9,12.35,12.91,11.32,13.63,11.37,12.87,11.27,12.56,11.87,12.53,14.5,11.38,11.25,11.13,13.7,12.58,11.88,14.5,11.91,13.87,14.38,12.04,13.61,13.1,12.96,12.3,14.54,13.66,14.86,12.42,14.34,14.1,12.37,14.33,11.64,13.45,13.49,13.55,12.65,11.54,12.48,12.26,13.93,11.98,12.04,14.59,11.51,12.49,13.71,11.26,12.15,13.84,14.62,11.76,12.59,13.56,12.21,11.24,14.47,14.63,12.51,11.43,14.84,14.14,14.16,12.93,13.19,11.53,12.78,12.79
```

```python3
import numpy as np
from matplotlib import pyplot as plt

sunflowers = np.genfromtxt('sunflower_heights.csv', delimiter=',')

# Calculate mean and std of sunflowers here:
sunflowers_mean = np.mean(sunflowers)
sunflowers_std = np.std(sunflowers)

# Calculate sunflowers_normal here:
sunflowers_normal = np.random.normal(sunflowers_mean, sunflowers_std, size=5000)

plt.hist(sunflowers, range=(11, 15), histtype='step', linewidth=2, label='observed',
         density=True)
plt.hist(sunflowers_normal, range=(11, 15), histtype='step', linewidth=2, label='normal',
         density=True)
plt.legend()
plt.savefig('sunflowers.png')
plt.show()
```

![Two histograms of observed sunflower heights and counterfactual normal sunflower heights](/images/Codecamy/sunflowers.png)