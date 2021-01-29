# -*- coding: utf-8 -*-
"""
----------Phenix Labs----------
Created on Thu Jan 28 18:12:45 2021
@author: Gyan Krishna

Topic: queue
"""

queue = []

while(True):
    print("options:: ")
    print("1. enqueue")
    print("2. dequeue")
    print("3. display")
    print("4. exit")

    opt = int(input("enter your option :: "))

    if(opt == 1):
        num = int(input("enter element to be inserted :: "))
        queue.insert(0, num)
    elif(opt == 2):
        if(len(queue) == 0):
            print("queue underflow!")
        else:
            ele = queue[len(queue)-1]
            del queue[len(queue)-1]
    elif(opt == 3):
        print(queue)
    elif(opt == 4):
        break
    else:
        print("invalid option!")
