# -*- coding: utf-8 -*-
"""
----------Phenix Labs----------
Created on Thu Jan 28 18:18:33 2021
@author: Gyan Krishna

Topic: matrix operations
"""
def displayMat(mat):
    for i in range(len(mat)):
        print(mat[i])

n = int(input("enter the size of the matrix ::"))

print("enter first matrix ::")
mat1 = [[1,2,3],[4,5,6],[7,8,9]]
mat2 = [[1,2,3],[4,5,6],[7,8,9]]

# mat1 = []
# for i in range(n):
#     tmp = []
#     for j in range(n):
#         tmp.append(int(input()))
#     mat1.append(tmp)

# print("enter second matrix ::")
# mat2 = []
# for i in range(n):
#     tmp = []
#     for j in range(n):
#         tmp.append(int(input()))
#     mat2.append(tmp)

# addition of two matrix
add = []
for i in range(n):
    tmp = []
    for j in range(n):
        sumTemp = mat1[i][j] + mat2[i][j]
        tmp.append(sumTemp)
    add.append(tmp)

# substraction of two matrix
sub = []
for i in range(n):
    tmp = []
    for j in range(n):
        subTemp = mat1[i][j] - mat2[i][j]
        tmp.append(subTemp)
    sub.append(tmp)

# transpose of two matrix
transpose = [[0]*n]*n
for i in range(n):
    for j in range(n):
        transpose[i][j] = mat1[j][i]

flag = True
for i in range(n):
   for j in range(n):
       if(not(i == j and mat1[i][j] == 1)):
           flag = False
           break
if(flag == True):
    print("identity matrix")
else:
    print("not identity matrix")


print("matrix 1:: ")
displayMat(mat1)

print("matrix 2:: ")
displayMat(mat2)

print("sum :: ")
displayMat(add)

print("differrence:: ")
displayMat(sub)

print("transpose:: ")
displayMat(transpose)

