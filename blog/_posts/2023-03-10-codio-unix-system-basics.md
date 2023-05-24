---
layout: post
title: My favorite material from Codio's Unix System Basics on Coursera
topic: training
---

[Unix System Basics \| Codio](https://www.coursera.org/learn/codio-unix-system-basics)

# sed

> Delete all blank lines.

```bash
sed '/^$/d' myfile.txt 
```

> From a specific line to the end of the file.

```bash
sed '/So I tried/,$d' myfile.txt
```

> Delete everything after a specific line and save it "in place".

```bash
sed -i '1,/So I tried/!d' myfile.txt
```

# awk

> Using `awk` to count the number of occurrences of the word "Pooh" in the text

```bash
awk '/Pooh/{x++}END{print x}' myfile.txt
```

> Print the number of words in a file.

```bash
awk '{ total = total + NF }; END {print total}' myfile.txt 
```

> Print the number of lines in a file.

```bash
awk 'END{print NR}' myfile.txt
```

> Parse the comma-separated text and output two fields from each line. Don’t print the header line.

```bash
 awk -F"," '{if (NR!=1){ print $1 $2 $3 }}' data.csv
```

> Print out just the second column of the file.

```bash
awk  -F"," '{print $2}' data.csv 
```

# printf

> Print the result of a math equation.

```bash
printf "%d\n" $((8+4))
```

> Print only the first 4 digits beyond the decimal point of a floating point number.

```bash
printf "%.4f\n" 3.1415926535
```

# dd

> This command copies the contents of trydd.txt to outdd.txt using the conversion ucase which turned it all to upper case characters.

```bash
dd if=trydd.txt of=outdd.txt conv=ucase
```

# while

> Create a foreground job that prints out numbers to the console in a forever loop.

```bash
COUNTER=0; while true; do printf $COUNTER; sleep 1; let COUNTER++; done
```