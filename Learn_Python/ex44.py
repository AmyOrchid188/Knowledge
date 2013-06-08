#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Junhui Liu <liujunhui08@gmail.com>
# Created Time: 06/08/13 14:43:31 (CST)
# Modified Time: 06/08/13 14:48:02 (CST)
# Exercise 44: Inheritance Vs. Composition

class Parent(object):

    def override(self):
        print "PARENT override()"

    def implicit(self):
        print "PARENT implicit()"

    def altered(self):
        print "PARENT  altered()"

class Child(Parent):

    def override(self):
        print "CHILD override()"

    def altered(self):
        print "CHILD altered()"
        super(Child, self).altered()
        print "CHILD, AFTER PARENT altered()"


dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()
