#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Junhui Liu <liujunhui08@gmail.com>
# Created Time: 05/29/13 11:28:12 (CST)
# Modified Time: 05/29/13 11:35:07 (CST)
# Exercise 17: More Files
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from  %s to %s " % (from_file, to_file)

# we could do these two on on line too, how?
in_file = open(from_file)
indata = in_file.read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()
in_file.close()
