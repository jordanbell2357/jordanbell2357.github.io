---
layout: post
title: My favorite material from Codio's Bash Week 1 on Coursera 
---

[Bash Scripting and System Configuration \| Codio](https://www.coursera.org/learn/codio-bash-scripting-and-system-configuration)

# \<\<

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

# \[\]

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

# test

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

**Implicit**

```bash
instruments=("piano" "flute" "guitar" "oboe")
```

**Explicit**

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

```bash
#!/bin/bash

even=(2 4 6 8 10)
odd=(1 3 5 7 9)

[ ${even[2]} -gt ${odd[2]} ]; echo $?
[[ $((${even[4]} + ${odd[3]})) -gt 10 ]] && echo "This is larger than 10"
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

# elif

```bash
#!/bin/bash

echo Enter major or minor:
read scaleType

if [[ $scaleType == 'major' ]]
then
  echo "Major scales sound bright and hopeful"
elif [[ $scaleType == 'minor' ]]
then
  echo "Minor scales sound sad and mysterious"
else
  echo "I'm sorry, I don't understand"
fi

echo "What is your favorite genre of music?"
read genre

case $genre in

  pop | Pop)
    echo "You might enjoy Ariana Grande"
    ;;

  classical | Classical)
    echo "You might enjoy Vivaldi"
    ;;

  "hip hop" | "Hip Hop" | hiphop | rap)
    echo "You might enjoy Drake"
    ;;

  dance | Dance)
    echo "You might enjoy UMEK"
    ;;

  country | Country)
    echo "You might enjoy Jason Aldean"
    ;;

  *)
    echo "Great Choice!"
    ;;
esac
```

# for

```bash
for i in 1 2 3 4 5
do
    echo $i
done
```

```bash
for i in 1 2 3 4 5; do echo $i; done
```

> Let’s create an array called `favMusicals` and write a for loop that displays each array item’s value to the terminal.

```bash
declare -a favMusicals=('Hamilton' 'The Lion King' 'Grease' 'West Side Story' 'Rent')

for musical in "${favMusicals[@]}"
do
  echo "I love the musical: $musical"
done
```

# while

```bash
declare -i n=0
while (( n < 10 ))
do
       echo "n is equal to: $n"
       (( n++ ))
done
```

# until

```bash
declare -i m=0
until (( m == 10 ))
do
        echo "m is equal to: $m"
        (( m++ ))
        sleep 1
done
```

# Functions

```bash
briefing() {
  echo "Good Morning, $1!"  # $1 represents the first variable passed to the function
  echo "The weather today will be $2."  # $2 is the second variable passed to the function
}

echo "It's time to get ready for your day..."

briefing Tony sunny. # Here, we call the briefing function, passing Tony as variable 1 and sunny as variable 2
```

```bash
declare -A BPM

BPM=( [Lento]=40 [Largo]=45 [Adagio]=55 [Andante]=75, [Moderato]=95, [Vivace]=135, [Presto]=175 )

for KEY in "${!BPM[@]}"; do echo "Key: $KEY"; echo "Value: ${BPM[$KEY]}"; echo; done

currentTempo=0
while [ $currentTempo -le 40 ]
do
    echo "$currentTempo BPM is too slow to play"
    (( currentTempo+=5 ))
done
```

# Arguments

```bash
#!/bin/bash
for i in $@
do
    echo $i
done
echo "There were $# arguments."
```

# Options

```bash
#!/bin/bash
while getopts u:p: option; do
        case ${option} in
                u) user=$OPTARG;;
                p) pass=$OPTARG;;
        esac
done

echo "user:$user / pass: $pass"
```

```bash
#!/bin/bash
while getopts :u:p:ab option; do
        case $option in
                u) user=$OPTARG;;
                p) pass=$OPTARG;;
                a) echo "got the A flag";;
                b) echo "got the B flag";;
                ?) echo "I don't know what $OPTARG is!";;
        esac
done

echo "user:$user / pass: $pass"
```

```bash
while getopts u:p:s: option; do
        case ${option} in
                u) user=$OPTARG;;
                p) pass=$OPTARG;;
                s) skey=$OPTARG;;
        esac
done

echo "Username: $user"
echo "Password: $pass"
echo "Security Key: $skey"
```

# read

```bash
#!/bin/bash

echo "What is your name?"
read name

echo "What is your password?"
read -s pass

read -p "What's your favorite animal? " animal

echo "Name: $name, Password: $pass, Fave Animal: $animal"

echo "Which animal"
select animal in "cat" "dog" "bird" "fish"

do
    echo "You selected $animal!"
    break
done
```

```bash
#!/bin/bash

echo "Which animal"
select animal in "cat" "dog" "quit"
do
       case $animal in 
               cat) echo "Cats like to sleep.";;
               dog) echo "Dogs like to play catch.";;
               quit) break;;
               *) echo "I'm not sure what that is.";;
        esac
done
```

# read -i

```bash
#!/usr/bin/env bash

read -ep "What is your pet's name? " -i "Pabu" petname

echo $petname

if (($# < 3 )); then
    echo "This command takes three arguments:"
    echo "petname, pettype, and petbreed."

else

    echo "Pet Name: $1"
    echo "Pet Type: $2"
    echo "Pet Breed: $3"

fi
```

# \[\[ -z \]\]

```bash
#!/usr/bin/env bash

read -p "What would you like for dinner? [Chicken Noodle Soup] " dinner

while [[ -z $dinner ]]
do
    dinner="Chicken Noodle Soup"
done

echo "You will be having $dinner$ for dinner!"
```

```bash
#!/usr/bin/env bash

read -p "Please enter a 5-digit zip code: [nnnnn]" zipcode

until [[ $zipcode =~ [0-9]{5} ]]; do
    read -p "Still waiting on that zip code! [nnnnn] " zipcode
done

echo "Your zip code is $zipcode
```

# tr

```bash
echo "dog dOg" | tr "[a-z]" "[A-Z]"
```

<samp>DOG DOG</samp>

```bash
echo "dog dOg" | tr "[:lower:]" "[:upper:]"
```

<samp>DOG DOG</samp>

```bash
echo "dog dOg" | tr [:space:] '\t'
```

# awk

> Print all of the lines of data

```bash
awk '{print}' students.txt
```

> Print all of the lines in the file students.txt that match the pattern freshman using the command below.

```bash
awk '/freshman/ {print}' students.txt 
```

# cut

> Let’s use cut to print the first, third, and fifth characters from each line of the file pres_first.txt.

```bash
cut -c 1,3,5 pres_first.txt
```

> Let’s print characters 2-6 from each line of pres_last.txt.

```bash
cut -c 2-6 pres_last.txt
```

# tee

> We can append information to one or more files with the -a option.

```bash
echo "that only few can see" | tee -a message1.txt message2.txt
```

# xargs

```bash
echo 'red blue yellow' | xargs mkdir
```

# RANDOM

```bash
echo $(( 1 + $RANDOM % 5 ))
```



