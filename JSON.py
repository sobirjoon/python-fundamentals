# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 14:28:20 2022

@author: sobirjon
"""

import json

# myself = {
#     'name':'sobirjon',
#     'surname':'ergashev',
#     'age':22,
#     'ID':40353633,
#     'citizenship':'uzbekistan',
#     'medical_drugs': [
#         {'title':'magnesium B6'},
#         {'title':'growth hormone'}
#         ]
    
#     }

# with open('myself.json', 'w') as file:
#     json.dump(myself, file)

filename = 'myself.json'
with open(filename) as file:
    myself = json.load(file)

print(myself)


# myself_json = json.dumps(myself, indent=3)
# print(myself_json)