---
layout: post
title: FFmpeg and ImageMagick
---

<link href="https://vjs.zencdn.net/7.8.4/video-js.css" rel="stylesheet" />
<script src="https://vjs.zencdn.net/7.8.4/video.js"></script>

[ffmpeg Documentation](https://ffmpeg.org/ffmpeg.html)

[Convert Between Image Formats \| ImageMagick](https://imagemagick.org/script/convert.php)

```bash
# Create 30 images with increasing filled progress bars
for i in {1..30}; do
    progress=$((i*1000/30))  # increase size 10 times
    convert -size 1000x200 xc:grey50 -fill "rgb(100,149,237)" -draw "rectangle 0,0 $progress,200" progress_$(printf "%02d" $i).png
done

width=2000  # change this to the width of your original images

# Overlay progress bar onto each image, create new image
for i in {1..30}; do
    # Calculate progress bar position
    x_offset=$(( (width-1000)/2 ))  # center the progress bar

    # Overlay progress bar and save as new image
    convert ais_june_choropleth_$i.png progress_$(printf "%02d" $i).png -geometry +$x_offset+10 -composite ais_june_choropleth_progress_$(printf "%02d" $i).png
done

# Create video using ffmpeg
ffmpeg -framerate 5 -pattern_type glob -i 'ais_june_choropleth_progress_*.png' -c:v libx264 -r 30 -pix_fmt yuv420p ais_june_choropleth.mp4

# Clean up progress bar and composite images
rm progress_*.png
rm ais_june_choropleth_progress_*.png
```

<body>
  <video
    id="my-video"
    class="video-js"
    controls
    preload="auto"
    width="640"
    height="264"
    poster="/images/FFmpeg/ais_june_choropleth_1.png"
    data-setup="{}"
  >
    <source src="/images/FFmpeg/ais_june_choropleth.mp4" type="video/mp4" />
    <p class="vjs-no-js">
      To view this video please enable JavaScript, and consider upgrading to a
      web browser that
      <a href="https://videojs.com/html5-video-support/" target="_blank"
        >supports HTML5 video</a
      >
    </p>
  </video>

  <script>
    var player = videojs('my-video');
  </script>
</body>
