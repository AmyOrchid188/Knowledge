#!/bin/bash
# A shell script to look up usernames in /etc/passwd file
# Written by: Vivek Gite
# Last Updated on: Sep/10/2003
# -----------------------------------------------
# Set vars
user=$1 #first command line argument

passwddb=/etc/passwd

# Verify the type of input and number of values
# Display an error message if the username(input) is not correct
# Exit the shell script with a status of 1 using exit 1 command

[ $# -eq 0 ] && { echo "Usage: $0 username"; exit 1; }

grep "^$user" $passwddb > /dev/null
retval=$? #store exit status of grep

# If grep found username, it sets exit status to zero
# Use exit status to make the decision
[ $retval -eq 0 ] && echo "$user found" || echo "$user not found"


