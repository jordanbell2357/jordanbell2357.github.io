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

```bash
#!/bin/bash
echo ~+
echo {0..100..5}
mkdir {png,jpg,pdf}_files{1..3}
touch {png,jpg,pdf}_files{1..3}/image_{1..5}
rm {png,jpg,pdf}_files{1..3}/image_{1..5}
rmdir {png,jpg,pdf}_files{1..3}
echo "6 times 3 is equal to: $(( 6 * 3 ))"
message="impossible work!"
echo ${message:2}
```

# Command Substitution

```bash
echo "Today is $(date)."
```

# `[]`

```bash
ls doc[1-5][a-e].png
```

```bash
ls doc[[:digit:]][[:lower:]].txt
```

# File globbing

> Write a command using a named character class to list all of the files that contain a number.

```bash
ls *[[:digit:]]*
```
# printf

```bash
echo "The answers are: $(( 8 - 5)) and $(( 15 / 3 ))"
```

```bash
printf "The answers are: %d and %d\n" $(( 8 - 5)) $(( 15 / 3 ))
```

```bash
printf "%(%Y-%m-%d %H:%M:%S)T\n"
```

```bash
echo "System report for $HOSTNAME"
printf "Report Date:\t%(%Y-%m-%d)T\n"
printf "Bash Version:\t%s\n" $BASH_VERSION
printf "Kernel Release:\t%s\n" $(uname -r)
printf "Available Storage:\t%s\n" $(df -h)
printf "Available Memory:\t%s\n" $(free -h)
printf "Files in Directory:\t%s\n" $(ls | wc -l)
```

# Test

```bash
[ "green" = "green" ]; echo $?
```

<samp>0</samp>

```bash
[ 7 -lt 15 ]; echo $?
```

<samp>0</samp>

```bash
[ 7 -gt 15 ]; echo $?
```

<samp>1</samp>

# Arrays

Implicit

```bash
instruments=("piano" "flute" "guitar" "oboe")
```

Explicit

```bash
declare -a instruments=("piano" "flute" "guitar" "oboe")
```

```bash
echo ${instruments[1]}
```

<samp>flute</samp>

```bash
echo ${instruments[@]}
```

```bash
for i in {0..6}; do echo "$i: ${instruments[$i]}"; done
```

# Associative Arrays

```bash
declare -A student
student[name]=Rodney
student["area of study"]="Systems Administration"
echo ${student[name]} is majoring in ${student["area of study"]}.
```

<samp>Rodney is majoring in Systems Administration.</samp>

# if

```bash
declare -i a=3

if [[ $a -gt 4 ]]; then
        echo "$a is greater than 4."
else    
        echo "$a is not greater than 4."
fi
```

```bash
declare -i a=3

if (( "$a" > 4 )); then
        echo "$a is greater than 4."
else    
        echo "$a is not greater than 4."
fi
```

# case

> This statement checks the country entered by the user and responds with the commands nested within that particular criteria.

```bash
#!/bin/bash

echo -n "Enter the name of a country: "
read COUNTRY

echo -n "The official language of $COUNTRY is "

case $COUNTRY in

  Lithuania)
    echo -n "Lithuanian"
    ;;

  Romania | Moldova)
    echo -n "Romanian"
    ;;

  Italy | "San Marino" | Switzerland | "Vatican City")
    echo -n "Italian"
    ;;

  *)
    echo -n "unknown"
    ;;
esac
```

