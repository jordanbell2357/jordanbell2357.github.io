---
layout: post
title: Game theory using Sage
---

[Game Theory \| Sage Reference Manual](https://doc.sagemath.org/html/en/reference/game_theory/index.html)

[Sage Cell Server](https://sagecell.sagemath.org/?z=eJzLzCtJTU8tik8rzUsuyczPU7BVqNbQtFIw0OHlUsACNAx1gLKGuGSN8Moa45U11FEAazfGowBsgglu2yEKTPFaAVVTy8uVCfV8emJuKtDjzvn5BalFiSWZZanuQBGNTLSw0UTVoZdZHF9cCtKRkpIJ0qShCQAEYEYd&lang=sage&interacts=eJyLjgUAARUAuQ==)

```
integer_function = {(): 0,
                    (1,): 1,
                    (2,): 1,
                    (3,): 1,
                    (1, 2,): 3,
                    (1, 3,): 4,
                    (2, 3,): 5,
                    (1, 2, 3,): 5}
integer_game = CooperativeGame(integer_function)
integer_game.is_superadditive()
```

<samp>False</samp>

[Sage Cell Server](https://sagecell.sagemath.org/?z=eJzLzCtJTU8tik8rzUsuyczPU7BVqNbQtFIw0OHlUsACNAx1gLKGuGSN8Moa45U11FEAazfGowBsgglu2yEKTPFaAVFjXsvLlQn1fHpibirQ4875-QWpRYklmWWp7kARjUy0sNFE1aGXWRxfXArSkZKSCdKkoQkABQpGHw==&lang=sage&interacts=eJyLjgUAARUAuQ==)

```
integer_function = {(): 0,
                    (1,): 1,
                    (2,): 1,
                    (3,): 1,
                    (1, 2,): 3,
                    (1, 3,): 4,
                    (2, 3,): 5,
                    (1, 2, 3,): 7}
integer_game = CooperativeGame(integer_function)
integer_game.is_superadditive()
```

<samp>True</samp>

[Sage Cell Server](https://sagecell.sagemath.org/?z=eJzLzCtJTU8tik8rzUsuyczPU7BVqNbQtFIw0OHlUsACNAx18MkagWSNcOtVgCio5eXKhFqcnpibCrTUOT-_ILUosSSzLNUdKKKRieYuTVQdepnF8cWlIB0pKZkgTRqaAMibNCM=&lang=sage&interacts=eJyLjgUAARUAuQ==)

```
integer_function = {(): 0,
                    (1,): 0,
                    (2,): 2,
                    (1, 2,): 2}
integer_game = CooperativeGame(integer_function)
integer_game.is_superadditive()
```

<samp>True</samp>

[Sage Cell Server](https://sagecell.sagemath.org/?z=eJzLzCtJTU8tik8rzUsuyczPU7BVqNbQtFIw0OHlUsACNAx18MkagWSNcOtVgCio5eXKhFqcnpibCrTUOT-_ILUosSSzLNUdKKKRieYuTVQdesUZiQU5qZXxZYk5pakamgArxjLh&lang=sage&interacts=eJyLjgUAARUAuQ==)

```
integer_function = {(): 0,
                    (1,): 0,
                    (2,): 2,
                    (1, 2,): 2}
integer_game = CooperativeGame(integer_function)
integer_game.shapley_value()
```

<samp>{1: 0, 2: 2}</samp>


[Sage Cell Server](https://sagecell.sagemath.org/?z=eJzLSS0pSS2KTyvNSy7JzM9TsFWo1tC0UjDQ4eVSwAQa6s7qOvikww0JyBvhlwcarwAzxBi_IiP8ikCGKBBvH1ypSS0vVw4kUNITc1OBAeKcn1-QWpRYklmW6g4U0chBDTJNFPV6xRmJBTmplfFliTmlqRqaAG1jSRk=&lang=sage&interacts=eJyLjgUAARUAuQ==)

```
letter_function = {(): 0,
                   ('C',): 0,
                   ('W1',): 0,
                   ('W2',): 0,
                   ('C', 'W1',): 3,
                   ('C', 'W2',): 3,
                   ('W1', 'W2',): 0,
                   ('C', 'W1', 'W2',): 4}
letter_game = CooperativeGame(letter_function)
letter_game.shapley_value()
```

<samp>{'C': 7/3, 'W1': 5/6, 'W2': 5/6}</samp>