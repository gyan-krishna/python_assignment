# -*- coding: utf-8 -*-
"""
----------Phenix Labs----------
Created on Thu Jan 28 16:30:30 2021
@author: Gyan Krishna

Topic: Searching operations
"""

def linearSearch(lst, s):
    for i in range(len(lst)):
        if( lst[i] == s):
            return i
    return -1


def binarySearch(lst, s):
    l = 0
    r = len(lst) - 1

    while(l <= r):
        mid = int((l+r)/2)
        if(lst[mid] == s):
            return mid
        elif(lst[mid] < s):
            l = mid+1
        else:
            r = mid-1
    return -1

arr = [20, 65, 30, 42, 10, 5, 80]
arr.sort()
print("sorted array = ",arr)

s = int(input("enter search element ::"))

print("linear search :: ",linearSearch(arr, s))
print("binary search :: ",binarySearch(arr, s))
