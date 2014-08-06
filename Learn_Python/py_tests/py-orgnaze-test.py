#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Junhui Liu <liujunhui08@gmail.com>
# Created Time: 07/15/14 15:04:20 (CST)
# Modified Time: 07/15/14 15:07:39 (CST)
import unittest

class SimpleWidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget('The widget')

class DefaultWidgetSizeTestCase(SimpleWidgetTestCase):
    def runTest(self):
        self.assertEqual(self.widget.size(), (50,50),
                         'incorrect default size')

class WidgetResizeTestCase(SimpleWidgetTestCase):
    def runTest(self):
        self.widget.resize(100,150)
        self.assertEqual(self.widget.size(), (100,150),
                         'wrong size after resize')
