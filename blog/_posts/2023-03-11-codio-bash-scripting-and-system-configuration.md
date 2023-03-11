---
layout: post
title: My favorite material from Codio's Bash Scripting and System Configuration on Coursera 
---

[Bash Scripting and System Configuration \| Codio](https://www.coursera.org/learn/codio-bash-scripting-and-system-configuration)

# <<

```bash
cat << ThisIsTheEnd
Is this the real life?
Is this just fantasy?
Caught in a landslide,
No escape from reality
ThisIsTheEnd
```

# Brace Expansion

> The following command displays numbers 0-20 in intervals of 2

```bash
echo {0..20..2}
```

```bash
echo {earth,wind,fire}_{1..3}
```

# Parameter Expansion

```bash
book="Where the Sidewalk Ends" 
```

> Let’s replace all e's with ampersands `&` using two forward slashes `//`.

```bash
echo ${book//e/&}
```

# Arithmetic Expansion

