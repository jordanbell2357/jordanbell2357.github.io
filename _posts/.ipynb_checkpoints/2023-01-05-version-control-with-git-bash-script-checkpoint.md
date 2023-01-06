---
layout: post
title: Version Control with Git bash script
---

<https://www.coursera.org/learn/version-control-with-git>

The Final Project is in fact not graded - I completed the course with 100% completing the quizzes and the final exam before I completed
the Final Project (and had to access the course from my Completed Courses to get to the Final Project).

Because of this, I judge it be sound to present my solution to this project. This is a step by step example for learners to imitate,
and it is longer than most worked out examples that appear at the top of many search engine results.

[![© 2018 Atlassian](/assets/images/screenshots/FP1.png)](https://www.coursera.org/learn/version-control-with-git)

[![© 2018 Atlassian](/assets/images/screenshots/FP2.png)](https://www.coursera.org/learn/version-control-with-git)

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
git checkout master
git merge release1
git tag -a -m "Merge branch 'release1'" v1.00

# I
git checkout develop
git merge release1
git commit -m "Merge branch 'release1' into develop"

# F1
git checkout feature2
git rebase master
git commit -m "feature 2 wip"

# K
git checkout -b hotfix1
echo "feature 1" >| fileA.txt
git add fileA.txt
git commit -m "fix feature 1 bug Y"

# L
git checkout master
git merge hotfix1
git tag -a -m "Merge branch 'hotfix1'" v1.01

# M
git checkout develop
git merge hotfix1
git commit -m "Merge branch 'hotfix1' into develop"

# F2
git checkout feature2
git rebase master
```

[![Commit graph. © 2018 Atlassian](/assets/images/screenshots/FP3.png)](https://www.coursera.org/learn/version-control-with-git)