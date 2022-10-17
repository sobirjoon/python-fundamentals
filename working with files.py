# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 12:19:50 2022

@author: sobirjon
"""
import pickle

with open('info-pkl', 'rb') as file:
    a = pickle.load(file)
    b = pickle.load(file)

print(a)
print(b)


# studentA = {'ism':'hasan', 'familiya':'husanov', 'tyil':2003, 'kurs': 2}
# studentB = {'ism':'alijon', 'familiya':'valiyev', 'tyil':2004, 'kurs': 1}

# with open('info-pkl','wb') as file:
#     pickle.dump(studentA,file)
#     pickle.dump(studentB,file)




# filename = 'teachers.txt'

# with open(filename, 'w') as file:
#     for i in range(1,10000): 
#         file.write(f'{i}) Sobirjon Ergashev\n')


# for i in range(1,10):
#     with open(f'Teachers - {i}', 'w') as file:
#         for i in range(1,10):
#             file.write(f'{i}) Sobirjon Ergashev\n')



# filename = 'data/names.txt'

# convert file into list
# with open(filename) as file:
#     students = file.readlines()
# print(students)    


#remove '\n' in students
# students = [i.rstrip() for i in students]
# print(students)    


# with open(filename) as file:
#     for i in file:
#         print(i)



# with open(filename) as file:
#     names = file.read()
#     print(names)



# with open('pi.txt') as  file:
#     pi = file.read()
# print(pi)



# file = open('pi.txt')
# text = file.read()
# print(text)
# file.close()
