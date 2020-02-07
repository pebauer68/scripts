#!/bin/bash
# example: >  ./show_p_mem.sh $(pidof <program name>)   
# check that pidof gives only one pid as result !
echo "$1" | xargs pmap | grep total | awk '{ printf("%'"'"'d Kbytes\n",$2); }'
