---
layout: post
title: Reynolds Number Lattice Boltzman method simulation
---

[Simulation and modeling of natural processes \| University of Geneva \| Coursera](https://www.coursera.org/learn/modeling-simulation-natural-processes)

**Week 5: Lattice Boltzmann modeling of fluid flow. Jonas Latt**

```python
#!/usr/bin/python3
# Copyright (C) 2015 Universite de Geneve, Switzerland
# E-mail contact: jonas.latt@unige.ch
#
# 2D flow around a cylinder
#

from numpy import *
import matplotlib.pyplot as plt
from matplotlib import cm

###### Flow definition #########################################################
maxIter = 200000  # Total number of time iterations.
Re = 10.0         # Reynolds number.
nx, ny = 420, 180 # Numer of lattice nodes.
ly = ny-1         # Height of the domain in lattice units.
cx, cy, r = nx//4, ny//2, ny//9 # Coordinates of the cylinder.
uLB     = 0.04                  # Velocity in lattice units.
nulb    = uLB*r/Re;             # Viscoscity in lattice units.
omega = 1 / (3*nulb+0.5);    # Relaxation parameter.

###### Lattice Constants #######################################################
v = array([ [ 1,  1], [ 1,  0], [ 1, -1], [ 0,  1], [ 0,  0],
            [ 0, -1], [-1,  1], [-1,  0], [-1, -1] ])
t = array([ 1/36, 1/9, 1/36, 1/9, 4/9, 1/9, 1/36, 1/9, 1/36])

col1 = array([0, 1, 2])
col2 = array([3, 4, 5])
col3 = array([6, 7, 8])

###### Function Definitions ####################################################
def macroscopic(fin):
    rho = sum(fin, axis=0)
    u = zeros((2, nx, ny))
    for i in range(9):
        u[0,:,:] += v[i,0] * fin[i,:,:]
        u[1,:,:] += v[i,1] * fin[i,:,:]
    u /= rho
    return rho, u

def equilibrium(rho, u):              # Equilibrium distribution function.
    usqr = 3/2 * (u[0]**2 + u[1]**2)
    feq = zeros((9,nx,ny))
    for i in range(9):
        cu = 3 * (v[i,0]*u[0,:,:] + v[i,1]*u[1,:,:])
        feq[i,:,:] = rho*t[i] * (1 + cu + 0.5*cu**2 - usqr)
    return feq

###### Setup: cylindrical obstacle and velocity inlet with perturbation ########
# Creation of a mask with 1/0 values, defining the shape of the obstacle.
def obstacle_fun(x, y):
    return (x-cx)**2+(y-cy)**2<r**2

obstacle = fromfunction(obstacle_fun, (nx,ny))

# Initial velocity profile: almost zero, with a slight perturbation to trigger
# the instability.
def inivel(d, x, y):
    return (1-d) * uLB * (1 + 1e-4*sin(y/ly*2*pi))

vel = fromfunction(inivel, (2,nx,ny))

# Initialization of the populations at equilibrium with the given velocity.
fin = equilibrium(1, vel)

###### Main time loop ##########################################################
for time in range(maxIter):
    # Right wall: outflow condition.
    fin[col3,-1,:] = fin[col3,-2,:] 

    # Compute macroscopic variables, density and velocity.
    rho, u = macroscopic(fin)

    # Left wall: inflow condition.
    u[:,0,:] = vel[:,0,:]
    rho[0,:] = 1/(1-u[0,0,:]) * ( sum(fin[col2,0,:], axis=0) +
                                  2*sum(fin[col3,0,:], axis=0) )
    # Compute equilibrium.
    feq = equilibrium(rho, u)
    fin[[0,1,2],0,:] = feq[[0,1,2],0,:] + fin[[8,7,6],0,:] - feq[[8,7,6],0,:]

    # Collision step.
    fout = fin - omega * (fin - feq)

    # Bounce-back condition for obstacle.
    for i in range(9):
        fout[i, obstacle] = fin[8-i, obstacle]

    # Streaming step.
    for i in range(9):
        fin[i,:,:] = roll(
                            roll(fout[i,:,:], v[i,0], axis=0),
                            v[i,1], axis=1 )
 
    # Visualization of the velocity.
    if (time%100==0):
        plt.clf()
        plt.imshow(sqrt(u[0]**2+u[1]**2).transpose(), cmap=cm.Reds)
        plt.savefig("vel.{0:04d}.png".format(time//100))
```

```bash
ffmpeg -framerate 12 -i vel.%04d.png -crf 0 vel.mp4
```

# Re=10

  <video
    id="lbm10"
    class="video-js"
    controls
    preload="auto"
    width="500"
    height="250"
    poster="/modeling/lbm10/vel.1999.png"
    data-setup="{}">
    <source src="/modeling/lbm10/vel.mp4" type="video/mp4"/>
    <p class="vjs-no-js">
      To view this video please enable JavaScript, and consider upgrading to a
      web browser that
      <a href="https://videojs.com/html5-video-support/" target="_blank">supports HTML5 video</a>
    </p>
  </video>

# Re=20

  <video
    id="lbm20"
    class="video-js"
    controls
    preload="auto"
    width="500"
    height="250"
    poster="/modeling/lbm20/vel.1499.png"
    data-setup="{}">
    <source src="/modeling/lbm20/vel.mp4" type="video/mp4"/>
    <p class="vjs-no-js">
      To view this video please enable JavaScript, and consider upgrading to a
      web browser that
      <a href="https://videojs.com/html5-video-support/" target="_blank">supports HTML5 video</a>
    </p>
  </video>

# Re=28

  <video
    id="lbm28"
    class="video-js"
    controls
    preload="auto"
    width="500"
    height="250"
    poster="/modeling/lbm28/vel.2999.png"
    data-setup="{}">
    <source src="/modeling/lbm28/vel.mp4" type="video/mp4"/>
    <p class="vjs-no-js">
      To view this video please enable JavaScript, and consider upgrading to a
      web browser that
      <a href="https://videojs.com/html5-video-support/" target="_blank">supports HTML5 video</a>
    </p>
  </video>

# Re=30

  <video
    id="lbm30"
    class="video-js"
    controls
    preload="auto"
    width="500"
    height="250"
    poster="/modeling/lbm30/vel.1999.png"
    data-setup="{}">
    <source src="/modeling/lbm30/vel.mp4" type="video/mp4"/>
    <p class="vjs-no-js">
      To view this video please enable JavaScript, and consider upgrading to a
      web browser that
      <a href="https://videojs.com/html5-video-support/" target="_blank">supports HTML5 video</a>
    </p>
  </video>

# Re=35

  <video
    id="lbm35"
    class="video-js"
    controls
    preload="auto"
    width="500"
    height="250"
    poster="/modeling/lbm35/vel.1999.png"
    data-setup="{}">
    <source src="/modeling/lbm35/vel.mp4" type="video/mp4"/>
    <p class="vjs-no-js">
      To view this video please enable JavaScript, and consider upgrading to a
      web browser that
      <a href="https://videojs.com/html5-video-support/" target="_blank">supports HTML5 video</a>
    </p>
  </video>

# Re=40

  <video
    id="lbm40"
    class="video-js"
    controls
    preload="auto"
    width="500"
    height="250"
    poster="/modeling/lbm40/vel.1999.png"
    data-setup="{}">
    <source src="/modeling/lbm40/vel.mp4" type="video/mp4"/>
    <p class="vjs-no-js">
      To view this video please enable JavaScript, and consider upgrading to a
      web browser that
      <a href="https://videojs.com/html5-video-support/" target="_blank">supports HTML5 video</a>
    </p>
  </video>


<script>
  var player = videojs('lbm10');
</script>

<script>
  var player = videojs('lbm20');
</script>

<script>
  var player = videojs('lbm28');
</script>

<script>
  var player = videojs('lbm30');
</script>

<script>
  var player = videojs('lbm40');
</script>