# -*- coding: utf-8 -*-
"""
----------Phenix Labs----------
Created on Fri Jan 29 14:07:35 2021
@author: Gyan Krishna

Topic:
"""

class Rectangle:
    def __init__(self, l, b):
        self.length = l
        self.breadth = b

    def showArea(self):
        area = (self.length * self.breadth)
        print("area = ", area)

    def showPerimeter(self):
        per = 2 * (self.length + self.breadth)
        print("peremeter = ", per)

l = int(input("enter length  ::"))
b = int(input("enter breadth ::"))

obj = Rectangle(l,b)
obj.showPerimeter()
obj.showArea()