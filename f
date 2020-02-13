#!/bin/bash
# display help texts
argc=$1               # read the command line argument
myed="pluma"          # set myed to my editors name

case $argc in
    "e" )    $myed ~/bin/fav.txt& ;;       # edit help text
    "f" )    $myed ~/bin/f& ;;             # edit helper script
esac

echo ~/bin/fav.txt
cat ~/bin/fav.txt
