# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 14:09:28 2022

@author: sobirjon
"""
#28-DARS. KLASSLAR

class Student:
    
    def __init__(self, firstName, lastName, birthOfYear):
        
        self.firstName = firstName
        self.lastName = lastName
        self.birthOfYear = birthOfYear
        self.level = 1
        
    def get_info(self):
        return f"{self.firstName} {self.lastName}. {self.birthOfYear}. {self.level}"


    def set_level(self, level):
        self.level = level
    
    def update_level(self):
        if self.level < 4:
            self.level += 1
        elif self.level == 'Graduated':
            return None
        else:
            self.level = 'Graduated'


class Subject:
    def __init__(self, title):
        self.title = title 
        self.studentsNum = 0
        self.students = []
        
    def add_student(self, student):
        self.students.append(student)
        self.studentsNum += 1
        
    def get_students(self):
        return [student.get_info() for student in self.students]
    
maths = Subject('Mathematics for CS')
student1 = Student("Sobirjon", "Ergashev", 2000)
student2 = Student("Hasan", "Husanov", 2002)
student3 = Student("Husanboy", "Hasanov", 2002)

maths.add_student(student1)
maths.add_student(student2)
maths.add_student(student3)

print(maths.studentsNum)
print(maths.get_students())



def see_methods(klass):
    return [method for method in dir(klass) if method.startswith('__') is False]

print(see_methods(Student))
























# class Student:
#     def __init__(self, name, surname, birthyear):
#         self.name = name
#         self.surname = surname
#         self.birthyear = birthyear
        
#     def bankAccountOfUser():
#         pass
    
#     def getUserEmail():
#         pass
        
#     def getName(self):
#         return self.name
    
#     def getSurName(self):
#         return self.surname
    
#     def getFullName(self):
#         return f"{self.name} {self.surname}"
        
        
#     def tellme(self):
#         return f"Full name {self.name} {self.surname}, {self.birthyear}"


