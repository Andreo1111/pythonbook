#!/usr/bin/env python
#-*- coding: utf-8 -*-

'''
Exercise 7.3 Write a program that asks the user for ten numbers, and then prints the
largest, the smallest, and how many are dividable by 3. Use the algorithm described earlier
in this chapter.
'''

try:
    amax = 1
    bmin = 1
    cdiv = 0
    count = 1

    while count <= 3:
        number = int(input("Please input number :"))
        count +=1
        if amax <= number:
            amax = number  
            if (number %3) == 0:
                print('Divided on 3')
            print("Max",amax)
            continue
        if  bmin >=number:
            bmin = number
            if (number %3) == 0:
                print('Divided on 3')
            print("Min",bmin)            
            continue
        
       
except ValueError:
        
        print("Error! Please input number!!!")
    
