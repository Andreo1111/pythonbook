#!/usr/bin/env python
#-*- coding: utf-8 -*-

'''
Exercise 7.4 “99 bottles of beer” is a traditional song in the United States and Canada. It
is popular to sing on long trips, as it has a very repetitive format which is easy to memorize,
and can take a long time to sing. The song’s simple lyrics are as follows: “99 bottles of beer
on the wall, 99 bottles of beer. Take one down, pass it around, 98 bottles of beer on the
wall.” The same verse is repeated, each time with one fewer bottle. The song is completed
when the singer or singers reach zero. Write a program that generates all the verses of the
song (though you might start a bit lower, for instance with 10 bottles). Make sure that your
loop is not endless, and that you use the proper inﬂection for the word “bottle.”
'''

try:
    botle = int(input("Please input number botle:"))
    song1 = " bottles of beer on the wall,"
    song2 = " bottles of beer "
    r = range(botle+1)
    for i in r[::-1]:
        
        print(i,song1,i,song2)    
except ValueError:
        
        print("Error! Please input number!!!")
    
