#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Junhui Liu <liujunhui08@gmail.com>
# Created Time: 05/30/13 08:59:23 (CST)
# Modified Time: 05/30/13 09:09:04 (CST)
# Exercise 21: Functions Can Return Something
def add(a, b):
    print "Adding %d + %d " % (a, b)
    return a + b

def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a -b

def multiply(a, b):
    print "MULTIPLYING %d * %d " % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b

print "Let's do some math with just functions!"

age = add( 30, 5)
height = subtract( 78, 4)
weight = multiply( 90, 2)
iq = divide( 100, 2)


print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# A pluzzle for the extra credit, type it in anyway
print "Here is a puzzle."
what = add(age, subtract(height,multiply(weight, divide(iq, 2))))
print "That becomes:", what, "can you do it by hand?"
