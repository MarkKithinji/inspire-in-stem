#!/usr/bin/python
#mark Victor
# 23| 5| 2022
####################################################################3


# its a scripting language ( no compiling)
#vvariables store data
#- camel casing

#from pickletools import markobject


#name= "mark"
#print( f"his name is "+ markobject)
#all characters are in single qotes
# a string is a list of character
# casting: ovnvrert from one data type to another
# for power use doublestar*
# for multiplication use one star



#print(1**2, 2**2, 3**2, 4**2, 5**2, 6**2, 7**2, 8**2, 9**2)

#adding tabs  \t
#print("monday\t tuesday\t wednesday\t")




#initializing dictionary ****************************************

#student = {"name": "mark", "age":"methusella", "gender":"male"}

#print(student['name']+ " is " + student['age'] + "'s" + " agemate coz he is " + student['gender'])

#adding pairs to dictionary
#student["id-number"] = "3024968"
#student["hobby"]="reading"
#student["football_preference"]="man city"

#print (student)

# to empty dictionary
#student={}
#student["home_city"]="nakuru" #adding new things to dictionary
#student["favourite_food"]= "ndengu"

#print (student)

#student["home_city"] = "Meru"#
#print (student)

#to remove anything, use the keyword, del
#del student ["favourite_food"]
#print (student)


from unicodedata import name


person = {'name': 'david spencer',
           'gender': 'female',
           'phone_number': '000',
           'location': 'Nattenda'}

person['age'] = '18'
person['fav_colour'] = 'jungle_green'
print (person.get('loction', 'the location is non existent'))