#!/bin/bash
# this script is test string compare
read -s -p "Enter your password " pass
echo
if test "$pass" = "tom"
then
   echo "you are allowed to login!"
fi
