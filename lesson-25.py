'''
i am comment
'''

# creating a list and unpacking

'''clothes = ['kofia', 'jordans', 't-shirt', 'bell-bottoms']

A, B, C, D = clothes
print(A)'''

# trying to use dictionaries


detail_bank = {'duolingo': 'IamFrench2020#', 'geeZ_club': '252509', 'I-Carly': 1277, 'account_pin': '2062'}
y = detail_bank.keys()
x = detail_bank.values()
stp_1= input('are you sure you want to retrieve data?\n yes\t no\n ...')
acc= 'yes'
den= 'no'
basket_2=''
while basket_2=='':
    if stp_1 == acc:
        stp_2= input ('enter password---')
        basket_2= acc
                
        
        if stp_2 == detail_bank['account_pin']:
            print("verifying....")
        
            print ("welcome back to account information retrival\n your accounts include: ", detail_bank.keys)
            basket=""
            while basket=="":
                getinfo = input("enter account name...")
                print("retrieving information for your account... ")
                for y in detail_bank:
                    if y==getinfo:
                        basket=y
                if basket!="":
                    print("Your password is : ",detail_bank.get(basket))
                else:
                        print("could not retrieve data,\n consider rechecking the spelling \n then retry")
            
        else:
            print ('wrong password. retry')
    elif stp_1== den:
        print('process terminated successfully\n goodbye')
        basket_2= den
    else:
          print('invalid choice. retry')
          stp_1= input('are you sure you want to retrieve data?\n yes\t no\n ...')
          

     
     
        
                
