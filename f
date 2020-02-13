#!/bin/bash
# display help texts
argc=$1               # read the command line argument
myed="pluma"          # set myed to my editors name

case "$argc" in
     "" )   ;;                            # do nothing
     e )    $myed ~/bin/fav.txt& ;;       # edit help text
     f )    $myed ~/bin/f& ;;             # edit helper script
     ?|-help|--help )   echo "usage: Parameter e ... edit help text";
                        echo "       Parameter f ... edit helper script" ;; 
esac

echo helptext in: ~/bin/fav.txt
cat ~/bin/fav.txt
