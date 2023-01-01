---
layout: page
title: Bubblesort loop example
---

```python
def bubblesort(L):
    '''
    Pre: L is a list of numbers
    Post: L is sorted
    '''
    k = 0
    while k < len(L):
      i = 0
      while i < len(L) - k:
        if L[i] > L[i+1]:
          swap L[i] and L[i+1]
        i += 1
      k +=1
```

<script src="/assets/js/jquery.min.js"></script>
<script src="/assets/js/jquery-ui.min.js"></script>
<script src="/assets/js/jquery.transit.js"></script>
<script src="/assets/js/raphael.js"></script>
<script src="/assets/js/JSAV.js"></script>

<script>
  var jsav = new JSAV("av");
  var arr = [1, 2, 3, 4, 5, 6, 7, 8];

  jsav.label("Indexed Array");
  var arr4 = jsav.ds.array(arr, {indexed: true});
  arr4.highlight(2);
  arr4.css(4, {"background-color": "aqua", "color": "rgb(150, 55, 50)"});
  arr4.layout();
  
  jsav.displayInit();
  jsav.recorded(); // done recording changes, will rewind



  $(".jsavtreenode").live("hover", function() {
    //console.log($(this).text(), $(this).offset().left, $(this).offset().top);
  });
  $("path").live("hover", function() {
    //console.log($(this).attr("d"));
  });
</script>