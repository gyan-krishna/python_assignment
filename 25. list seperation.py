# -*- coding: utf-8 -*-
"""
----------Phenix Labs----------
Created on Fri Jan 29 15:00:58 2021
@author: Gyan Krishna

Topic: list seperation
"""

even = []
odd = []
lst = []

n = int(input("enter the number of elements ::"))

for i in range(n):
    lst.append(int(input("enter data :: ")))

for i in lst:
    if(i % 2 == 0):
        even.append(i)
    else:
        odd.append(i)

print("odd list  ::",odd)
print("even list ::",even)