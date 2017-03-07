#!/usr/bin/env python
#-*- coding: utf-8 -*-

'''
Exercise 7.1 Write a program that lets the user enter a number. Then the program dis-
plays the multiplication table for that number from 1 to 10. E.g., when the user enters 12,
the ﬁrst line printed is “1 * 12 = 12” and the last line printed is “10 * 12 = 120”.
'''
try:
    number = int(input("Please input number :"))
    count = 1
    while count <=10:
        multi = ' {:^4d}  *  {:^4d}  = {:^4d}'.format(count,number,(count*number))
        count +=1
        print(multi)
except ValueError:
    print("Please enter number!!!")
