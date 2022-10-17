# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 15:07:48 2022

@author: sobirjon
"""

# RO'YXATNI TARTIBLASH


# sort() metodi 

# cars = ['bmw', 'mercedez benz', 'volvo', 'general motors', 'tesla', 'audi']
# cars.sort()
# print(cars)

# cars = ['Bmw', 'mercedez benz', 'volvo', 'general motors', 'tesla', 'audi']
# cars.sort()
# print(cars)

# cars = ['bmw', 'mercedez benz', 'volvo', 'general motors', 'tesla', 'audi']
# cars.sort(reverse=True) #ro'yhatni teskari tartibda saqlash uchun
# print(cars)


# sorted() funksiyasi asl ro'yhatni ketma-ketligini buzmagan holda tartiblaydi

# guests = ['Sobirjon', 'Ahmad', 'Liam', 'Orla', 'Muhammad', 'Mahmud']
# print("sorted()  >>> ", sorted(guests) )
# print("Asl ro'yxat o'zgarmadi: ", guests)
 
# print(sorted(guests, reverse=True))



# ages = [12, 45, 66, 42, 76, 53, 90]
# ages.sort()
# print(ages)
# print(sorted(ages, reverse=True))


# RO'YXATNI AYLANTIRISH - reverse() metodi

# fruits = ['pear', 'banana', 'apple', 'watermelon', 'lemon']
# fruits.reverse()
# print(fruits)


# RO'YXATNING UZUNLIGINI BILISH - len() funksiyasi

# fruits = ['pear', 'banana', 'apple', 'watermelon', 'lemon']
# fruits.append('mandarin')
# print("Elementlar soni:", len(fruits))

# range() funksiyasi

# numbers = list(range(0,11))
# print(numbers)

# even_numbers = list(range(1,100,4))
# print("Even numbers: ", even_numbers)

# SONLI RO'YXAT USTIDA SODDA AMALLAR

# costs = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# cheap = min(costs)
# expensive = max(costs)
# total = sum(costs)

# print("Cheap: " , cheap, "\nExpensive: ", expensive, "\nTotal cost: ", total)


# RO'YXATNI KESISH

cars = ['bmw', 'mercedez benz', 'volvo', 'general motors', 'tesla', 'audi']
# my_cars = cars[0:5]
# print(my_cars)

# new_car = cars[4]
# print("I have purchased a new car - ", new_car.upper())

# print(cars[2:5])
# print(cars[:4])
# print(cars[2:])


# RO'YXATDAN NUSXA OLISH

# numbers = [1, 2, 3, 4, 5]
# numbers2 = numbers
# numbers2.append(6)
# numbers2.append(7)
# print("numbers list: ", numbers)
# print("numbers2 list: ", numbers2)


# TUPLES - O'ZGARMAS RO'YXAT

# tuple_Is_immutable_sequence = (20, 30, 55.2)
# print(tuple_Is_immutable_sequence)


# toys = ('bus', 'car', 'bear', 'dino', 'snake', 'lizard')
# print(toys[0])
# print(toys[-1])
# print(toys[2:5])


# toys = ('bus', 'car', 'bear', 'dino', 'snake', 'lizard')
# toys = list(toys)

# toys.append('dragon')
# toys.remove('bus')
# toys[1] = 'mcqueen'
# toys = tuple(toys)
# print(toys)

# countries = ['United States', 'United Kingdom', 'Germany', 'Soviet Union', 'Uzbekistan', 'Japan']
# countries.append('North Korea')
# countries.append('Russia')
# countries.append('Turkey')

# print(countries)
# print("Length of list: ", len(countries))

# print(sorted(countries))

# reversed_list = sorted(countries, reverse=True)
# print(reversed_list)
# print(countries)

# countries.reverse()
# print(countries)

# numbers = list(range(120, 1200))
# print(numbers)
# print(sum(numbers))

# print(max(numbers) - min(numbers))
# print(len(numbers))

# print(numbers[:20])
# print(numbers[-20:])
# print(numbers[530:550])


foods = ['palov', 'cheeseburger', 'non-burger', 'shashlik', 'kebab']
breakfast = foods[:] # I just copied foods list to breakfast list
print(breakfast)

breakfast.remove('cheeseburger')
breakfast.remove('non-burger')
breakfast.remove('shashlik')
breakfast.append('norin')
breakfast.append('lavash')
breakfast.append('hot-dog')

print(breakfast)

breakfast = tuple(breakfast)









































