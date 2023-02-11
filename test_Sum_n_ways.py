# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 14:10:33 2023

@author: ramli
"""

import unittest
import Sum_n_ways

class T_sum1_n_ways (unittest.TestCase):
    def test_add_1 (self): #positive case 1
        result = Sum_n_ways.sum1 (10,5)
        self.assertEqual(result, 15)
    
    def test_add_2 (self): #positive case 2
        result = Sum_n_ways.sum1 (0,0.4)
        self.assertEqual (result, 0.4)
        
    def test_add_3 (self): #Negative case 1
        result = Sum_n_ways.sum1 (3)
        self.assertNotEqual (result, 3)

    def test_add_4 (self): #Positive case 2
        result = Sum_n_ways.sum1 (0)
        self.assertEqual (result, 20)

class T_sum2_n_ways (unittest.TestCase):
    def test_add_1 (self): # we can use more than one assert function.
    # but considered as one Test case
        self.assertEqual (Sum_n_ways.sum2 (10,5), 15)
        self.assertEqual (Sum_n_ways.sum2 (0,0.4), 0.40)
        self.assertNotEqual (Sum_n_ways.sum2 (3, 10), 12)

if __name__ == '__main__':
    unittest.main()