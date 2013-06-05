#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Junhui Liu <liujunhui08@gmail.com>
# Created Time: 06/04/13 09:04:08 (CST)
# Modified Time: 06/04/13 09:08:52 (CST)
# Exercise 29: What If

people = 20
cats = 30
dogs = 15

if people < cats:
    print "Too many cats! The world is doomed!"

if people > cats:
    print "Not many cats! The world is saved!"

if people < dogs:
    print "The world is drooled on !"

if people > dogs:
    print "The world is dry!"


dogs += 5
if people >= dogs:
    print "People are greater than or equal to dogs."

if people <= dogs:
    print "People are less than or equal to dogs."

if people == dogs:
    print "People are dogs."
