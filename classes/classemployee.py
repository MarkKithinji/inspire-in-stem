
#!/usr/bin/python
# mark Victor
# 02 |06 | 2022
# Classes


#make a class that will ahve employee name and aemplyee salary

class employee:
    def __init__(self, _id, _name, _salary):
        self.id= _id
        self.name= _name
        self.salary= _salary

        def info_bank(self):
            print("employee id "+ _id+"\n name "+ _name+"\n receives an average salary of "+ _salary)
            
employee_1= employee (10988, 'Njokie', 70000)