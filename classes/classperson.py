#!/usr/bin/python
# mark Victor
# 02 |06 | 2022
# Classes

class person:
   def __init__(self, _name, _age):
        self.name= _name
        self.age= str(_age)

   def sayhie(self):
        print("hello, my name is "+ self.name+ " and i am "+ self.age)
    
    
person1 = person('Bob', 16)
person1.sayhie()

person2 = person('Alfred', 22)
person2.sayhie()
    