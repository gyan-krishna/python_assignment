# -*- coding: utf-8 -*-
"""
----------Phenix Labs----------
Created on Sun Jan 24 00:45:47 2021
@author: Gyan Krishna

Topic:
"""

def fact(n):
    if(n == 0):
        return 1;
    else:
        return fact(n-1)*n


n = int(input("enter x :: "))
x = int(input("enter n :: "))

sign = 1
p = 1
sum = 0


for i in range(n):
    sum += (x**p/fact(p))* sign
    p += 2
    sign *= -1

print(sum)

