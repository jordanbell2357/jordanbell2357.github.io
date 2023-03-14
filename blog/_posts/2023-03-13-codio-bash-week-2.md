---
layout: post
title: My favorite material from Codio's Bash Week 2 on Coursera 
---

[Bash Scripting and System Configuration \| Codio](https://www.coursera.org/learn/codio-bash-scripting-and-system-configuration)

# Glob Expressions

> List .png files beginning with file followed by something that’s NOT a lowercase letter, then a number.

```bash
ls file[![:lower:]][[:digit:]].png
```

# Extended globbing

> The + character allows us to match one or more occurrences of the given patterns.

```bash
ls file3c+(.txt|.png)
```

> We can use a for loop to cycle through all of the filenames and display each filename after removing everything `#*` that comes before the first.

```bash
for filename in *; do echo ${filename#*.}; done | sort -u
```

# grep

> Locate lines with 1 or more occurrence of the word my.

```bash
grep -E 'my+' jabberwocky
```

> Return lines containing exactly 1 or 2 digits.

```bash
grep -E '[[:digit:]]{1,2}' jabberwocky
```

> Let's use grep to search for lines that contain ll inside this file, remembering to include -E to enable extended regexes.

```bash
grep -E '(ll)' jabberwocky
```

> Only return the portion of the line that matches this pattern

```bash
grep -E -o '(.u.+u.)' jabberwocky
```

# sed

> Let’s print all of the lines in the file greeneggs.txt that contain the pattern Sam using sed

```bash
sed -n -E '/Sam/p' greeneggs.txt
```

> We can limit this to only match lines beginning with Sam by anchoring the pattern with a ^ at the beginning.

```bash
sed -n -E '/^Sam/p' greeneggs.txt
```

> Let’s change every instance of the word green to the word old using substitution and redirect the result to a file called oldeggs.

```bash
sed -E 's/green/old/g' greeneggs.txt > oldeggs
```

> Run the command below in the terminal to match the first three digits in each line and replace them with the same digits, wrapped in parenthesis ()

```bash
sed -E 's/[0-9]{3}/(&)/' data.csv
```

> We can use backreferences to modify this approach and add a hyphen between the remaining three and four characters.
>
> Let's create three backreference groups by wrapping our patterns to match in parenthesis ().
>
> `\1`: 3-digit Area Code: `([0-9]{3})`
>
> `\2`: 3-digit Exchange Code: `([0-9]{3})`
>
> `\3`: 4-digit Line Number: `([0-9]{4})`

```bash
sed -E 's/([0-9]{3})([0-9]{3})([0-9]{4})/(\1) \2-\3/' data.csv
```

> Inserts a \# at the beginning of lines 3−10 inside the file

```bash
sed '3,10s/^/#/' flowers.txt
```

# awk

> Find each line in the file that contains the pattern Male, and print the 1st and 4th columns of data for each match.

```bash
awk -F"," '/Male/{print $1,$4}' people.csv
```

> For example, we can check the column holding first names `$2` and match all first names that begin and end with A with any number
> of any type of characters in between.
>
> Once we locate these matches, we can print only the first name, last name, and gender columns for these matches.

```bash
awk -F"," '$2 ~ /^A.*a$/{print $2,$3,$5}' people.csv
```

> Find all of the lines belonging to Discover card users, and display each card number to the terminal.

<samp>
Discover, Chris Howe, 6543435725654171, 08/31, CVC: 255
American Express, Kathleen Ford, 341584729447996, 08/31, CID: 9885
</samp>

```bash
awk -F"," '/Discover/{print $3}' credit.csv
```

```bash
#!/binbash

while read line
do

  if [[ $line =~ .*[Dd]iscover.* ]];
  then
    if [[ $line =~ [0-9]{16} ]];
    then
      echo ${BASH_REMATCH[0]}
    fi
  fi
done < credit.csv
```

> Create a command that displays a complete list of valid email addresses in the file signups.txt
>
> Between 1 and 16 numbers, uppercase or lowercase letters, periods, or underscores
>
> An \@ sign
>
> A domain with any number of lowercase letters, (like gmail, hotmail, etc.)
>
> A period .
>
> top level domain of .com, .org, or .net

```bash
grep -E '([[:alnum:]]|\.|\_)+(@)([[:alnum:]]|\.|\_)+(\.com|\.org|\.net)$' signups.txt | grep -E '([[:alnum:]]|\.|\_\@){1,16}'
```

```bash
#!/bin/bash

grep -E '(^[A-Za-z0-9_\.]{1,16})@[[:lower:]]+\.(com|org|net)' signups.txt
```