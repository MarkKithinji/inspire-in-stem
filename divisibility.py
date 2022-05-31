#!/usr/bin/python
# mark Victor
# 27| 5| 2022
# divisibilty



# num = int (input ("Enter a number : "))

# if (num%7==0)and(num%5==0):

#               print (f"The number {num} is divisible by 5 or 7.")

# else:
#             print(f"The number {num} isn't divisible by 5 or 7.")



number = int(input("enter number to check visibility ---"))
div_1= int(input("you want your number to be divisible by ---"))
div_2= int(input("enter another number (optional), to ignore, enter 0 --- "))
if (number%div_1==0) and (number% div_2==0):
    print ( f"the number is divisible by both {div_1} and {div_2}")
elif (number %div_1==0):
    print ( f"the number is not divisible by {div_1}")

elif div_2 == 0:
    print ( f"the number is not divisible by {div_1}")
elif (number%div_2==0):
    print ( f"the number is only divisible by {div_2}" )
else:
    print( f"the number is not divisible by both {div_1} and {div_2}" )
