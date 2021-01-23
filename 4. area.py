# -*- coding: utf-8 -*-
"""
----------Phenix Labs----------
Created on Sat Jan 23 23:25:34 2021
@author: Gyan Krishna

Topic:
"""

from multipledispatch import dispatch
import math


class ComputeArea:
    #area of square
    @dispatch(int)
    def area(side):
        area = side * side
        return area

    #area of rectangle
    @dispatch(int, int)
    def area(l, b):
        area = l* b
        return area

    #area of a triangle
    @dispatch(int, int, int)
    def area(a,b,c):
        s = (a + b + c)/2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return area

    #area of rhombus
    @dispatch(float, float)
    def area(d1, d2):
        area = d1 * d2/ 2
        return area

    #area of a circle
    @dispatch(float)
    def area(r):
        area = 2 * math.pi * r * r
        return area


print("area of square is {}".format(ComputeArea.area(10)))
print("area of rectangle is {}".format(ComputeArea.area(10, 20)))
print("area of triangle is {}".format(ComputeArea.area(10, 20, 30)))
print("area of rhombus is {}".format(ComputeArea.area(2.5, 6.5)))
print("area of circle is {}".format(ComputeArea.area(3.5)))