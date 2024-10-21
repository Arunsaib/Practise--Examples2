##Question1:
##Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
##Note: i=0,1.., X-1; j=0,1,¡­Y-1.
##Example
##Suppose the following inputs are given to the program:
##3,5
##Then, the output of the program should be:
##[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 
# --solution
from numpy import *

Num1= int(input("How many rows You need:- "))

Num2= int(input("How many columns you need:- "))

arr= zeros((Num1,Num2)) #Creating a 2D array with zeros
for i in range(Num1):
    for j in range(Num2):
         arr[i,j]= i*j

print("The Resultant Matrix is the product of Indices, it as follows like this...")
print(arr)         
