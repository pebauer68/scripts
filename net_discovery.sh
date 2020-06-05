nmap -sP 192.168.1.0/24 | grep for | awk '{ printf "%-30s %s\n", $5 , $6}' | sort
