#!/bin/bash
# useful example for reading and phrasing /etc/passwd [1] file using the while loop
file=/etc/passwd
# set field delimiter to :
# read all 7 fields in to 7 vars
while IFS=: read -r user enpass uid gid desc home shell
do
   # only display for uid >=500
   [ $uid -ge 500 ] && echo "User $user ($uid) assigned \"$home\" home directory with $shell shell"
done < "$file"

