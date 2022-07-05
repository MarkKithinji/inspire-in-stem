#!/usr/bin/python
# mark Victor
# 23| 5| 2022
# If statements


# write a program that gets the user input and adds Ksh 10,000 to her account if she is btw ages 25 & 30 yrs

age = input(" what is your age")
gender = input ("specify your gender")
#name = input ("name of user")

acc_bal = 0

if (int (age> 25)) and (int(age <30)): 
    acc_bal = acc_bal + 10000
    print ("you have recieved Ksh 10,000")
else: 
    print("sorry, no money for you")


# write a program to withdraw Ksh 25000 if the account balance is btw Ksh 100,000 - 200,000
# if account balance is btw 500,000 and 1,000,000, tax 30%
# if account balance is above 1,000,000, deduct 15,000


