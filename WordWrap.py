# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 15:54:43 2022

@author: sobirjon
"""

# Python version of WordWrap
# Read word from KB

word = input("Enter a single word: ")

# Display the word
print(word)

# some required data
len = len(word)  # get the length of word
numLines = len-2    # len-2 lines to display
index1 = 1     # initial index for 1st character
index2 = len-2     # initial index for 2nd character
gap = len-2     # gap between characters

# display middle characters
for count in range(numLines):
    # output 1st character
    print( word[index1], end="" )
    index1 = index1 + 1 # move index1 up 1
    # output spaces
    for space in range(gap):
        print(' ', end="");
    
    # output 2nd character
    print( word[index2] )
    index2 = index2 - 1 # move index2 down 1
    
# display word in reverse
for count in range(len-1,-1,-1):
    print(word[count], end="")
print()