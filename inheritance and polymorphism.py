# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 17:33:39 2022

@author: sobirjon
"""
class Person:
    def __init__(self, name, surname, passport, birthyear):
        self.name = name
        self.surname = surname
        self.passport = passport
        self.birthyear = birthyear 
        
    def get_info(self):
        info = f"{self.name} {self.surname} - "
        info += f"Passport: {self.passport}, {self.birthyear} - year"
        return info 

    def get_age(self, year):
        return year - self.birthyear
        
    
class Student(Person):
    def __init__(self, name, surname, passport, birthyear, idnumber, address, subjects):
        super().__init__(name, surname, passport, birthyear)
        self.idnumber = idnumber
        self.level = 1
        self.address = address
        self.subjects = []
        
    def get_id(self):
        return self.idnumber
    
    def get_level(self):
        return self.level
        
    def get_info(self):
        info = f"{self.name} {self.surname}."
        info += f"{self.get_level()} - level. \nID number: {self.idnumber} "
        return info
    
    
class Address:
    def __init__(self, house, street, district, province):
        self.house = house
        self.street = street 
        self.district = district
        self.province = province
    
    def get_address(self):
        address = f"{self.house} - house, {self.street} street, "
        address += f"{self.district} district, {self.province} province, Uzbekistan"
        return address
 






















# address = Address(12,'Paxtakor',"Marhamat","Andijan")
# student = Student("Valijon", "Aliyev", "FA112299", 2000, "0000012", address)

# print(student.address.get_address())
# print(student.address.district)

# student = Student("Sobirjon", "Ergashev", "FA0035332", 2000, '0000012')
# print(f"{student.get_info()}. \nID number: {student.get_id()}")
# print(f"{student.get_level()} - level student at QUB")












