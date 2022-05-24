from operator import truediv


a = ["banana, apple, microsoft, huawei"]
for element in a:
    print(element)
    print(element)

b = ("20,30,60")
#for n in b:
    #total = 0
    #total= total + n
#print (total)
    
for number in range(1, 20, 2):
    print ("attempt", number ,(number ) * ".")

successful = False
for number in range (1,20,3):
    print("attempt")
    if successful:
        print("successful")
        break

else:
    print ("attempted 10 times and failed")