#!/bin/bash
# set n to 1
n=1
# Continue until $n equsls 5
while [ $n -le 5 ]
do
   echo "Welcome $n times."
   n=$(( n + 1 )) #increaments $n
done

