#!/bin/bash
# Author: Junhui Liu <liujunhui08@gmail.com>
# Created Time: 08/13/13 09:31:42 (CST)
# Modified Time: 08/13/13 09:34:58 (CST)
# set an infinite while loop
while :
do
    read -p "Enter number (-9999 to exit ) : " n

    # break while loop if input is -9999
    [ $n -eq -9999 ] && { echo "Bye!"; break; }

    isEvenNo=$(( $n %2 )) #get modules
    [ $isEvenNo -eq 0 ] && echo "$n is an even number." || echo "$n is an odd number."

done
