# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 11:04:51 2022

@author: sobirjon
"""

def factorial(N):
    i=1
    factorial=1
    while i!= N+1:
        factorial = factorial*i
        i += 1
    return factorial

print(f"OUTPUT: {factorial(9)}")