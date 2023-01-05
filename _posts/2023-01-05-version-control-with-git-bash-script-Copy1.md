---
layout: post
title: Version Control with Git bash script
---

The Final Project is in fact not graded - I completed the course with 100% completing the quizzes and the final exam before I completed
the Final Project (and had to access the course from my Completed Courses to get to the Final Project).
Because of this, I've judged it is decent to present my solution to this project. This is a step by step example for learners to imitate, and it is longer than most worked out examples that appear search engine results.

<https://www.coursera.org/learn/version-control-with-git>

[![FP1](/assets/images/screenshots/FP1.png)](https://www.coursera.org/learn/version-control-with-git)

![FP2](/assets/images/screenshots/FP2.png)

Copy below and save as file X.sh file; then execute bash X.sh.

At this time: Copy up to and including merge H.

```bash
#!/bin/bash

# A
git init FinalProject
cd FinalProject
echo "# Readme v1.00" > README.md
git add README.md
git commit -m "add README.md"

# B
git checkout -b develop
touch fileA.txt
git add fileA.txt
git commit -m "add fileA.txt"

# C
git checkout -b feature1
echo "feature 1 wip" >| fileA.txt
git add fileA.txt
git commit -m "feature 1 wip"

# D
echo "feature 1 with 2 bugs" >| fileA.txt
git add fileA.txt
git commit -m "add feature 1"

# E
git checkout develop
git merge feature1
git commit -m "Merge branch 'feature1' into develop"

# F
git checkout -b feature2
echo "feature 2 wip" >> fileA.txt
git add fileA.txt
git commit -m "feature 2 wip"

# G
git checkout -b release1
echo "feature 1 with 1 bug" >| fileA.txt
git add fileA.txt
git commit -m "fix feature 1 bug X"

# H
# this block is broken
git checkout master
git merge release1
git commit -m "Merge branch 'release1'"

# I
git checkout develop
git merge release1
git commit -m "Merge branch 'release1' into develop"

# F1
git checkout feature2
git rebase master
git commit "feature 2 wip"

# K
git checkout -b hotfix1
echo "feature 1" >| fileA.txt
git add fileA.txt
git commit -m "fix feature 1 bug Y"

# L
git checkout master
git merge hotfix1
git commit -m "Merge branch 'hotfix1'"

# M
git activate develop
git merge hotfix1
git commit -m "Merge branch 'hotfix1' into develop"

# F2
git checkout feature2
git rebase master
```