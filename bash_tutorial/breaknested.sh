#!/bin/bash
# Author: Junhui Liu <liujunhui08@gmail.com>
# Created Time: 08/13/13 09:36:04 (CST)
# Modified Time: 08/13/13 09:49:55 (CST)
j=0
for i in {1..5}
do
    while true
    do
        echo " i is $i"
        j=$(( $j+1 ))
        [ $j -eq 4 ] && break 2
    done
done
