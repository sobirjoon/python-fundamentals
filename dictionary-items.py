# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 15:03:35 2022

@author: sobirjon
"""

# 14-dars: Worrk with dictionary items

# .items() metodi


# student = {
#     'first_name':'sobirjon',
#     'last_name':'ergashev',
#     'email':'sobirijone@outlook.com',
#     'birthdate':'13.03.2000',
#     'marital_status':'single',
#     'job':'student',
#     'phone_number':'+44 7950 973241'
#     }

# print(student.items())

# for key,value in student.items():
#     print(f"Key: {key}")
#     print(f"Value: {value} \n")
    
# cars = {
#         'ahmad':'matiz',
#         'toshmat':'gentra',
#         'eshmat':'malibu',
#         'toshmamat':'tracker',
#         'ali':'matiz',
#         'vali':'gentra',
#         'olim':'lacetti'
#         }    

# for k, v in cars.items():
#     print(f"{k.title()}ning mashinasi {v}")
    
# .keys() metodi

# products = {
#     'olma':10000,
#     'anor':12000,
#     'uzum':13000,
#     'anjir':25000,
#     "yong'oq":30000,
#     "nok":9000    
#     }

# print(products.keys())

# print("Do'kondagi mahsulotlar:")
# for i in products.keys():
#     print(i.title())
    
# orders = ['anor', 'olma','tuxum','baliq']
# for i in products:
#     if i in orders:
#         print(f"{i.title()} {products[i]} so'm")

# for i in orders:
#     if i not in products:
#         print(f"Iltimos, do'koningizga {i} ham olib keling")

# for i in sorted(products):
#     print(i.title())

# .values() metodi

cars = {
        'ahmad':'matiz',
        'toshmat':'gentra',
        'eshmat':'malibu',
        'toshmamat':'tracker',
        'ali':'matiz',
        'vali':'gentra',
        'olim':'lacetti'
        }  

# print(cars.values())

# print("Foydalanuvlar quyidagi mashinalarni yoqtirishadi: ")
# for i in cars.values():
#     print(i)

# print("Quyidagilar eng ommabop mashinalar: ")
# for i in set(cars.values()):
#     print(i)


# for i in range(1,61):
#     print(f"{i}) Salom!")

# countries = {
#     'uzbekistan':'tashkent',
#     'usa':'washington',
#     'russia':'moscow',
#     'malasia':'kuala-lumpur',
#     'turkey':'anqara',
#     'uk':'london'
#     }

# country = input("Which country's capital city do you want to know?\n>>> ").lower()
# capital = countries.get(country)

# if capital==None:
#     print(f"Sorry, info about {country} is not available in our db.")
# else:
#     print(f"{country.upper()}'s capital city is {capital.title()}")

# print('Countries in the world: ')
# for i in sorted(countries):
#     print(i.upper())

# print('Capital cities of countries:')
# for i in sorted(countries.values()):
#     print(i.upper())


# menu = {
#         'osh':20000,
#         "lag'mon":22000,
#         'non':4000,
#         'choy':5000,
#         'shashlik':12000,
#         'somsa':6000,
#         'tabaka':15000
#         }

# print('3 ta taomga buyurtma bering.')
# orders = []
# for i in range(3):
#     orders.append(input(f"{i+1}-taom:").lower())
# print('\n')
# for i in orders:
#     if i in menu:
#         print(f"{i.title()} {menu[i]} so'm")
#     else:
#         print(f"Kechirasiz, bizda {i} yo'q.")
        
    















