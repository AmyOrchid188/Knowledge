#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Junhui Liu <liujunhui08@gmail.com>
# Created Time: 07/15/14 16:15:32 (CST)
# Modified Time: 07/15/14 16:36:04 (CST)
import unittest

class InequalityTest(unittest.TestCase):

    def testEqual(self):
        self.assertNotEqual(1, 3-2)

    def testNotEqual(self):
        self.assertEqual(2, 3-2)

if __name__ == '__main__':
    #unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(InequalityTest("testNotEqual"))
    suite.addTest(InequalityTest("testEqual"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
