#!/usr/bin/env bash

# \e = \033

printf "Default\e[1B"
sleep 1
printf "\e[1mBold\e[0m\e[1B"
sleep 1
printf "\e[3mItalic\e[0m\e[1B"
sleep 1
printf "\e[1m\e[5mBold blinking"
sleep 3
printf "\e[0m\e[1B"
sleep 1
printf "\e[7mInverted\e[0m\e[1B"
sleep 1
printf "\e[21mUnderlined\e[0m\e[1B"
sleep 1
printf "\e[31mRed foreground\e[0m\e[1B"
sleep 1
printf "\e[42mGreen background\e[0m\e[1B"
sleep 1
printf "\e[9mStrikethrough\e[0m\e[1E"
sleep 1
printf "First newline\n"
sleep 1
printf "Hello"
sleep 3
printf "\e[1KBye\n"