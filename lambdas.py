# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 16:21:00 2022

@author: sobirjon
"""

 
from math import sqrt

# uzunlik = lambda pi, r : 2*pi*r
# print(uzunlik(math.pi, 10))

# product = lambda x,y : x ** y
# print(product(3, 3))

# def daraja(n): # funksiya yasovchi funksiya
#     return lambda x : x**n

# kvadrat = daraja(2)
# kub = daraja(3)
# print(f"3-ning kvadrati {kvadrat(3)} ga, kubi {kub(3)} ga teng")


# sonlar = list(range(11))
# ildizlar = list(map(sqrt, sonlar))
# print(ildizlar)

# kvadratlar = list(map(lambda x:x*x, sonlar))
# print(kvadratlar)


# a = [4, 5, 6]
# b = [7, 8, 9]

# a_plus_b = list(map(lambda x,y:x+y,a,b))
# print(a_plus_b)


# ismlar = ['hasan','husan','olim','umid']
# print(list(map(lambda matn:matn.upper(),ismlar)))

# import random as r

# sonlar = r.sample(range(100),10) # 0-99 oralig'ida 10 ta tasodifiy sonlar

# def juftmi(x):
#     """x juft bo'lsa True, aks holda False qaytaruvchu funksiya"""
#     return x%2==0

# juft_sonlar = list(filter(juftmi,sonlar))
# print(sonlar)
# print(juft_sonlar)

# import random as r

# sonlar = r.sample(range(100),10) # 0-99 oralig'ida 10 ta tasodifiy sonlar
# juft_sonlar = list(filter(lambda son: son%2==0,sonlar))

# print(sonlar)
# print(juft_sonlar)


# mevalar = ['olma','anor','anjir','shaftoli',"o'rik","tarvuz","qovun","banan"]

# mevalar_b = list(filter(lambda meva:meva.startswith('o'),mevalar))
# print(mevalar_b)

# mevalar2 = list(filter(lambda meva:len(meva)<=5, mevalar))
# print(mevalar2)

# list(filter(lambda meva:(meva.startswith('a') and meva.endswith('r')), mevalar))

















































