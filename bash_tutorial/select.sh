#!/bin/bash
# Author: Junhui Liu <liujunhui08@gmail.com>
# Created Time: 08/13/13 08:52:28 (CST)
# Modified Time: 08/13/13 08:59:23 (CST)
# PS3 - Prompt used by "select" inside shell script
# Set PS3 prompt
PS3="Enter the space shuttle to get more information :"

# set shuttle list
select shuttle in columbia endeavour challenger discovery atlantis enterprise pathfinder
do
    echo "$shuttle selected"
done
