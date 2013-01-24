#!/bin/bash
# set var
PASSWORD_FILE=/etc/passwd
# get user name
read -p "Enter a username :" username

# try to locate username in in /etc/passwd
grep "^$username" $PASSWORD_FILE > /dev/dull

# store exit status of grep
# if found grep will return 0 exit status
# if not found grep will return a nonzero exit status
status=$?


if test $status -eq 0
then
    echo "User '$username' found in $PASSWORD_FILE file"
else
    echo "User '$username' not found in $PASSWORD_FILE file"
fi

