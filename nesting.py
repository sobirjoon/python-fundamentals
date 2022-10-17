# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 15:45:21 2022

@author: sobirjon
"""
# 16-lesson - Nesting

# developers = {
#     'ali':['python','c++'],
#     'vali':['html','css','js'],
#     'hasan':['php','sql'],
#     'husan':['python','php'],
#     'maryam':['c++','c#']
#     }

# for k, v in developers.items():
#     print(f"\n{k.title()} quyidagi dasturlash tillarini biladi: ", end='')
#     for k in v:
#      print(f'{k.upper()} ', end='')

# kinolar = {
#     'ali':['Terminator','Rambo','Titanic'],
#     'vali':['Tenet','Inception','Interstellar'],
#     'hasan':['Abdullajon','Bomba','Shaytanat'],
#     'husan':['Mahallada duv-duv gap','John Wick']
#     }

# for ism, kinolar in kinolar.items():
#     print(f"\n{ism.title()}ning sevimli kinolari:")
#     for i in kinolar:
#         print(i)

# davlatlar = {
#     "o'zbekiston":{'poytaxt':"toshkent",
#                    'maydon':448978,
#                    'aholi':33_000_000,
#                    'pul birligi':"so'm"
#                    },
#     "rossiya":{'poytaxt':"moskva",
#                    'maydon':17_098_246,
#                    'aholi':144_000_000,
#                    'pul birligi':"rubl"
#                    },
#     "aqsh":{'poytaxt':"vashington",
#                    'maydon':9_631_418,
#                    'aholi':327_000_000,
#                    'pul birligi':"dollar"},
#     "malayziya":{'poytaxt':"kuala-lumpur",
#                    'maydon':329750,
#                    'aholi':25_000_000,
#                    'pul birligi':"rinngit"}
#     }

# for davlat, info in davlatlar.items():
#     if davlat.lower()=='aqsh':
#         davlat = davlat.upper()
#     else:
#         davlat = davlat.capitalize()
#     print(f"\n{davlat}ning poytaxti {info['poytaxt'].title()}"
#           f"\nHududi: {info['maydon']} kv.km"
#           f"\nAholisi: {info['aholi']}"
#           f"\nPul birligi: {info['pul birligi']}")







# student1 = {
#     'first_name':'sobirjon',
#     'last_name':'ergashev',
#     'university':"queen's university belfast",
#     'major':'computer science'
#     }

# student2 = {
#     'first_name':'ahmad',
#     'last_name':'sobirjonov',
#     'university':"harvard university",
#     'major':'computer engineering'
#     }

# student3 = {
#     'first_name':'toshmat',
#     'last_name':'eshmatov',
#     'university':"stanford university",
#     'major':'information technology'
#     }
# student = [student1, student2, student3]
# for i in student:
#     print(f"\nFirst name : {i['first_name'].title()}", \
#           f"\nLast name: {i['last_name'].title()}", \
#           f"\nUniversity: {i['university'].title()}", \
#           f"\nMajor: {i['major'].title()}")
      
# malibus = []

# for i in range(10):
#     new_car = {
#         'model':'malibu',
#         'color':None,
#         'year':'2022',
#         'cost':None,
#         'km':0,
#         'korobka':'avto'     
#         }
#     malibus.append(new_car)

# for i in malibus[:3]:
#     i['color'] = 'blue'

# for i in malibus[3:6]:
#     i['color'] = 'black'
    
# for i in malibus[6:10]:
#     i['color'] = 'white'    
    
# for i in malibus:
#     if i['korobka']=='avto':
#         i['cost']=40000
#     else:
#         i['cost']=35000
    
# for i in malibus:
#     print(i)































