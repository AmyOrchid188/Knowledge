#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Junhui Liu <liujunhui08@gmail.com>
# Created Time: 06/08/13 14:20:54 (CST)
# Modified Time: 06/08/13 14:42:50 (CST)

# Exercise 43: Basic Oject Orented Analysis And Design
class Scene(object):

    def enter(self):
        pass

class Engine(object):

    def __init__(self, scene_map):
        pass

    def play(self):
        pass

class Death(Scene):

    def enter(self):
        pass

class CentralCorridor(Scene):

    def enter(self):
        pass

class LaserWeaponArmory(Scene):

    def enter(self):
        pass

class TheBridge(Scene):

    def enter(self):
        pass

class Map(object):

    def __init__(self, start_scene):
        pass
    def next_scene(self, scene_name):
        pass
    def opeing_scene(self):
        pass

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
