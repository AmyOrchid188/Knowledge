#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Junhui Liu <liujunhui08@gmail.com>
# Created Time: 05/29/13 16:30:04 (CST)
# Modified Time: 05/29/13 16:39:00 (CST)
# Exercise 18: Names, Variables, Code, Functions
# this one is like you scripts with argv

def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r " % (arg1, arg2)

# Ok , that *args is actually pointless, we can just do this
def print_two_again(arg1,arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes one argument
def print_one(arg1):
    print "arg1: %r" % arg1

# this one takes no argument
def print_none():
    print "I got nothin'."


print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()
