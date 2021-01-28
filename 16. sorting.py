# -*- coding: utf-8 -*-
"""
----------Phenix Labs----------
Created on Sun Jan 24 21:37:01 2021
@author: Gyan Krishna

Topic: Sorting
"""
#-----------------------------------------------------------------------------#
def bubbleSort(lst):
    l = len(lst)
    for i in range(l-1):
        for j in range(l-1-i):
            if(lst[j] < lst[j+1]):
                tmp = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = tmp
    print("bubble sort    ::",lst)
#-----------------------------------------------------------------------------#
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
#-----------------------------------------------------------------------------#
def insertionSort(lst):
    l = len(lst)
    for i in range(1, l):
        key = lst[i]
        j = i - 1
        while(j >= 0 and lst[j] < key):
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = key
    print("insertion sort ::", lst)
#-----------------------------------------------------------------------------#
def merge(lst, l, r):

    leftLst = []
    rightLst = []
    mid = int((l + r)/2)


    for i in range(l,mid+1):
        leftLst.append(lst[i])

    for i in range(mid+1,r+1):
        rightLst.append(lst[i])

    leftIndex = 0
    rightIndex = 0
    index = l

    while(leftIndex < len(leftLst) and rightIndex < len(rightLst)):
        if(leftLst[leftIndex] >= rightLst[rightIndex]):
            lst[index] = leftLst[leftIndex]
            leftIndex += 1
        else:
            lst[index] = rightLst[rightIndex]
            rightIndex += 1
        index += 1

    while(leftIndex < len(leftLst)):
            lst[index] = leftLst[leftIndex]
            leftIndex += 1
            index += 1

    while(rightIndex < len(rightLst)):
            lst[index] = rightLst[rightIndex]
            rightIndex += 1
            index += 1

def mergeSort(lst, l, r):
    if(r > l):
        mid = int((l+r)/2)
        mergeSort(lst, l, mid)
        mergeSort(lst, mid+1, r)

        merge(lst, l, r)
#-----------------------------------------------------------------------------#
def partition(lst, l, r):
    pivot = lst[r]
    i = l-1

    for j in range(l, r):
        if(lst[j] > pivot):
            i += 1
            tmp = lst[i]
            lst[i] = lst[j]
            lst[j] = tmp
    tmp = arr[r]
    arr[r] = arr[i+1]
    arr[i+1] = tmp
    return i+1

def quickSort(lst, l, r):
    if(l < r):
        part = partition(lst, l, r)
        quickSort(arr, l, part-1)
        quickSort(arr, part+1, r)
#-----------------------------------------------------------------------------#


#-----------------------------------------------------------------------------#

#                                     testing
arr = [20, 65, 30, 42, 10, 5, 80]
bubbleSort(arr)

arr = [20, 65, 30, 42, 10, 5, 80]
selectionSort(arr)

arr = [20, 65, 30, 42, 10, 5, 80]
insertionSort(arr)

arr = [20, 65, 30, 42, 10, 5, 80]
mergeSort(arr,0,len(arr)-1)
print("merge sort     ::", arr)

arr = [20, 65, 30, 42, 10, 5, 80]
quickSort(arr,0,len(arr)-1)
print("Quick sort     ::", arr)
