#!/bin/bash
# A simple shell script for display multiplication of number which passed from command line argument
n=$1
# make sure command line arguments are passec to  the script
if [ $# -eq 0 ]
then
    echo "A shell script to print multiplication table."
    echo "Usage: $0 number."
    exit
fi

# use for loop
for i in {1..10}
do
   echo "$n * $i = $(($n * $i))"
done

