# -*- coding: utf-8 -*-
"""
----------Phenix Labs----------
Created on Thu Jan 28 18:03:32 2021
@author: Gyan Krishna

Topic: Stack
"""

arr = []

while(True):
    print("options:: ")
    print("1. push")
    print("2. pop")
    print("3. display")
    print("4. exit")

    opt = int(input("enter your option :: "))

    if(opt == 1):
        num = int(input("enter element to be pushed :: "))
        arr.append(num)
    elif(opt == 2):
        if(len(arr) == 0):
            print("stack underflow!")
        else:
            ele = arr[len(arr)-1]
            del arr[len(arr)-1]
    elif(opt == 3):
        print(arr)
    elif(opt == 4):
        break
    else:
        print("invalid option!")