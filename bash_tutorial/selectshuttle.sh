#!/bin/bash
# Author: Junhui Liu <liujunhui08@gmail.com>
# Created Time: 08/13/13 09:00:17 (CST)
# Modified Time: 08/13/13 09:24:41 (CST)
# The default value for PS3 is set to #?.
# Change it i.e. Set PS3 prompt

PS3="Enter the space shuttle to get quick information: "

# set shuttle list
select shuttle in columbia endeavour challenger discovery atlantis enterprise pathfinder exit
do
    case $shuttle in
        columbia)
            echo "---------------------"
            echo "Space Shuttle Co.umbia was the first spaceworthy space shuttle in NASA's orbital fleet."
            echo "---------------------"
            ;;
        endeavour)
            echo "---------------------"
            echo "Space Shuttle Endeavour is one of three currently operational orbiters in the Space Shuttle."
            echo "---------------------"
            ;;
        challenger)
            echo "---------------------"
            echo "Space Shuttle Challenger was NASA's second Space Shuttle orbiter to be put into service."
            echo "---------------------"
            ;;
        discovery)
            echo "---------------------"
            echo "Discovery became the third operational orbiter, and is noe the oldest one in service."
            echo "---------------------"
            ;;
        atlantis)
            echo "---------------------"
            echo "Atlantis was the fourth operational shuttle built."
            echo "---------------------"
            ;;
        enterprise)
            echo "---------------------"
            echo "Space Shuttle Enterprise was the first Space Shuttle orbiter."
            echo "---------------------"
            ;;
        pathfinder)
            echo "--------------------"
            echo "Space Shuttle Orbiter Pathfinder is a Space Shuttle simulator made of steel and wood."
            echo "--------------------"
            ;;
        exit)
            echo "Bye!"
            break
            ;;
        *)
            echo "Error: Please try again(select 1..8)!"
            ;;
    esac
done
