# '''type 1-100
#  if divisiblw by 3, type get_freeze_countif divisible by 5 type
#  if it si divisible by bot 3 and 5 type feez buzz'''

# '''type programm to reverse a string
# programm taking \unordered list of numbers and removes duplucates'''


num = 1
while num < 100:
    
    

    if (num %3==0) and (num%5!=0):
        print ('Feez!')

    elif (num%5==0) and (num%3!=0):
        print('Buzz!')
    
    elif (num%3!=0) and (num%5!=0):
        print (num)

    else:
        (num%3==0) and (num%5==0)
        print('Feez! Buzz!')

    num+= 1





 