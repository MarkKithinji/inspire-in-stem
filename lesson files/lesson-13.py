#!/usr/bin/python
#mark Victor
# 23| 5| 2022


#squares = []  #empty list

#for numbers in range (0, 10):
 #   square = numbers **2
 #   squares . append(square)
#
#print (squares)

#x = []

#for numbers in range (0,10, 2):
 #   cubes = numbers **3
  #  x . append (cubes)
    
#print (x)

sum = 0

for numbers in range (0, 10):
    sum = sum + numbers

print (sum)

# finding product of numbers
sum_num = 0
prod_num = 1

for number in range (0,50):
    if  (number%2)==1:
        prod_num = prod_num*number
        
print (prod_num)