#!/usr/bin/env bash

setterm --bold on
echo "This line is bold"
sleep 2

setterm --blink on
echo "This line is bold and blinking"
sleep 2
setterm --foreground default

setterm --foreground magenta
echo "This line foreground color is magenta"
sleep 2
setterm --foreground default

setterm --background blue
echo "This line background color is blue"
sleep 2
setterm --background default

setterm --half-bright on --foreground red
echo "This line is half-bright and has foreground red"
sleep 2
setterm --half-bright off --foreground default

setterm --inversescreen on 
echo "The screen is inverted"
sleep 2
setterm --inversescreen off

echo "The screen is no longer inverted"
sleep 2

setterm --reverse on
echo "This line is inverted"
sleep 2
setterm --reverse off

echo "This line is no longer inverted"
sleep 2

setterm --underline on
echo "This line is underlined"
sleep 2
setterm --underline off

echo "This line is no longer underlined"
sleep 2

setterm --default
echo "This line is default (should be same style as previous line)"