#!/bin/bash
# A simple shell script to run commands
for command in date pwd df
do
   echo
   echo "*** The output of $command command  >"
   # run command
    $command
    echo
done
