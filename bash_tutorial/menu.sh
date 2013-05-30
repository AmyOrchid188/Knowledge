#!/bin/bash
# A menu driven program using while loop
# The following menu driven program typically continue till user selects to exit by pressing 4 option. → The case
# statement is used to match values against $choice variable and it will take appropriate action according to users
# choice.
#---------------------------------------------------------------------------------------
# set an infinite loop
while :
do
    clear
    # display menu
    echo "Server Name - $(hostname)"
    echo "--------------------------" 
    echo "   M A I N M E N U"
    echo "--------------------------"
    echo "1. Display date and time."
    echo "2. Display what users are doing"
    echo "3. Display network connections."
    echo "4. exit."
    #get input from user
    read -p "Enter your choice [ 1 - 4 ] " choice
    # Making decision using case .. in ..esac
    case $choice in 
           1)
            echo "Today is $(date)"
            read -p "Press [Enter] key to continue...."
            ;;
          2)
            w
            read -p "Press [Enter] key to continue...."
            ;;
         3)
            netstat -ntlp
           
            read -p "Press [Enter] key to continue...."
            ;;
         4)
            echo "Bye!!"
            exit 1
            ;;
         *)
           echo "Error: Invalid option ...."
           read -p "Press [Enter] key to continue...."
            ;;
           
   esac         
done
