
get_pali= input('enter a number to check if it is a palindrome')


num= input('enter any number')

try:
    val= int(num)
    if num == str(num)[::-1]:
        print ('the number given is a palendrome')

    else:
        print('the number given is not a palendrome')

except ValueError:
    print('the number given is not a viable number')

try:
    N_val= num
    if N_val== (num)[::-1]:
        print('the given number is a palindrome')

    else:
        print("the given number is not a palindrome")
except ValueError:
    print('the word given is not a palendrome')


