---
layout: post
title: The figures in Minkowski's Zur Geometrie der Zahlen
---

<http://histmath-heidelberg.de/htmg/imc-1904.htm>

H. Minkowski. *Zur Geometrie der Zahlen.* pp. 164-173 in A. Krazer, ed. *Verhandlungen des dritten Internationalen Mathematiker- Kongresses in Heidelberg vom 8. bis 13. August 1904.* B. G. Teubner. Leipzig. 1905.

<https://www.mathunion.org/fileadmin/ICM/Proceedings/ICM1904/ICM1904.ocr.pdf>

Ghostscript: [^1] [^2]

[^1]: [Ghostscript](https://www.ghostscript.com/)

[^2]: [GNU Ghostscript](https://www.gnu.org/software/ghostscript/)

```bash
gs -dNOPAUSE -dBATCH -dFirstPage=174 -dLastPage=183 -sDEVICE=pdfwrite -sOutputFile=Minkowski1904.pdf -f ICM1904.ocr.pdf
```

<samp>
GPL Ghostscript 9.55.0 (2021-09-27)  
Copyright (C) 2021 Artifex Software, Inc.  All rights reserved.  
This software is supplied under the GNU AGPLv3 and comes with NO WARRANTY:  
see the file COPYING for details.  
Processing pages 174 through 183.  
Page 174  
Loading NimbusRoman-Regular font ... done.  
Loading NimbusRoman-Bold font ... done.  
Loading NimbusRoman-BoldItalic font ... done.  
Page 175  
Page 176  
Page 177  
Loading NimbusRoman-Italic font ... done done.  
Page 178  
Page 179  
Page 180  
Page 181  
Page 182  
Page 183
</samp>

[H. Minkowski. *Zur Geometrie der Zahlen.* PDF](/gs/Minkowski1904.pdf)

> Mit Projektionsbildern auf einer Doppeltafel.

These figures are either absent or incompletely scanned in most online scans of these congress proceedings. These figures are
scanned in the Bibliothèque nationale de France (BnF) Gallica copy:

<https://gallica.bnf.fr/ark:/12148/bpt6k99443c/f188.item.r=Minkowski>

[Figures PDF](/gs/Doppeltafel.pdf)

ImageMagick: [^3]

[^3]: [ImageMagick](https://imagemagick.org/script/magick.php)

```bash
convert -density 600 Doppeltafel.pdf[2] -background white -flatten -resize 1400x1400^ -quality 100 Doppeltafel.png
```

[![Figures PNG](/gs/Doppeltafel.png)](/gs/Doppeltafel.png)