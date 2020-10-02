# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 22:29:57 2020

@author: aKt
"""

#getting the no from user
p = int(input("Enter Prime Number P:"))
q = int(input("Enter Prime Number q:"))

#getting the values from to key exchangers
a = int(input("Enter values for Aditya:"))
b = int(input("Enter values for Rachit:"))

A = (q^a)%p
R = (q^b)%p

print("Exchange of values take place ")
A_key = (R^a)%p #Aditya's secret key
R_key = (A^b)%p #Rachit's secret key

print("Aditya's secret key is : ",A_key)
print("Rachit's secret key is : ",R_key)