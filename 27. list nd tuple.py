# -*- coding: utf-8 -*-
"""
----------Phenix Labs----------
Created on Fri Jan 29 15:15:01 2021
@author: Gyan Krishna

Topic: list of tuples
"""
def bubbleSort(lst):
    l = len(lst)
    for i in range(l-1):
        for j in range(l-1-i):
            if(lst[j][1] < lst[j+1][1]):
                tmp = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = tmp

    print("bubble sort    ::",lst)

n = int(input("enter the number of records ::"))
lst = []

for i in range(n):
    name =  str(input("enter name  :: "))
    marks = int(input("enter marks :: "))

    tup = (name, marks, )
    lst.append(tup)

print("original list :: ", lst)
bubbleSort(lst)