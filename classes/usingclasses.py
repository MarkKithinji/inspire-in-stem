#!/usr/bin/python
# mark Victor
# 05 |06 | 2022
# Classes in action

reg_1= input("enter name...")
reg_2= input('enter name of organistion...')
import random
characters='qwertyuiopasdfghjklzxcvbnm,QWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*()1234567890'



for keys in range (1,2):
    card_no= ''
    for keys in range(1,6):
        card= random.choice(characters)
        card_no= card_no + card
    print('card no ready,', card_no)
    



class government:
    def __init__(self, reg_1, reg_2, card_no):
        self._name=reg_1
        self._org=reg_2
        self._membC=card_no

    def details(self):
        print("government realisation programme\n".upper,self._name," is recognised as member of", self._org,". \nthe official membership card number is"+ str(self._membC)+" good luck")
        print('check point 2')


agent_1=government('reg_1', 'reg_2',' card_no')
agent_1.details()


'''import string
import random


## characters to generate password from
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_random_password():
	## length of password from the user
	length = int(input("Enter password length: "))

	## shuffling the characters
	random.shuffle(characters)
	
	## picking random characters from the list
	password = []
	for i in range(length):
		password.append(random.choice(characters))

	## shuffling the resultant password
	random.shuffle(password)

	## converting the list to string
	## printing the list
	print("".join(password))



## invoking the function
generate_random_password()'''