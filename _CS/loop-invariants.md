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
      L is sorted (non-descending)
      Returns True if 0 in L and False otherwise
    ''' 
    i = 0
    j = -1
    while i < len(L):
        if L[i] == 0:
            j += 1
            L[i], L[j] = L[j], L[i]
        i += 1
```

Let $$\mathbb{N}$$ be the set of nonnegative integers. For $$a,b \in \mathbb{N}$$, define 

$$\mathrm{range}(a,b) = \{x \in \mathbb{N} : a \leq x < b\}$$

If $$a \geq b$$, then $$\mathrm{range}(a,b)=\emptyset$$.

If $$a < b$$, then $$\mathrm{range}(a,b)=\{a,\ldots,b-1\}$$, e.g. $$\mathrm{range}(0,4)=\{0,1,2,3\}$$. 

Define the predicate $$P(i,j)$$ by

1. $$-1 \leq j < i \leq \mathrm{len}(L)$$.
2. If $$x \in \mathrm{range}(0,j+1)$$, then $$L[x]=0$$.
3. If $$x \in \mathrm{range}(j+1,i)$$, then $$L[x]=1$$.

Suppose that $$P(i_0,j_0)$$ is true for some $$i_0$$ and $$j_0$$ at the start of a loop iteration that executes.
The loop executing means that $$i_0 < \mathrm{len}(L)$$, and combining this with
$$P(i_0,j_0)$$ being true gives

1. $$-1 \leq j_0 < i_0 < \mathrm{len}(L)$$.
2. If $$x \in \mathrm{range}(0,j_0+1)$$, then $$L[x]=0$$.
3. If $$x \in \mathrm{range}(j_0+1,i_0)$$, then $$L[x]=1$$.

Either $$L[i_0]=0$$ or $$L[i_0]=1$$.

#### $$L[i_0]=0$$

Either $$j_0+1<i_0$$ or $$j_0+1=i_0$$.

##### $$j_0+1 < i_0$$

Here, $$L[j_0+1]=1$$.

- $$j_1=j_0+1$$.
- $$L[i_0]=0$$ and $$L[j_1]=1$$ are swapped: now $$L[i_0]=1$$ and $$L[j_1]=0$$.
- $$i_1=i_0+1$$.

We want to show that $$P(i_1,j_1)$$ is true, namely

1. $$-1 \leq j_1 < i_1 \leq \mathrm{len}(L)$$.
2. If $$x \in \mathrm{range}(0,j_1+1)$$, then $$L[x]=0$$.
3. If $$x \in \mathrm{range}(j_1+1,i_1)$$, then $$L[x]=1$$.

Using $$-1 \leq j_0$$ and $$j_1=j_0+1$$, we get $$-1 \leq j_1$$.

Using $$j_0<i_0$$ we get $$j_0+1<i_0+1$$ and so $$j_1<i_1$$.

Using $$i_0< \mathrm{len}(L)$$ and $$i_1=i_0+1$$ we get $$i_1 \leq \mathrm{len}(L)$$. Hence 

$$-1 \leq j_1 < i_1 \leq \mathrm{len}(L)$$

If $$x \in \mathrm{range}(0,j_0+1)$$, then $$L[x]=0$$. And $$L[j_1]=0$$. Hence if $$x \in
\mathrm{range}(0,j_1+1)$$, then $$L[x]=0$$.

Using (3) and $$j_1 \geq j_0$$, if $$x \in \mathrm{range}(j_1+1,i_0)$$, then $$L[x]=1$$.
$$L[i_0]=1$$, thus if $$x \in \mathrm{range}(j_1+1,i_1)$$, then $$L[x]=1$$.

We have established in this case that $$P(i_1,j_1)$$ is true.

##### $$j_0+1 = i_0$$

Here, $$L[j_0+1]=0$$.

- $$j_1=j_0+1$$; so $$j_1=i_0$$.
- $$L[i_0]=0$$ and $$L[j_1]=0$$ are swapped: now $$L[i_0]=0$$ and $$L[j_1]=0$$.
- $$i_1=i_0+1$$.

Using $$-1 \leq j_0$$ and $$j_0 \leq j_1$$ we get $$-1 \leq j_1$$.

Using $$j_1=i_0$$ and $$i_1=i_0+1$$, we get $$j_1 < i_1$$.

Using $$i_0< \mathrm{len}(L)$$ and $$i_1=i_0+1$$ we get $$i_1 \leq \mathrm{len}(L)$$. Hence 

$$-1 \leq j_1 < i_1 \leq \mathrm{len}(L)$$

If $$x \in \mathrm{range}(0,j_0+1)$$, then $$L[x]=0$$. And $$L[j_1]=0$$. Hence if $$x \in
\mathrm{range}(0,j_1+1)$$, then $$L[x]=0$$.

Since in this case $$j_1+1=i_1$$, here $$\mathrm{range}(j_1+1,i_1)=\emptyset$$. Thus it is vacuously
true that if $$x \in \mathrm{range}(j_1+1,i_1)$$, then $$L[x]=1$$.

We have established in this case that $$P(i_1,j_1)$$ is true.


#### $$L[i_0]=1$$

Using $$-1 \leq j_0$$ and $$j_1=j_0$$, we get $$-1 \leq j_1$$. Using $$j_0<i_0$$, we get
$$j_1 = j_0 < i_0 < i_0+1 = i_1$$ so $$j_1<i_1$$.
Using $$i_0< \mathrm{len}(L)$$ and $$i_1=i_0+1$$ we get $$i_1 \leq \mathrm{len}(L)$$. Hence

$$-1 \leq j_1 < i_1 \leq \mathrm{len}(L)$$

...