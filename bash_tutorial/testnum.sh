#!/bin/bash
read -p "Enter number: " n
if test $n -ge 0
then
    echo "$n is positive number."
else
    echo "$n is negative number."
fi
