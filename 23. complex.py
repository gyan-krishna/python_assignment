# -*- coding: utf-8 -*-
"""
----------Phenix Labs----------
Created on Fri Jan 29 14:12:45 2021
@author: Gyan Krishna

Topic:
"""

class Complex:

    def __init__(self, r, i):
        self.real = r
        self.img = i

    def add(c1, c2):
        r = c1.real + c2.real
        i = c1.img + c2.img

        sum = Complex(r, i)
        return sum

    def sub(c1, c2):
        r = c1.real - c2.real
        i = c1.img - c2.img

        sub = Complex(r, i)
        return sub

    def mul(c1, c2):
        r = c1.real*c2.real + c1.img * c2.img
        i = c1.real*c2.img  + c1.img * c2.real

        mul = Complex(r, i)
        return mul

    def show(self):
        print(" ({}, {}i)".format(self.real, self.img))


r = int(input("enter real part of num 1      ::"))
i = int(input("enter imaginary part of num 1 ::"))
c1 = Complex(r,i)

r = int(input("enter real part of num 1      ::"))
i = int(input("enter imaginary part of num 1 ::"))
c2 = Complex(r,i)

sum = Complex.add(c1,c2)
diff = Complex.sub(c1,c2)
pro = Complex.mul(c1, c2)

print("complex number 1 ::",end="")
c1.show()
print("complex number 2 ::",end="")
c2.show()

print("sum              ::",end="")
sum.show()

print("differrence      ::",end="")
diff.show()

print("product          ::",end="")
pro.show()