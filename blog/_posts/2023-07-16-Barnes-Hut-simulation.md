---
layout: post
title: Barnes Hut simulation
---

[Simulation and modeling of natural processes \| University of Geneva \| Coursera](https://www.coursera.org/learn/modeling-simulation-natural-processes)

**Week 6: Particles and point-like objects. Jonas Latt**

# 2d

  <video
    id="barnes_hut_2d"
    class="video-js"
    controls
    preload="auto"
    width="500"
    height="250"
    poster="/modeling/barnes_hut_2d/bodies_000499.png"
    data-setup="{}">
    <source src="/modeling/barnes_hut_2d/barnes_hut_2d.mp4" type="video/mp4"/>
    <p class="vjs-no-js">
      To view this video please enable JavaScript, and consider upgrading to a
      web browser that
      <a href="https://videojs.com/html5-video-support/" target="_blank">supports HTML5 video</a>
    </p>
  </video>

```bash
ffmpeg -framerate 36 -i bodies_%06d.png -c:v libx264 -pix_fmt yuv420p barnes_hut_2d.mp4
```

# 3d

  <video
    id="barnes_hut_3d"
    class="video-js"
    controls
    preload="auto"
    width="500"
    height="250"
    poster="/modeling/barnes_hut_3d/bodies3D_000499.png"
    data-setup="{}">
    <source src="/modeling/barnes_hut_3d/barnes_hut_3d.mp4" type="video/mp4"/>
    <p class="vjs-no-js">
      To view this video please enable JavaScript, and consider upgrading to a
      web browser that
      <a href="https://videojs.com/html5-video-support/" target="_blank">supports HTML5 video</a>
    </p>
  </video>

```bash
ffmpeg -framerate 36 -i bodies3D_%06d.png -c:v libx264 -pix_fmt yuv420p barnes_hut_3d.mp4
```

<script>
  var player = videojs('barnes_hut_2d');
</script>

<script>
  var player = videojs('barnes_hut_3d');
</script>