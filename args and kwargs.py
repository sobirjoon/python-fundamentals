# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 15:14:21 2022

@author: sobirjon
"""

# *args & **kwargs

# def total(*numbers):
#     totalSum = 0
#     for i in numbers:
#         totalSum += i
#     return totalSum

# print(total())
# print(total(1,65))
# print(total(1,2,3,4,5,6))


# def total(x,y,*numbers):
#     return x+y+sum(numbers)

# print(total(1,65,77,80))
# print(total(1,0,77,90))
# print(total(12,32,39,40,54,67))

# def studentsNames(firstName, lastName, **info):
#     info['firstName'] = firstName
#     info['lastName'] = lastName
#     return info

# student1 = studentsNames('Sobirjon', 'Ergashev', studentNum=40353633, email='sobirjone@outlook.com', ID=5058932)
# student2 = studentsNames('Muhammad', 'Nabijonov', studentNum=40336573, email='muhammadun@outlook.com', ID=5716033)

# print(student1)
# print(student2)


# def multiply(*numbers):
#     multiples = 1
#     for i in numbers:
#         multiples *= i
#     return multiples

# print(multiply(4,5,6,5)) 


# def student_info(first, last, **kwargs):
#     kwargs['firstName'] = first
#     kwargs['lastName'] = last
#     return kwargs

# student = student_info('sobirjon', 'olimov', birthyear = 2000, major='CIT', university = "Queen's University Belfast")
# print(student)

# def bankAccount (first, last, **kwargs):
#     kwargs['firstname']  = first
#     kwargs['lastname'] = last
#     return kwargs

# myAccount = bankAccount('Sobirjon', 'Ergashev', bankName = 'Barclays UK', bankAccountNumber = 403325594509, countryCode = 45)
# print(myAccount)









