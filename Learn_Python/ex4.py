#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Kun Huang <academicgareth@gmail.com>
# Created Time: 05/24/13 09:05:05 (CST)
# Modified Time: 05/24/13 09:29:57 (CST)
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empyty cars today."
print "We c an transport", carpool_capacity, "people today"
print "We have ", passengers,"to carpool today"
print "We need to put about", average_passengers_per_car, "in each car."
