# -*- coding: utf-8 -*-
"""
----------Phenix Labs----------
Created on Thu Jan 28 18:03:32 2021
@author: Gyan Krishna

Topic: Stack
"""

stack = []

while(True):
    print("options:: ")
    print("1. push")
    print("2. pop")
    print("3. display")
    print("4. exit")

    opt = int(input("enter your option :: "))

    if(opt == 1):
        num = int(input("enter element to be pushed :: "))
        stack.append(num)
    elif(opt == 2):
        if(len(stack) == 0):
            print("stack underflow!")
        else:
            ele = stack[len(stack)-1]
            del stack[len(stack)-1]
    elif(opt == 3):
        print(stack)
    elif(opt == 4):
        break
    else:
        print("invalid option!")