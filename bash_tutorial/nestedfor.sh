#!/bin/bash
# A shell script to print each number five times.
for ((i=1; i<=5; i++))
do
   for ((j=1; j<=5;j++))
   do
      echo -n "$1 "
   done
   echo "" ### Print the new line###
done
