#!/usr/bin/python
# mark Victor
# 27| 5| 2022
# quadratic equations

a= int(input("enter coefficient of first term---"))
b= int(input("enter coefficient of second term---"))
c= int(input("enter coefficient of third term---"))



from cmath import sqrt 
import math
w=math.sqrt((b**2)-(4*a*c))

def find_roots (a, b, c):    #coefficient is the fig coming right before)
    y1 = ((-b+ w))/(2*a)
    y2 = ((-b- w))/(2*a)
    print("the roots of the quadratic eqn are",y1,y2)
find_roots(a,b,c)