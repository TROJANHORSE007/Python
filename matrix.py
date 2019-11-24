# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 12:09:14 2019

@author: Shubham
"""

a = []
print("First matrix")
for j in range(2):
    a.append([])
    for i in range(2):
        x=int(input("enter an number:-"))
        a[j].append(x)



b = []
print("second matrix")
for j in range(2):
    b.append([])
    for i in range(2):
        x=int(input("enter An number:-"))
        b[j].append(x)
        
        
c = []
for j in range(2):
    c.append([])
    for i in range(2):
        c[j].append(a[j][i] + b[j][i])
        
print(c)