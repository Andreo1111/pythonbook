#!/usr/bin/env python
#-*- coding: utf-8 -*-

'''
Exercise 7.5 The Fibonacci sequence is a sequence of numbers that starts with 1, followed
by 1 again. Every next number is the sum of the two previous numbers. I.e., the sequence
starts with 1, 1, 2, 3, 5, 8, 13, 21,... Write a program that calculates and prints the Fibonacci
sequence until the numbers get higher than 1000.
'''

try:
    a,b = 0,1
    while a < 1000:
        print(a,end=" ")        
        a,b = b,a+b
    print()
            
except ValueError:
    print("Error! Please input number!!!")
    
