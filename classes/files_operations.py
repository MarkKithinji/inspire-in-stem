#!/usr/bin/python
# mark Victor
# 03 |06 | 2022
# using verious commands

f= open('lesson.txt')# reading the file
print(f.read())
f.close()
with open('lesson_2.txt', 'w') as f:
     f.write('me programmers diary\n') 
     f.write('this is kinda fun')



f= open('lesson.txt')
print (f.readlines())


