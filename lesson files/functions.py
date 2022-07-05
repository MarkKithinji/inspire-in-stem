#!/usr/bin/python
# mark Victor
# 27| 5| 2022
# functions

# a function is a block of code executed as one
## initializing function##
###calling function###

def say_hello():  ## initializing function##
    print ('Hello')

    x=4
    y=7
    z= x+y
    print (z)

say_hello()   ##calling function

def bark():
    print ('dogs bark')
    

def chew():
    print('i am animal')

def neigh():
    print('horse neighs')


bark()
chew()
neigh()


def add_numbers(x,y):  #parameter have been added. so function takes parameters x and y
    sum_numbers= x+y
    print ('The sum of numbers: ',sum_numbers)
add_numbers (40,50)
add_numbers (100,400)
add_numbers (1,4)


def other_nums(x,y):
    prod_nums= (x*y)
    print ('The sum of numbers: ',prod_nums)
other_nums (40,50)
other_nums (100,400)
other_nums (1,4)




