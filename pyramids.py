#!/usr/bin/python
# mark Victor
# 27| 5| 2022
# half pyramid

# rows = int(input ("enter number of rows:"))

# for i in range (rows):
#     for j in range (i+1):
#         print("*",ends ="")
#         print("\n")

rows = int(input ("enter number of rows:"))

for i in range (rows):
    for j in range (i+1):
        print("* ",ends ="")
    print("\n")


# row= int(input("enter name"))
# for i in range (rows):
#     for j in range (i+1):
#         print (j+1)


###########################################################

rows = int(input("enter number of rows"))
k = 0
for i in range (1,rows+1):
    for space in range(1,(rows-i)+1):
        print(end="")
while k!=(2*i-1):
    print("*", end = "")