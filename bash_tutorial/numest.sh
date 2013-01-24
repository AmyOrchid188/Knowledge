#!/bin/bash
read -p "Enter a number: " n
if [ $n -gt 0 ]; then
   echo "$n is a positive."
elif [ $n -lt 0 ]
then 
   echo "$n is a negative."
elif [ $n -eq 0 ]
then
   echo "$n is zero number."
else
   echo "Oops! $n is not a number."
fi


