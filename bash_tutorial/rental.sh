#!/bin/bash

# if no command line argument given
# set rental to Unknown

if [ -z $1 ]
then
   rental="*** Unknown vehicle***"
elif [ -n $1 ] # not empty
then
 # otherwise make first arg as rental
  rental=$1
fi


# Use case statement to make decision for rental
case $rental in 
     "car") echo "For $rental rental is Rs.20 per k/m.";;
     "van") echo "For $rental rental is Rs.10 per k/m.";;
     "jeep") echo "For $rental rental is Rs.5 per k/m.";;
     "bicycle") echo "For $rental rental is 20 paisa per k/m.";;
     "enfield") echo "For $rental rental is Rs.3 per k/m.";;
     "thunderbird") echo "For $rental rental is Rs.5 per k/m.";;
     *) echo "Sorry, I can not get a $rental rental for you!";;
esac


