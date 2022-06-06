#!/usr/bin/python
# mark Victor
# 03 |06 | 2022
# Classes

class vehicle:
    def __init__(self, maximum_speed, mileage):
        self.speed= maximum_speed
        self.distance= mileage

    def details(self):
        print(self.speed+ self.distance)
print('Toyota information....'.upper())
Toyota= vehicle(str('55Km/H\n'), str('23344 miles\n'))
Toyota.details()

print('KartDrive information.....'.upper())
KartDrive= vehicle(str('80 Knots\n'), str('6604545nm'))
KartDrive.details()


# class students:
#     def __init__(self, name, gender, adm_no):
#         self.name= 

#Wtransfer this to password file
import random

print('Welcome to Android Password Generator')

num_passwords= int(input("How many passwords do you want?---"))


pass_length= int(input("length_password---"))



for pwd in range ( num_passwords):
    passwords=''
    for c in range (pass_length):
        
        passwords+=random.choice
print (passwords)





