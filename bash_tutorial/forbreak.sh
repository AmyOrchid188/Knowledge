#!/bin/bash
# Author: Junhui Liu <liujunhui08@gmail.com>
# Created Time: 08/13/13 09:26:40 (CST)
# Modified Time: 08/13/13 09:31:16 (CST)
match=$1 # filename
found=0 # set to 1 if file found in the for loop

# show usage
[ $# -eq 0 ] && { echo "Usage: $0 filename"; exit 1; }

# Try to find file in /etc
for f in /etc/*
do
     if [ $f == "$match" ]
     then
         echo "$match file found!"
         found=1 #file found
         break # break the for loop
     fi

 done
 # loop file not found
 [ $found -ne 1 ] && echo "$match file not found in /etc directory"
