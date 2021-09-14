---
layout: page
title: Tutorials
permalink: /tutorials/
---

```
import numpy as np
from numpy.polynomial import Polynomial
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import rcParams

# make sure the full paths for ImageMagick and ffmpeg are configured
rcParams['animation.convert_path'] = '/usr/bin/convert'
rcParams['animation.ffmpeg_path'] = '/home/jordan/anaconda3/bin/ffmpeg'

fig, ax = plt.subplots()

t = np.arange(-3, 7, 1)
p = Polynomial([1, 1, 1])
q = p(t)
l = plt.plot(t, q)

ax = plt.axis([-5,5,-1,10])

redDot, = plt.plot([-3], [p(-3)], 'ro')

def animate(i):
    redDot.set_data(i, p(i))
    return redDot,

# create animation using the animate() function with no repeat
myAnimation = animation.FuncAnimation(fig, animate, frames=np.arange(-5, 5, 1), \
                                      interval=10, blit=True, repeat=False)

# save animation at 30 frames per second 
myAnimation.save('myAnimation.gif', writer='imagemagick', fps=30)
```
![Parabola](/assets/images/myAnimation.gif)