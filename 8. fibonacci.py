# -*- coding: utf-8 -*-
"""
----------Phenix Labs----------
Created on Sun Jan 24 00:01:55 2021
@author: Gyan Krishna

Topic:
"""

def fibonacci(n):
    fib=[0,1]
    a = 0
    b = 1
    for i in range(n):
        c = a + b
        a = b
        b = c
        fib.append(c)
    return fib
def isPrime(n):
    f = 0
    for i in range(2,n):
        if(n % i == 0):
            return False
    return True

ans = fibonacci(15)
print(ans)
print(ans[::-1])

fib2 = fibonacci(500)
ans2 = []
for i in fib2:
    if(isPrime(i)):
        ans2.append(i)
print(ans2)