# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 15:48:54 2022

@author: sobirjon
"""

import unittest 

from circle import *



class CircleTest(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(getArea(5), 78.53975)
        self.assertAlmostEqual(getArea(10), 314.159)
     
    def test_perimeter(self):
        self.assertAlmostEqual(getPerimeter(5), 31.4159)
        self.assertAlmostEqual(getPerimeter(6), 37.699079999999995)   
        
unittest.main()












