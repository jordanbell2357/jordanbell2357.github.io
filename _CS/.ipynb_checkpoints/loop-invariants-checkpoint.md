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

1. $$-1 \leq j < i \leq \mathrm{len}(L)$$
2. if $$0 \leq k \leq j$$ then $$L[k]=0$$
3. if $$j+1 \leq k < i$$ then $$L[k]=1$$

Suppose that $$P(i_0,j_0)$$ is true for some $$i_0$$ for which the loop executes. This means
$$i_0 < \mathrm{len}(L)$$, and so

1. $$-1 \leq j_0 < i_0 \leq \mathrm{len}(L)$$
2. if $$0 \leq k \leq j_0$$ then $$L[k]=0$$
3. if $$j_0+1 \leq k < i_0$$ then $$L[k]=1$$

Either $$L[i_0]=0$$ or $$L[i_0]=1$$.

# $$L[i_0]=0$$