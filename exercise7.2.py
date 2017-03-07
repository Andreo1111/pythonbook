#!/usr/bin/env python
#-*- coding: utf-8 -*-

'''
Exercise 7.2 If you did the previous exercise with a while loop, then do it again with a
for loop. If you did it with a for loop, then do it again with a while loop. If you did not
use a loop at all, you should be ashamed of yourself.
'''

try:

    number = int(input("Please input number :"))

    for i in range(1,11):
        mult = '{:^4d}*{:^4d}={:^4d}'.format(i,number,i*number)
        print(mult)

except NameError:
    print("Error! Please input number!!!")
