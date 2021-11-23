====================================================
WebQuiz: a LaTeX_ package for writing online quizzes
====================================================

WebQuiz_ makes it possible to use LaTeX_ to write interactive online quizzes.
The quizzes are first written in LaTeX_ and then converted into HTML using
WebQuiz_, which is written in python. The conversion from LaTeX_ to HTML is
done behind the scenes using TeX4ht_. The idea is that you should be able to
produce nice online quizzes using WebQuiz_ and basic knowledge of LaTeX_.

WebQuiz_ is designed to be used from the command-line.  For example, if
`quiz1.tex` is a LaTeX file for a quiz then:

:`latex quiz1`:
    produces a "readable" DVI file for the quiz
:`pdflatex quiz1`:
    produces a "readable" PDF file for the quiz
:`webquiz quiz1`:
    creates the web page `quiz1.html`

If you prefer to use LaTeX_ from a GUI for LaTeX_ then it should be possible to
configure it to use WebQuiz_ directly. As an example, the manual provides some
details about how to do this for TeXShop.

Usage
-----

usage: webquiz [-h] [-q] [-d] [-s] [--latex | -l | -x] [-r RCFILE]
               [-i | -e | --settings [SETTINGS]]
               [quiz_file [quiz_file ...]]

A LaTeX package for writing online quizzes

positional arguments:
  quiz_file             latex quiz files

optional arguments:
  -h, --help            show this help message and exit
  -q, --quiet           Suppress tex4ht messages (also -qq etc)
  -d, --draft           Use make4ht draft mode
  -s, --shell-escape    Shell escape for tex4ht/make4ht
  --latex               Use latex to compile document with make4ht (default)
  -l, --lua             Use lualatex to compile the quiz
  -x, --xelatex         Use xelatex to compile the quiz
  -r RCFILE, --rcfile RCFILE
                        Specify location of the webquiz rc-file
  -i, --initialise, --initialize
                        Install web components of webquiz
  -e, --edit-settings   Edit default settings for webquiz
  --settings <SETTINGS>
                        List default settings for webquiz

Installation
------------
To use WebQuiz_ you need to have a standard LaTeX_ distribution installed, such as TeXLive_, that includes TeX4ht_. In addition, you need to have Python3_ installed. As WebQuiz_ uses scalable vector graphics (SVG) you should check that all of the dependencies of dvisvgm_ are installed on your system, especially if you plan on using graphics or images.

Once the TeX components of WebQuiz_ package have been installed you can install the web components of WebQuiz_ using the following command, which needs to be run  from the command line:

> webquiz --initialise

If you want to install the web components of WebQuiz_ into a system directory then you need to run this command from an administrators account, so using `sudo` on a unix-like system. For more details about the installation and configuration of WebQuiz_ please see Section 3.2 of the WebQuiz_ manual.

Please see the manual for more details about initialising and using WebQuiz_.

Installation from the ctan zipfile
----------------------------------
On both unix-like systems (including macosx), and windows systems (using
either TeXLive or MiKTeX), you can install WebQuiz by downloading the
WebQuiz zip file from:

    http://mirrors.ctan.org/macros/latex/contrib/webquiz.zip

To install the package, unzip this file and change directory to the
webquiz/scripts subdirectory run:

> webquiz --tex-install

(or webquiz.bat --text-install on windows). This commands unpacks the webquiz
files into their standard locations in the TeX install tree to it should be
run from an administrators account, or using sudo on a unix-like system.
Roughly what this command does is the following:

- It creates a symbolic link, or equivalent, to the main WebQuiz executable,
  which is the file webquiz.py in the scripts directory
- Copies the latex directory to somewhere in the TeX search path and then
  runs `mktexlsr` so that LaTeX and WebQuiz can find these files.
- Copies the python code into the TeX scripts subdirectory
- Copies the WebQuiz doc subdirectory into the TeX doc/latex subdirectory.

If you are using MiKTeX you may need to open the MiKTeX console, go to
the Tasks menu and then rebuild the TeX filename database.

Once the files above are in place initialise WebQuiz by following the
installation instructions above.

Mainly for development purposes, there is another undocumented
command-line option for removing these files from TEXMFMAIN:

> sudo webquiz/scripts/webquiz --tex-uninstall

System requirements
-------------------

In order to work WebQuiz needs the following programs to be installed on your
system:

* An up-to-date LaTeX_ distribution, such as that provided by TeXLive_. In
  particular, you need to have TeX4ht_ and make4ht_ installed.
  Unfortunately, since TeXLive 2018 was released there have been a significat
  bunber of updates to a number of packahges that WebQuiz_ uses, including
  updates to TeX4ht_, make4ht_, tikz_ and pstricks_. For this reason, *it is
  strongly recommended that you all packages from ctan_ before using WebQuiz_*.

* python3_ As of writing python 3.7.2 is available.

* Javascript_

* If you plan to use pstricks_ with WebQuiz_, or if you want to
  compile the online manual for WebQuiz, then you need to ensure that
  ghostscript_ and dvisvgm_ are installed and properly configured on your
  system. See the WebQuiz_ manual and the dvisvgm_ documentation for more
  details

* A web server. To view online quizzes you of course need a web server. As
  described in the **Installation** section you will also need to copy of the
  WebQuiz_ components onto your web server using the command:

  > webquiz --initialise

Authors
-------
The LaTeX component of WebQuiz_ was written by Andrew Mathas and the python,
css and javascript code was written by Andrew Mathas (and Don Taylor), based on
an initial protype of Don Taylor's from 2001. Since 2004 the program has been
maintained and developed by Andrew Mathas. Although the program has changed
substantially since 2004 Don's idea of using TeX4ht_, and some of his code, is
still very much in use.

Copyright (C) 2004-2019

License
-------
GNU General Public License, Version 3, 29 June 2007

This program is free software: you can redistribute it and/or modify it
under the terms of the GNU\_General Public License
(GPL_) as published by
the Free Software Foundation, either version 3 of the License, or (at
your option) any later version.

This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General
Public License for more details.

.. _GPL:         https://www.gnu.org/licenses/gpl-3.0.en.html
.. _LaTeX:       https://www.latex-project.org/
.. _Python3:     https://www.python.org
.. _TeX4ht:      http://www.tug.org/tex4ht/
.. _TeXLive:     https://www.tug.org/texlive/
.. _WebQuiz:     https://github.com/AndrewAtLarge/WebQuiz/
.. _ctan:        https://ctan.org/
.. _dvisvgm:     https://ctan.org/pkg/dvisvgm
.. _ghostscript: https://www.ghostscript.com
.. _javascript:  https://www.javascript.com
.. _make4ht:     https://ctan.org/pkg/make4ht
.. _pstricks:    https://ctan.org/pkg/pstricks
.. _tikz:        https://ctan.org/pkg/tikz
