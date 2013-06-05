#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Junhui Liu <liujunhui08@gmail.com>
# Created Time: 05/31/13 15:31:45 (CST)
# Modified Time: 05/31/13 16:05:58 (CST)
# Exercise 24: More Practice

print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intution
and requires an explannation
\n\t\twhere there is none.
"""

print "-------------------"
print poem
print "-------------------"

five = 10 - 2 + 3 - 6
print "This should be five:%s" % five
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 100
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = secret_formula(start_point)

print "With a starting point of : %d " % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans,jars,crates)

start_point = start_point / 10
print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)
