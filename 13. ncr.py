# -*- coding: utf-8 -*-
"""
----------Phenix Labs----------
Created on Sun Jan 24 00:43:14 2021
@author: Gyan Krishna

Topic:
"""

def fact(n):
    if(n == 0):
        return 1;
    else:
        return fact(n-1)*n

def ncr(n,r):
    ans = fact(n)/(fact(r)*fact(n-r))
    return ans

n = int(input("enter n :: "))
r = int(input("enter c :: "))

print(ncr(n,r))