#!/bin/bash
OPT=$1 #option
FILE=$2 #filename

#test -e and -E command line args matching
case $OPT in
   -e|-E)
        echo "Editing $2 file..."
        [ -z $FILE ] && {  echo "File name missing"; exit 1; }||vi $FILE
        ;;
   -c|-C)
        echo "Displaying $2 file..."
        [ -z $FILE ] && { echo "File name missing."; exit 1; }|| cat $FILE
       ;;
   -d|-D)
        echo "Today is $(date)"
        ;;
   *)
    echo "Bad arguments"
    echo "Usage: $0 -ecd filename"
    echo "          -e file: Edit file."
    echo "          -c file: Display file."
    echo "          -d     : Display current date and time."
   ;;
esac



