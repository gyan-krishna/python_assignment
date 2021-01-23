# -*- coding: utf-8 -*-
"""
----------Phenix Labs----------
Created on Sun Jan 24 00:39:16 2021
@author: Gyan Krishna

Topic:
"""

def isPrime(n):
    for i in range(2,n):
        if(n % i == 0):
            return False
    return True

r1 = int(input("enter lower range:: "))
r2 = int(input("enter upper range:: "))

print("twin primes nos in given range is ::")
for i in range(r1,r2-1,1):
    if(isPrime(i) and isPrime(i + 2)):
        print(i, " ", i+2 )
