# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 10:01:23 2022

@author: sobirjon
"""
# orders = ['olma', 'anjir', 'qovun', 'uzum', 'nok','shaftoli']
# products = {
#     'olma':20000,
#     'tarvuz':25000,
#     'uzum':10000,
#     'shaftoli':15000    
#     }

# while orders:
#     order = orders.pop()
#     if order in products.keys():
#         cost = products[order]
#         print(f"{order.title()} - {cost} so'm")
#     else:
#         print(f"Bizda {order} yo'q!")

# basket = []
# while True:
#     product = input("Savatga mahsulot qo'shing: ")
#     basket.append(product)
#     response = input("Yana mahsulot qo'shasizmi? (ha/yo'q): ")
#     if response.lower() != 'ha':
#         break



# students = [
#   'Авазбек',
#   'Хуршидбек',
#   'Собиржон',
#   'Оллоберди',
#   'Аббосбек',
#   'Собиржон',
#   'Мухаммад',
#   'Азамат'
#   ]

# graded_students = {}

# while students:
#     i = students.pop()
#     grade = input(f"{i.title()}нинг баҳосини киритинг: ")
#     print(f"{i.title()} баҳоланди.")
#     graded_students[i] = grade


# friends = [
#   'Собиржон',
#   'Авазбек',
#   'Хуршидбек',
#   'Собиржон',
#   'Оллоберди',
#   'Собиржон',
#   'Аббосбек',
#   'Собиржон',
#   'Мухаммад',
#   'Собиржон',
#   'Собиржон',
#   'Азамат'
#   ]


# while 'Собиржон' in friends:
#     friends.remove('Собиржон')
# print(friends)





# print("<< Дўстларни ёшини сақлаймиз! >>")
# friends = {}
# flag = True 
# while flag:
#     name = input("Дўстингизни исмини ёзинг: ")
#     age = input(f"{name.title()}нинг ёшини киритинг: ")
#     friends[name] = int(age)
    
#     response = input("Яна маълумот қўшасизми? (ҳа/йўқ): ")
#     if response == "йўқ":
#         flag = False
        
# for k, v in friends.items():
#     print(f"{k.title()} {v} ёшда")


# friends = {'Собиржон': 22,
#  'Авазбек': 22,
#  'Хуршидбек': 23,
#  'Оллоберди': 23,
#  'Аббосбек': 22,
#  'Мухаммад': 24,
#  'Азамат': 25}





# names = []

# print("<< ДЎСТЛАР РЎЙХАТИ >>")
# n = 1

# while True:
#     prompt = f"{n}-дўстингизни исмини ёзинг: "
#     name = input(prompt)
#     names.append(name)
#     response = input("Яна исм қўшасизми? (ҳа/йўқ): ")
#     if response.lower() == 'ҳа':
#         n+=1
#         continue
#     else:
#         break


# print("\n>> ДЎСТЛАР РЎЙХАТИ: ")
# for i in names:
#     print(i.title())




