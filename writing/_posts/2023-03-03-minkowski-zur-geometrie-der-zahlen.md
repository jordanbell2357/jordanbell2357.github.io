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

[H. Minkowski. *Zur Geometrie der Zahlen.* PDF](/gs/Minkowski/Minkowski1904.pdf)

> Mit Projektionsbildern auf einer Doppeltafel.

These figures are either absent or incompletely scanned in most online scans of these congress proceedings. These figures are
scanned in the Bibliothèque nationale de France (BnF) Gallica copy:

<https://gallica.bnf.fr/ark:/12148/bpt6k99443c/f188.item.r=Minkowski>

[Figures PDF](/gs/Minkowski/Doppeltafel.pdf)

ImageMagick: [^3]

[^3]: [ImageMagick](https://imagemagick.org/script/magick.php)

```bash
convert -density 600 Doppeltafel.pdf[2] -background white -flatten -resize 1400x1400^ -quality 100 Doppeltafel.png
```

[![Figures PNG](/gs/Minkowski/Doppeltafel.png)](/gs/Minkowski/Doppeltafel.png)