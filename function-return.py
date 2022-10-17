# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 12:03:59 2022

@author: sobirjon
"""

# 20-dars. Functions: return 

# def full_name(first, last):
#     full_name = f"{first} {last}"
#     return full_name


# student = full_name('Sobirjon', 'Ergashev')


# def full_name(first, last, middle=''):
#     if middle: 
#         full_name = f"{first} {middle} {last}"
#     else:
#         full_name = f"{first} {last}"
#     return full_name.title()

# student = full_name('Sobirjon', 'Ergashev', 'Nabijonovich')
# print(student)

# None = mavjud emas

# def avto_info(company, model, color, year, cost=None):
#     auto = {
#         'company': company,
#         'model': model,
#         'color': color,
#         'year' : year,
#         'cost' : cost        
#         }
#     return auto

# automobile1 = auto_info('GM', 'Malibu', 'Qora', 2021)
# automobile2 = auto_info('GM', 'Nexia 3', 'Oq', 2020, 10500)

# automobiles = [automobile1, automobile2]

# print('CARS AVAILABLE NOW: ')
# for i in automobiles:
#     if i['cost']:
#         cost = i['cost']
#     else:
#         cost = "Unavailable"
#     print(f"{i['model']} {i['color']}. Cost: {cost}")


# def oraliq(min, max, step=1):
#     sonlar = []
#     while min<max:
#         sonlar.append(min)
#         min += step
#     return sonlar
    
# print(oraliq(0, 10))
# print(oraliq(0, 21, 2))

# print("Saytimizdagi avtolar ro'yxatini shakllantiramiz.")
# avtolar=[] # salondagi avtolar uchun bo'sh ro'yxat
# while True:
#     print("\nQuyidagi ma'lumotlarni kiriting",end='')
#     kompaniya=input("Ishlab chiqaruvchi: ")
#     model=input("Modeli: ")
#     rangi=input("Rangi: ")
#     korobka=input("Korobka: ")
#     yili=input("Ishlab chiqarilgan yili: ")
#     narhi=input("Narhi: ")
#     kompaniya, model, rangi, korobka, yili, narhi))
    
#     #Foydalanuvchi kiritdan ma'lumotlardan avto_info yordamida 
#     #lug'at shakllantirib, har bir lug'atni ro'yxatga qo'shamiz:
#     avtolar.append(avto_info(
#     # Yana avto qo'shish-qo'shmaslikni so'raymiz
#     javob = input("Yana avto qo'shasizmi? (yes/no): ")
#     if javob=='no':
#         break

# def largest(x,y,z):
#     max = x
    
#     if y>=max:
#         max = y
        
#     if z>=max:
#         max = z
        
#     return max
        

# print(largest(60, 50, 40))

# def tub_sonlar_top(min,max):
#     tub_sonlar = []
#     for n in range(min,max+1):
#         tub = True
#         if(n==1):
#             tub = False
#         elif(n==2):
#             tub = True
#         else:
#             for i in range(2,n):
#                 if(n%i==0):
#                     tub = False
#         if tub:
#             tub_sonlar.append(n)
#     return tub_sonlar

# print(tub_sonlar_top(1,20))






























