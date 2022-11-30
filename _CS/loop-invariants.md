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
      L is sorted (ascending)
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

Define the predicate $$P(i,j)$$ by

1. $$-1 \leq j < i \leq \len(L)$$
2. if $$0 \leq k \leq j$$ then $$L[k]=0$$
3. if $$j+1 \leq k < i$$ then $$L[k]=1$$