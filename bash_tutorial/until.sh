#!/bin/bash
# Author: Junhui Liu <liujunhui08@gmail.com>
# Created Time: 08/13/13 08:49:35 (CST)
# Modified Time: 08/13/13 08:51:17 (CST)
i=1
until [ $i -gt 6 ]
do
    echo "Welcome $i times."
    i=$(( i+1 ))
done
