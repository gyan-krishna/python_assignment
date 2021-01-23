# -*- coding: utf-8 -*-
"""
----------Phenix Labs----------
Created on Sat Jan 23 22:46:47 2021
@author: Gyan Krishna

Topic:
"""
import sys

print("welcome to calculator app")
a  = int( input("enter opperand 1"))
op = str( input("enter operator"))
b  = int( input("enter opperand 2"))

res = 0

try:
    if(op == '+'):
        res = a + b
    elif(op == '-'):
        res = a - b
    elif(op == '/'):
        res = a / b
    elif(op == '*'):
        res = a * b
    elif(op == '%'):
        res = a % b
    else:
        print("unknown operator")
        sys.exit()
except:
    print("error!", sys.exc_info()[0])
    sys.exit()

print("{} {} {} = {}".format(a,op,b,res))