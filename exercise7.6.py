#!/usr/bin/env python
#-*- coding: utf-8 -*-

'''
Exercise7.6 Write a program that asks the user for two words. Then print all the char-
acters that the words have in common. You can consider capitals different from lower case
letters, but each character that you report, should be reported only once (e.g., the strings
“bee” and “peer” only have one character in common, namely the letter “e”). Hint: Gather
the characters in a third string, and when you ﬁnd a character that the two words have in
common, check if it is already in the third string before reporting it.
'''
try:
    word1 = input("Please input word number 1:")
    word2 = input("Please input word number 2:")
    result=set(word1) & set(word2)             #  Common uses include membership testing, removing duplicates from a sequence, and computing mathematical operations such as intersection, union, difference, and symmetric difference
    print(result)    
except ValueError:
    print("Error! Please input number!!!")
    
