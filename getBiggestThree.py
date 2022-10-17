# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 11:02:09 2022

@author: sobirjon
"""

def getBiggestOfThree(a,b,c):
    if a>b:
        if a>c:
            return a
        else:
            return c
    else:
        if b>c:
            return b
        else:
            return c

print(f"Output: {getBiggestOfThree(11, 5, 1)}")