#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Junhui Liu <liujunhui08@gmail.com>
# Created Time: 06/04/13 09:11:52 (CST)
# Modified Time: 06/04/13 09:19:04 (CST)
# Exercise 30: Else And If
people = 30
cars = 40
buses = 15

if cars > people:
    print "We should take the cars."
elif cars <people:
    print "We should not take the cars"
else:
    print "We can't decide."

if buses > cars:
    print "That's too many busses."
elif buses < cars:
    print " Maybe we could take the buses."
else:
    print " We still can't decide."

if people > buses:
    print "Alright, let's just take the buses."
else:
    print "Fine, let's stay home then."
