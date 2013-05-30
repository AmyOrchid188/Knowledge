#!/bin/bash
# read a text file using read command and while loop
file=/etc/resolv.conf
while IFS= read -r line
do
  # echo line is sorted in $line
  echo $line

done < "$file"

