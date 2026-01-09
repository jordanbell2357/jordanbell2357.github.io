#!/usr/bin/env bash

COLS=$(tput cols)
echo "This terminal has $COLS columns"
sleep 2

echo "$COLS A's on next line"
yes A | head -n $COLS | tr -d "\n"
echo
sleep 2

echo "$(($COLS+5)) A's on next line"
yes A | head -n $(($COLS+5)) | tr -d "\n"
echo
sleep 2

setterm --linewrap off
echo "Linewrap is now off"
sleep 2

echo "$(($COLS+5)) A's on next line"
yes A | head -n $(($COLS+5)) | tr -d "\n"
echo
sleep 2

setterm --linewrap on
echo "Linewrap is now back on"