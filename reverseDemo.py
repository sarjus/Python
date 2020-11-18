# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 03:54:08 2020
@author: Sarju S
Python Program to Reverse a Number using While loop.
"""
inputNumber = input("Enter an integer number to find the reverse:")
inputNumber = int(inputNumber)
reverseNumber = 0
while inputNumber>0:
    digit = inputNumber % 10
    reverseNumber = reverseNumber *10+digit
    inputNumber = inputNumber//10
#end of while loop
    
print("The reverse of the given number is:",reverseNumber)
    

