# -*- coding: utf-8 -*-
"""
----------Phenix Labs----------
Created on Sat Jan 23 22:41:46 2021
@author: Gyan Krishna

Topic: HCF andf LCM of tow numbers
"""

a = int(input("enter first number "))
b = int(input("enter second number "))


hcf = 1
small = min(a,b)
for i in range(1,small+1):
    if(a%i == 0 and b%i == 0):
        hcf = i
lcm = (a * b)/hcf
print("lcm = ",lcm)
print("hcf = ",hcf)