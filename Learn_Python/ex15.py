#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Junhui Liu <liujunhui08@gmail.com>
# Created Time: 05/29/13 11:00:59 (CST)
# Modified Time: 05/29/13 11:05:04 (CST)
# Exercise 15: Reading Files
from sys import argv

script, filename = argv

txt = open(filename)

print "Here's you file %r:" % filename
print txt.read()

print "Type the filename agagin:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
