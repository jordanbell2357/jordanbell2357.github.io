---
layout: page
title: Euler
permalink: /euler/
---

## Leonhard Euler, *The Elements of Algebra* (*Vollständige Anleitung zur Algebra*)

#### Table of Contents

- [English table of contents](/assets/euler/en/TOCen.pdf)

- [German table of contents](/assets/euler/de/TOCde.pdf)

#### Part I. "Containing the Analysis of Determinate Quantities."

##### Section I. "Of the different Methods of calculating Simple Quantities."

{% assign PartISectionI = site.euler | where: "part", "I" | where: "section", "I" %}

{% for item in PartISectionI %}
###### [{{item.title}}]({{ item.url }})
{% endfor %}

<!--
{% for chapter in site.euler %}
- [{{chapter.title}}]({{ chapter.url }})
{% endfor %}
-->

#### Editions

1. Leonhard Euler. *Vollständige Anleitung zur Algebra. Mit den Zusätzen von Joseph Louis Lagrange.* Herausgegeben von Heinrich Weber. B. G. Teubner. Leipzig and Berlin. 1911. Leonhardi Euleri Opera omnia. Series prima. Opera mathematica. Volumen primum.
    - [Springer](https://link.springer.com/book/9783764314002)
2. Leonhard Euler. *Vollständige Anleitung zur Algebra*. Kayserlichen Akademie der Wissenschaften. St. Petersburg. 1771.
    - [ETH-Bibliothek Zürich](https://doi.org/10.3931/e-rara-9093)
    - [Bayerische Staatsbibliothek. Münchener DigitalisierungsZentrum (MDZ)](https://mdz-nbn-resolving.de/urn:nbn:de:bvb:12-bsb10081749-3)
3. Leonhard Euler. *Vollständige Anleitung zur Algebra. Zweyter Theil. Von Auflösung algebraischer Gleichungen und der unbestimmten Analytic*. Kays. Acad. der Wissenschaften. St. Petersburg. 1770.
    - [Deutsches Textarchiv](https://www.deutschestextarchiv.de/euler_algebra02_1770)
4. Leonhard Euler. *Élémens d'algèbre par M. Léonard Euler, traduits de l'allemand, avec des notes et des additions. Tome Premier. De l'analyse déterminée.* Translated by Jean Bernoulli. Chez Jean-Marie Bruyset, Pere & Fils. Lyon. 1774.
    - [BnF Gallica](https://gallica.bnf.fr/ark:/12148/bpt6k110159v)
5. Leonhard Euler. *Élémens d'algèbre par M. Léonard Euler, traduits de l'allemand, avec des notes et des additions. Tome Second. De l'analyse indéterminée.* Translated by Jean Bernoulli. Chez Jean-Marie Bruyset, Pere & Fils. Lyon. 1774.
    - [BnF Gallica](https://gallica.bnf.fr/ark:/12148/bpt6k123306p)
6. Leonhard Euler. *Elements of Algebra*. Translated by Rev. John Hewlett. Third Edition. Longmans, Hurst, Rees, Orme, and Co. London. 1822.
    - [Archive.org](https://archive.org/details/elementsofalgebr00euleuoft/)
7. Leonard Euler, *Elements of Algebra*, Translated by Rev. John Hewlett. (Reprinted from *Elements of Algebra*, Fifth Edition, Longman, Orme, and Co., London, 1840.) With an Introduction by Clifford Truesdell. Springer. 1972.
    - [Springer](https://doi.org/10.1007/978-1-4613-8511-0)
8. Leonhard Euler. *Elements of Algebra*. Translated by Rev. John Hewlett. Third Edition. Cambridge Library Collection - Mathematics. Cambridge University Press. 2009.
    - [Cambridge University Press](https://doi.org/10.1017/CBO9780511693519)
9. Scott L. Hecht. Transcription in Microsoft Word of Hewlett's translation. 2015.
    - [Archive.org](https://archive.org/details/ElementsOfAlgebraLeonhardEuler2015/)
    - [Amazon.com](https://www.amazon.com/Elements-Algebra-Leonhard-Euler/dp/150890118X)
10. Ian Bruce. *Euler's Algebra*. New translation from the German. 2016.
    - [Ian Bruce. 17centurymaths.com](https://www.17centurymaths.com/contents/euleralgebra.htm)