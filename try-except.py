# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 17:21:06 2022

@author: sobirjon
"""

# while True:
#     yosh = input("Yoshingizni kiriting: ")
#     if yosh.isdigit():
#         yosh = int(yosh)
#         break        

# print(f"Siz {2022-yosh} yilda tug'ilgansiz")



# n = input("Butun son kiriting: ")
# try: 
#     n = int(n)
#     x = 20/n
# except ValueError:
#     print("Butun son kiritmadingiz!")
# except ZeroDivisionError:
#     print("0 bo'lib bo'lmaydi")
# else:
#     print(f"x={x}")


# FileNotFoundError
# filename = "data.txt" # bunday fayl mavjud emas
# with open(filename) as f:
#     text = f.read()



# user = {"username":"sariqdev",
#         "status":"admin",
#         "email":"admin@sariq.dev",
#         "phone":"99897123456"}

# key="baliq"
# try:
#     print(f'Foydalanuvchi: {user[key]}')
# except KeyError:
#     print("Bunday kalit mavjud emas")

# mevalar = ['olma', 'anor', 'anjir', 'uzum', 'banan']

# try:
#     print(mevalar[2])
# except IndexError:
#     print(f"Ro'yxatda {len(mevalar)} ta meva bor xolos")



# x, y = 5,10
# try:
#     y/(x-5)
# except ZeroDivisionError:
#     print("0 ga bo'lib bo'lmaydi.")



# age = input('Yoshingizni kiriting: ')
# try:
#     age = int(age)    
# except ValueError:
#     print("Butun son kiritmadingiz!") 
# else:
#     str = f"Siz {2022-age} yilda tug'ilgansiz!"
#     print(str)
    



# age = input('Yoshingizni kiriting: ')
# try:
#     age = int(age)    
# except:
#     print("Butun son kiritmadingiz!") 
# else:
#     str = f"Siz {2022-age} yilda tug'ilgansiz!"
#     print(str)
    
# print("Dastur tugadi.")


# age = input('Yoshingizni kiriting: ')
# try:
#     age = int(age)
#     str = f"Siz {2022-age} yilda tug'ilgansiz!"
#     print(str)
# except:
#     print("Butun son kiritmadingiz!")

# print("Dastur tugadi.")

