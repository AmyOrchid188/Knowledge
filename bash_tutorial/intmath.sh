#!/bin/bash
#set x,y,z  to an interger data type
declare -i x=5
declare -i y=10
declare -i z=0
z=$(( x + y ))
echo "$x + $y = $z"
#try to setting to character 'a'
x=a
z=$(( x + y ))
echo "$x + $y = $z"
