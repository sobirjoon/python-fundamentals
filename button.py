# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 15:41:11 2022

@author: sobirjon
"""

from tkinter import *   
  
top = Tk()
  
top.geometry("200x100")
  
b = Button(top,text = "Simple")
  
b.pack()  
  
top.mainaloop()