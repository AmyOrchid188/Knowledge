#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Junhui Liu <liujunhui08@gmail.com>
# Created Time: 07/15/14 15:07:51 (CST)
# Modified Time: 07/15/14 15:10:42 (CST)
import unittest

class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget('The widget')

    def tearDown(self):
        self.widget.dispose()
        self.widget = None

    def test_default_size(self):
        self.assertEqual(self.widget.size(), (50,50),
                         'incorrect default size')

    def test_resize(self):
        self.widget.resize(100,150)
        self.assertEqual(self.widget.size(), (100,150),
                         'wrong size after resize')
if __name__ == '__main__':
    #unittest.main()
     widgetTestSuite = unittest.TestSuite()
     widgetTestSuite.addTest(WidgetTestCase('test_default_size'))
     widgetTestSuite.addTest(WidgetTestCase('test_resize'))
