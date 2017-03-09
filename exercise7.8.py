#!/usr/bin/env python
#-*- coding: utf-8 -*-

'''
Exercise 7.8 Write a program that takes a random integer between 1 and 1000 (you can
use the randint() function for that). The program then asks the user to guess the number.
After every guess, the program will say either “Lower” if the number it took is lower,
“Higher” if the number it took is higher, and “You guessed it!” if the number it took is
equal to the number that the user entered. It will end with displaying how many guesses
the user needed. It might be wise, for testing purposes, to also display the number that the
program randomly picks, until you are sure that the program works correctly.
'''

from random import randint


try:
    rand = randint(1,1000)
    while True:
        user_number = int(input("Please input number from 1 to 1000 : "))
        if user_number < rand:
            print("Higher")
            continue
        elif user_number == rand:
            print("You guessed it!")
            exit()
        elif user_number > rand:
            print("Lower")
            continue
except ValueError:
    print("Error! Please input number!!!")
    
