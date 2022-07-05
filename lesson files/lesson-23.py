#!/usr/bin/python
# mark Victor
# 27| 5| 2022
# arithmetic progression




a = int(input("enter first number---"))
b= int(input("enter first number---"))
n=int(input("enter value of number---"))
d = int(input("entervalue of d---"))
for i in range (1,n+1):
    n_term=a+(i-1)*d
    print(n_term)


sum_n=(n_term/2)* (2*a + (n-1)* d)
print (sum_n)



