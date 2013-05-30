#!/bin/bash
# A simple shell script to display a file on screen passed as command line arguments
  [ $# -eq 0 ] && { echo "Usage: $0 file1 file2 fileN"; exit 1; }
# read all command line araguments via for loop
for f in $*
do 
   echo 
   echo "< $f >"
   [ -f $f ] && cat $f || echo "$f is not file."
   echo "-----------------------------------------"
done
