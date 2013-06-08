#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Junhui Liu <liujunhui08@gmail.com>
# Created Time: 06/08/13 09:29:01 (CST)
# Modified Time: 06/08/13 09:41:56 (CST)
# Exercise 42 Is-A, Has-A, Objects, and Classes
## Animal is-a object(yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is-a object
class Dog(Animal):

    def __init__(self, name):
        ##Dog has a __init___ function with self and name parameters
        self.name = name

## cat is-a object
class Cat(Animal):

    def __init__(self, name):
        ##??
        self.name = name

## Person is-a object
class Person(object):

    def __init__(self, name):
        ## ??
        self.name = name
        ## Person has-a pet of some kind
        self.pet = None

##
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? what is this strange magic?
        super(Employee,self).__init__(name)
        ## ??
        self.salary = salary

##
class Fish(object):
    pass
## ??
class Salmon(Fish):
    pass
##??
class Halibut(Fish):
    pass

## rover is-a Dog
rover = Dog("Rover")

## satan is-a cat
satan = Cat("Satan")

##mary is-a person
mary = Person("Mary")

## mary has-a pet named satan
mary.pet = satan
## Frank is-a employee with 120000 salary
frank = Employee("Frank", 120000)

## frank has-a pet named rover
frank.pet = rover

## flipper is-a fish
flipper = Fish()
## crouse is-a salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()
