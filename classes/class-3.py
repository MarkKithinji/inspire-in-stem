# def_sum(num 1, num 2)

def power (number, power):
    pow_num= number**power

    return pow_num
print(power(6, 4))
    

def get_full_name (f_name, s_name):
    full_name= f_name+s_name
    return full_name

print( get_full_name('Mark', '.VK'))

'''
returning a Dictionary!!!! Epic  ((  *-*  ))
'''
def create_full_name (first_name, second_name):
        person= {'first': 'first_name',
             'second': 'second_name',
             'last': 'last_name'}
student = create_full_name('Alice', 'Wonderland')
print (student)

