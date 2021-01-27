# -*- coding: utf-8 -*-
"""
----------Phenix Labs----------
Created on Sun Jan 24 21:37:01 2021
@author: Gyan Krishna

Topic: Sorting
"""

def bubbleSort(lst):
    l = len(lst)
    for i in range(l-1):
        for j in range(l-1-i):
            if(lst[j] < lst[j+1]):
                tmp = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = tmp
    print("bubble sort :: ",lst)

def selectionSort(lst):
    l = len(lst)
    for i in range(l):
        minimun = i
        for j in range(i,l):
            if(lst[minimun] < lst[j]):
                minimun = j
        tmp = lst[minimun]
        lst[minimun] = lst[i]
        lst[i] = tmp
    print("selection sort ::", lst)

def insertionSort(lst):




arr = [20, 65, 30, 42, 10, 5, 80]
bubbleSort(arr)
selectionSort(arr)