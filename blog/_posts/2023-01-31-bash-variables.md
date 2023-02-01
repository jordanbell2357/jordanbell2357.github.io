---
layout: post
title: Bash variables
---

`cat vars.sh`

```bash
#!/usr/bin/env bash
#File: vars.sh

x=5
echo "The value of x is $x"
let x=$x+1
echo "The value of x is $x"
num_lines=$(cat vars.sh | wc -l)
echo "The number of lines in this file is $num_lines"
```

`bash vars.sh`

```
The value of x is 5
The value of x is 6
The number of lines in this file is 9
```

`cat args.sh`

```bash
#!/usr/bin/env bash
#File: args.sh

file_lines=$(cat $1 | wc -l)
echo "The numer of lines in $1 is $file_lines"
```

`bash args.sh args.sh`

```
The numer of lines in args.sh is 5
```

`bash args.sh vars.sh`

```
The numer of lines in vars.sh is 9
```