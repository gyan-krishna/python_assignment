# -*- coding: utf-8 -*-
"""
----------Phenix Labs----------
Created on Sun Jan 24 00:13:48 2021
@author: Gyan Krishna

Topic:
"""

def isPrime(n):
    f = 0
    for i in range(2,n):
        if(n % i == 0):
            return False
    return True

def isArmstrong(n):
    sum = 0
    copy = n
    while(copy > 0):
        d = copy % 10
        sum += d**3
        copy = int(copy/10)

    if(n == sum):
        return True
    else:
        return False

def isPalindrome(n):
    rev = 0
    copy = n
    while(n > 0):
        d = n % 10
        rev = rev * 10 + d
        n = int(n/10)
    if(copy == rev):
        return True
    else:
        return False


def isPerfect(n):
    sum = 0
    for i in range(1,n):
        if(n % i == 0):
            sum += i
    if(n == sum):
        return True
    else:
        return False

def isKrishnamurthy(n):
    copy = n
    sum = 0
    while(copy > 0):
        d = copy % 10
        f = 1
        for i in range(1,d+1):
            f *= i
        sum += f
        copy = (int)(copy / 10)
    if(sum == n):
        return True
    else:
        return False


r1 = int(input("enter lower range:: "))
r2 = int(input("enter upper range:: "))

print("primes nos in given range is ::")
for i in range(r1,r2,1):
    if(isPrime(i)):
        print(i)


print("armstrong numbers b/w 100-999 is :: ")
for i in range(100,1000):
    if(isArmstrong(i)):
        print(i)

print("perfect nos in given range is ::")
for i in range(r1,r2,1):
    if(isPerfect(i)):
        print(i)

print("krishnamurthy nos in given range is ::")
for i in range(r1,r2,1):
    if(isKrishnamurthy(i)):
        print(i)

n = int(input("enter a number"))
if(isPalindrome(n)):
    print("palindrome")
else:
    print("not palindrome")