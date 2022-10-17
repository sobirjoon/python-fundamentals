# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 15:23:42 2022

@author: sobirjon
"""

#unit_testing


def get_full_name(name, surname, middle=''):
    
    if middle:
        return f"{name} {middle} {surname}".title()
    else:
        return f"{name} {surname}".title()

