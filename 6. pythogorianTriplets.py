# -*- coding: utf-8 -*-
"""
----------Phenix Labs----------
Created on Sat Jan 23 23:39:27 2021
@author: Gyan Krishna

Topic:
"""

a = int(input("enter a"))
b = int(input("enter b"))
c = int(input("enter c"))

a = a**2
b = b**2
c = c**2

if( a + b == c or b + c == a or c + a == b):
    print("pythogorian triplet")
else:
    print("not pythogorian triplet")