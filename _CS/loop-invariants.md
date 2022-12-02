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

$$\mathtt{range}(a,b) = \{x \in \mathbb{N} : a \leq x < b\}$$

If $$a \geq b$$, then $$\mathtt{range}(a,b)=\emptyset$$.

If $$a < b$$, then $$\mathtt{range}(a,b)=\{a,\ldots,b-1\}$$, e.g. $$\mathtt{range}(0,4)=\{0,1,2,3\}$$. 

Define the predicate $$P(i,j)$$ by

1. $$-1 \leq j < i \leq \mathtt{len}(L)$$.
2. If $$x \in \mathtt{range}(0,j+1)$$, then $$L[x]=0$$.
3. If $$x \in \mathtt{range}(j+1,i)$$, then $$L[x]=1$$.

# Theorem: $$P(i,j)$$ is a correct loop invariant

# Proof

# If list $$L$$ is empty

...

# If list $$L$$ is nonempty

## Entering loop

$$P(0,-1)$$ is true because $$\mathtt{range}(0,0)=\emptyset$$.

## Executing loop

Suppose that $$P(i_0,j_0)$$ is true for some $$i_0$$ and $$j_0$$ at the start of a loop execution.
The loop executing means that $$i_0 < \mathtt{len}(L)$$, and combining this with
$$P(i_0,j_0)$$ being true gives

1. $$-1 \leq j_0 < i_0 < \mathtt{len}(L)$$.
2. If $$x \in \mathtt{range}(0,j_0+1)$$, then $$L[x]=0$$.
3. If $$x \in \mathtt{range}(j_0+1,i_0)$$, then $$L[x]=1$$.

Either $$L[i_0]=0$$ or $$L[i_0]=1$$.

### Case $$L[i_0]=0$$

Either $$j_0+1<i_0$$ or $$j_0+1=i_0$$.

#### Subcase $$j_0+1 < i_0$$

Here, $$L[j_0+1]=1$$.

- $$j_1=j_0+1$$.
- $$L[i_0]=0$$ and $$L[j_1]=1$$ are swapped: now $$L[i_0]=1$$ and $$L[j_1]=0$$.
- $$i_1=i_0+1$$.

We want to show that $$P(i_1,j_1)$$ is true, namely

1. $$-1 \leq j_1 < i_1 \leq \mathtt{len}(L)$$.
2. If $$x \in \mathtt{range}(0,j_1+1)$$, then $$L[x]=0$$.
3. If $$x \in \mathtt{range}(j_1+1,i_1)$$, then $$L[x]=1$$.

Using $$-1 \leq j_0$$ and $$j_1=j_0+1$$, we get $$-1 \leq j_1$$.

Using $$j_0<i_0$$ we get $$j_0+1<i_0+1$$ and so $$j_1<i_1$$.

Using $$i_0< \mathtt{len}(L)$$ and $$i_1=i_0+1$$ we get $$i_1 \leq \mathtt{len}(L)$$. Hence 

$$-1 \leq j_1 < i_1 \leq \mathtt{len}(L)$$

If $$x \in \mathtt{range}(0,j_0+1)$$, then $$L[x]=0$$. And $$L[j_1]=0$$. Hence if $$x \in
\mathtt{range}(0,j_1+1)$$, then $$L[x]=0$$.

Using (3) and $$j_1 \geq j_0$$, if $$x \in \mathtt{range}(j_1+1,i_0)$$, then $$L[x]=1$$.
$$L[i_0]=1$$, thus if $$x \in \mathtt{range}(j_1+1,i_1)$$, then $$L[x]=1$$.

We have established in this case that $$P(i_1,j_1)$$ is true.

#### Subcase $$j_0+1 = i_0$$

Here, $$L[j_0+1]=0$$.

- $$j_1=j_0+1$$; so $$j_1=i_0$$.
- $$L[i_0]=0$$ and $$L[j_1]=0$$ are swapped: now $$L[i_0]=0$$ and $$L[j_1]=0$$.
- $$i_1=i_0+1$$.

Using $$-1 \leq j_0$$ and $$j_0 \leq j_1$$ we get $$-1 \leq j_1$$.

Using $$j_1=i_0$$ and $$i_1=i_0+1$$, we get $$j_1 < i_1$$.

Using $$i_0< \mathtt{len}(L)$$ and $$i_1=i_0+1$$ we get $$i_1 \leq \mathtt{len}(L)$$. Hence 

$$-1 \leq j_1 < i_1 \leq \mathtt{len}(L)$$

If $$x \in \mathtt{range}(0,j_0+1)$$, then $$L[x]=0$$. And $$L[j_1]=0$$. Hence if $$x \in
\mathtt{range}(0,j_1+1)$$, then $$L[x]=0$$.

Since in this case $$j_1+1=i_1$$, here $$\mathtt{range}(j_1+1,i_1)=\emptyset$$. Thus it is vacuously
true that if $$x \in \mathtt{range}(j_1+1,i_1)$$, then $$L[x]=1$$.

We have established in this case that $$P(i_1,j_1)$$ is true.

### Case $$L[i_0]=1$$

- $$j_1=j_0$$.
- $$L[i_0]=1$$ and $$L[j_1]=0$$ are swapped: now $$L[i_0]=0$$ and $$L[j_1]=1$$.
- $$i_1=i_0+1$$.

Using $$-1 \leq j_0$$ and $$j_1=j_0$$, we get $$-1 \leq j_1$$. Using $$j_0<i_0$$, we get
$$j_1 = j_0 < i_0 < i_0+1 = i_1$$ so $$j_1<i_1$$.
Using $$i_0< \mathtt{len}(L)$$ and $$i_1=i_0+1$$ we get $$i_1 \leq \mathtt{len}(L)$$. Hence

$$-1 \leq j_1 < i_1 \leq \mathtt{len}(L)$$

If $$x \in \mathtt{range}(0,j_0+1)$$, then $$L[x]=0$$. But $$j_1=j_0$$. Hence if $$x \in
\mathtt{range}(0,j_1+1)$$, then $$L[x]=0$$.

If $$x \in \mathtt{range}(j_0+1,i_0)$$, then $$L[x]=1$$. Using $$j_1=j_0$$, if $$x \in \mathtt{range}(j_1+1,i_0)$$ then
$$L[x]=1$$. And $$L[i_0]=1$$, so if $$x \in \mathtt{range}(j_1+1,i_1)$$ then $$L[x]=1$$.

We have established in this case that $$P(i_1,j_1)$$ is true.

Therefore we have shown that if $$P(i_0,j_0)$$ is true for $$i_0,j_0$$ at the beginning of the loop execution,
then $$P(i_1,j_1)$$ is true for $$i_1,j_1$$ at the end of the loop execution.

## Exiting loop

Suppose that $$P(i,j)$$ is true when the loop exits. Because $$i \leq \mathtt{len}(L)$$, when the loop exits it is the case
that $$i = \mathtt{len}(L)$$.
Thus $$P(i,j)$$ being true means

1. $$-1 \leq j < \mathtt{len}(L)$$.
2. If $$x \in \mathtt{range}(0,j+1)$$, then $$L[x]=0$$.
3. If $$x \in \mathtt{range}(j+1,\mathtt{len}(L))$$, then $$L[x]=1$$.

It follows from this that $$L$$ is sorted in non-descending order.

$$j \geq 0$$ if and only if then there is at least one $$x$$ such that $$L[x]=0$$.

Thus when the loop exits, the postcondition is true.

This completes the proof that $$P(i,j)$$ is a correct loop invariant for the given code. 

## ∎