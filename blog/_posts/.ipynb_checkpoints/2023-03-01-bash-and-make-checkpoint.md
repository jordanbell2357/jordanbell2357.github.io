---
layout: post
title: Bash and Make
topic: cli
---

[The Unix Workbench \| Johns Hopkins University](https://www.coursera.org/learn/unix)

> The `guessinggame.sh` program should have the following behavior:
>
> - When the program starts the user should be asked how many files are in the current directory, and then the user should be prompted for a guess.
>
> - If the user's answer is incorrect the user should be advised that their guess was either too low or too high and then they should be prompted to try to guess again.
>
> - If the user's guess is correct then they should be congratulated and the program should end.
>
> - The program should not end until the user has entered the correct number of files in the current directory.
>
> - The program should be able to be run by entering `bash guessinggame.sh` into the console.
>
> - The program should contain at least one function, one loop, and one if statement.
>
> - The program should be more than 20 lines of code but less than 50 lines of code.
>
> The makefile should produce the `README.md` which should contain the following information:
>
> - The title of the project.
>
> - The date and time at which make was run.
>
> - The number of lines of code contained in `guessinggame.sh`.
>
> - The `README.md` should be produced entirely from the makefile and should not be edited by hand.

<https://github.com/jordanbell2357/bash-make-git-and-github>

`guessinggame.sh`

```bash
#!/usr/bin/bash
#Filename: guessinggame.sh

numfiles=$(ls -1 | wc -l)

function user_guess {
  echo "Guess how many files are in the current directory:"
  read response
}

user_guess

while [[ $response -ne $numfiles ]]
do
  if [[ $response -gt $numfiles ]]
  then
    echo "Guess is too high"
  else
    echo "Guess is too low"
  fi
  user_guess
done
echo "Guess is correct. Congratulations!"
```

`makefile`

```bash
all: README.md

README.md: guessinggame.sh
	echo "# Bash, Make, Git, and GitHub" > README.md
	echo "The date and time at which make was run:" >> README.md
	date >> README.md
	echo "\n" >> README.md
	echo "The number of lines of code contained in guessinggame.sh:" >> README.md
	wc -l guessinggame.sh | egrep -o "[0-9]+" >> README.md

clean:
	rm README.md
```