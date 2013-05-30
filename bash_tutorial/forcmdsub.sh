#!/bin/bash
# A simple script for display command subsitution 
echo "Print file names in /tmp directory: "
for f in $(ls /tmp/*)
do
   echo $f
done 
