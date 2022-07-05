#!/usr/bin/python
# mark Victor
# 05 |06 | 2022
# password generator
# print('WELCOME TO PASSWORD GENERATOR\n intiating sign in...')

e_mail= str(input('Enter Email address in this formart (myadress123@youmail.com)\n---'))


try:
    f= open ('databank.txt')
    try:
        lines= f.readlines()
    except:
        print ('error 40')
    finally:
        f.close()
except:
    print ('could not retrieve password')

#  with open ('databank.txt') as f:
#      lines= f.readlines()
#      print(lines)
    

'''   print (lines)
    for i in lines:
         if i != E_mail:
             print ('Email address is not recognised, consider rechecking the spelling or signing up')
             sign_up= input('do you wish to sign in\n yes\t no\n...')
             if sign_up== 'yes':
                 from asyncore import write


                 print('PASSWORD GENERATOR SIGN-UP\n\n')



                 user_fname= input('enter your first name\n...')
                 user_lname= input('enter your last name\n...')
                 user_phone= input ('enter your phone number')
                 E_mail= input('nenter your email address\n...')
                 conf= input('please confirm your email address\n...')
                 while E_mail != conf:
                     print('E-mails do not match, retry')
                     E_mail= input('nenter your email address\n...')
                     conf= input('please confirm your email address\n...')

                 else:
                     print('uploading data...')
                    
                    
                 with open ('databank.txt', 'w') as f:
                     f.write(user_fname)
                     f.write('\n')
                     f.write(user_lname)
                     f.write('\n')
                     f.write(E_mail)
                     f.write('\n')
                     f.write(user_phone)

                 print ('uploaded details are:\n ',user_fname, '\n', user_lname,'\n', E_mail)

                 print('successful !')
                 checkpoint= 'passed'
             else:
                 re_do= input ('do you wish to continue with sign-up?\n yes\t no\n...')
                 if re_do == 'yes':
                     while E_mail != i:
                         E_mail= str(input('Enter Email address in this formart (myadress123@youmail.com)\n---'))
                     else:
                         checkpoint= 'passed'
                 else:
                     print('process terminated successfully!')
                     checkpoint='denied'

                 checkpoint= 'denied'
                 break
         else:
             print('logging in...')  
             checkpoint='passed'      

        



            


if checkpoint == 'passed':

    basket=''
    while basket =='':
        basket= characters
        no_passwords= 1
        no_digits= int(input('How long do you wish your password to be?' +'NOTICE'+' \n password should have at most 5 figures\n---'))
    else:
        basket=''
        
        if no_digits <= 5:
            for i in range (0,no_passwords):
                password=''
                for i in range (0, no_digits):
                        swapper_2= random.choice(characters)
                        password= password , swapper_2
                
            print('new password generated...', password)
            
        else:
                print('too many characters, retry')
                no_digits= int(input('How long do you wish your password to be?' +'NOTICE'+' \n password should have at most 20 figures\n---'))
                


            
    import random
    name= input('enter your name please?\n---')
    P_number= str(input('enter phone number\n---'))
            
            
            #trying to pull indivudual vaues from the inputed values
    shuffled= list(name)#
    random.shuffle(shuffled)
    shuffled= ''.join(shuffled)
    shuffled_2= list(P_number)#
    random.shuffle(shuffled_2)
    shuffled= ''.join(shuffled_2)
    shuffled_3= list(E_mail)#
    random.shuffle(shuffled_3)
    shuffled= ''.join(shuffled_3)

    characters= (shuffled,shuffled_2,shuffled_3)
    print (characters)


    word = (shuffled)
    shuffled = list(word)
    random.shuffle(shuffled)
    shuffled = ''.join(shuffled)
    print( shuffled)
'''