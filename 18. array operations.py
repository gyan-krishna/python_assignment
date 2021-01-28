# -*- coding: utf-8 -*-
"""
----------Phenix Labs----------
Created on Thu Jan 28 16:42:30 2021
@author: Gyan Krishna

Topic: array operations
"""
def linearSearch(lst, s):
    for i in range(len(lst)):
        if( lst[i] == s):
            return i
    return -1

arr = [20, 65, 30, 42, 10, 5, 80]
while(True):
    print("options:: ")
    print("1. insert element")
    print("2. search element")
    print("3. delete element")
    print("4. display the array")
    print("5. exit")

    opt = int(input("enter your option :: "))
    if(opt == 1):
        num = int(input("enter element to be inserted :: "))
        pos = int(input("enter position to insert at  :: "))

        arr.insert(pos, num)

    elif(opt == 2):
        num = int(input("enter element to be searched :: "))
        pos = linearSearch(arr, num)

        if(pos == -1):
            print("element not found!")
        else:
            print("element found at position ", pos)
    elif(opt == 3):
        pos = int(input("enter position to delete element from:: "))
        del arr[pos]
    elif(opt == 4):
        print(arr)
    elif(opt == 5):
        break
    else:
        print("invalid option!")