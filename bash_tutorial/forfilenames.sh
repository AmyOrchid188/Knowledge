#!/bin/bash
# A shell script to verify user password database
files="/etc/passwd /etc/group /etc/shadow /etc/gshadow"
for f in $files
do
   [ -f $f ] && echo "$f file found." || echo "***Error -  $f file missing."
done
