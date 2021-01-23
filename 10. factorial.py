# -*- coding: utf-8 -*-
"""
----------Phenix Labs----------
Created on Sun Jan 24 00:36:03 2021
@author: Gyan Krishna

Topic:
"""

def fact(n):
    if(n == 0):
        return 1;
    else:
        return fact(n-1)*n

print(fact(4))