#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Junhui Liu <liujunhui08@gmail.com>
# Created Time: 07/15/14 14:50:26 (CST)
# Modified Time: 07/15/14 15:01:42 (CST)
import random
import unittest

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.seq = list(range(10))

    def test_shuffle(self):
        # make sure the shuffled sequence does not lose any elements
        random.shuffle(self.seq)
        self.seq.sort()
        self.assertEqual(self.seq, list(range(10)))

        # should raise an exception for an immutable sequence
        self.assertRaises(TypeError, random.shuffle, (1,2,3))

    def test_choice(self):
        element = random.choice(self.seq)
        self.assertTrue(element in self.seq)

    def test_sample(self):
        with self.assertRaises(ValueError):
            random.sample(self.seq, 20)
        for element in random.sample(self.seq, 5):
            self.assertTrue(element in self.seq)

#def suite():
#    suite = unittest.TestSuite()
#    suite.addTest(TestSequenceFunctions())
#    return suite
if __name__ == '__main__':
    unittest.main()
#    runner = unittest.TextTestRunner()
#
#    test_suite = suite()
#
#    runner.run (test_suite)
