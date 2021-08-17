---
#
# By default, content added below the "---" mark will appear in the home page
# between the top bar and the list of recent posts.
# To change the home page layout, edit the _layouts/home.html file.
# See: https://jekyllrb.com/docs/themes/#overriding-theme-defaults
#
layout: home
---


$("script[type='math/tex']").replaceWith(
  function(){
    var tex = $(this).text();
    return "<span class=\"inline-equation\">" + 
           katex.renderToString(tex) +
           "</span>";
});

$("script[type='math/tex; mode=display']").replaceWith(
  function(){
    var tex = $(this).text();
    return "<div class=\"equation\">" + 
           katex.renderToString("\\displaystyle "+tex) +
           "</div>";
});

[KaTeX testing](/KaTeX) / [KaTeX page](https://katex.org/)