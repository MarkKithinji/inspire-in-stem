#!/usr/bin/python
# mark Victor
# 27| 5| 2022
# loops

# for number in range (0,20):
#     print('helleloliluuu')
#     break

# dict = {'chris': 'happy',
#         'johnny': 'sad',
#         'tim': 'beely'}

# print ()
##############################################################
# Python program to find.
# factorial of given number.
# import math
# def fact(n):
#      return(math.factorial(6))
# num = int(input("Enter the number:"))
# f = fact(num)
# print("Factorial of", num, "is", f)


##############################################################
number = int(input('enter the number'))
factorial = 1

if number <0:
    print (str("factorial of negative number does not exist"))

elif number ==0:
    print ("factorial of 0 is 1")

else:
    for i in range (1,number + 1):
        factorial = factorial * i

    print ("the factorial of ", number, "is", factorial  )