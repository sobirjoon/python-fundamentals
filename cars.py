# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 15:57:41 2022

@author: sobirjon
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 17:04:18 2022

@author: sobirjon
"""
from uuid import uuid4

class Auto:

    def __init__(self, make, model, year, km=0, price=None):
        
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        self.__km = km

    def set_price(self, price):
        self.price = price
    
    def add_km(self, km):
        
        if km>=0:
            self.__km += km
        else:
            raise ValueError("km manfiy bo'medi.")
            
    def get_info(self):
        info = f"{self.make.upper()} {self.model.title()}"
        info += f"{self.year}-yil, {self.__km} km yurgan."
        if self.price:
            info += f" Narxi: {self.price}"
        return info
    
    def get_km(self):
        return self.__km
