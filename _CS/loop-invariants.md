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
    ''' 
    i = 0
    j = -1
    while i < len(L):
        if L[i] == 0:
            j += 1
            L[i], L[j] = L[j], L[i]
        i += 1
```

Define the predicate $$P(i,j)$$ by

1. $$-1 \leq j < i \leq \mathrm{len}(L)$$.
2. If $$0 \leq k \leq j$$ then $$L[k]=0$$.
3. If $$j+1 \leq k < i$$ then $$L[k]=1$$.

Suppose that $$P(i_0,j_0)$$ is true for some $$i_0$$ for which the loop executes. This means
$$i_0 < \mathrm{len}(L)$$, and thus

1. $$-1 \leq j_0 < i_0 < \mathrm{len}(L)$$.
2. If $$0 \leq k \leq j_0$$ then $$L[k]=0$$.
3. If $$j_0+1 \leq k < i_0$$ then $$L[k]=1$$.

Either $$L[i_0]=0$$ or $$L[i_0]=1$$.

#### $$L[i_0]=0$$

- $$j_1=j_0+1$$.
- $$L[i_0]$$ and $$L[j_1]$$ are swapped.
- $$i_1=i_0+1$$.

We want to show that $$P(i_1,j_1)$$ is true, namely

1. $$-1 \leq j_1 < i_1 \leq \mathrm{len}(L)$$.
2. If $$0 \leq k \leq j_1$$ then $$L[k]=0$$.
3. If $$j_1+1 \leq k < i_1$$ then $$L[k]=1$$.

Using $$-1 \leq j_0$$ and $$j_1=j_0+1$$, we get $$-1 \leq j_1$$. Using $$j_0<i_0$$ we get $$j_0+1<i_0+1$$ and so $$j_1<i_1$$.
Using $$i_0< \mathrm{len}(L)$$ and $$i_1=i_0+1$$ we get $$i_1 \leq \mathrm{len}(L)$$. Hence 

$$-1 \leq j_1 < i_1 \leq \mathrm{len}(L)$$

If $$0 \leq k \leq j_0$$, then $$L[k]=0$$. And $$L[j_1]=0$$. Hence if $$0 \leq k \leq j_1$$ then
$$L[k]=0$$.

If $$j_1 \leq k < i_0$$ then $$L[k]=1$$. And $$L[i_0]=1$$. So if $$j_1 \leq k < i_1$$ then $$L[k]=0$$.

We have established in this case that $$P(i_1,j_1)$$ is true.

#### $$L[i_0]=1$$

Using $$-1 \leq j_0$$ and $$j_1=j_0$$, we get $$-1 \leq j_1$$. Using $$j_0<i_0$$, we get
$$j_1 = j_0 < i_0 < i_0+1 = i_1$$ so $$j_1<i_1$$.
Using $$i_0< \mathrm{len}(L)$$ and $$i_1=i_0+1$$ we get $$i_1 \leq \mathrm{len}(L)$$. Hence

$$-1 \leq j_1 < i_1 \leq \mathrm{len}(L)$$