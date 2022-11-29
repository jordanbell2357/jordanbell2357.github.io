---
layout: page
title: Loop invariants
---

```python
def sort(L):
    '''
    Precondition:
      L is a list of 0s and 1s
    Postcondition:
      L is sorted
      Returns True if L contains a 0 and False otherwise
    ''' 
    i = 0
    j = -1
    while i < len(L):
        if L[i] == 0:
            j += 1
            L[i], L[j] = L[j], L[i]
        i += 1
    return j >= 0
```