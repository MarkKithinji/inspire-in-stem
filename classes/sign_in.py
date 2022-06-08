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
    f.write(user_phone)
    f.write('\n')
    f.write(E_mail)

print ('uploaded details are:\n ',user_fname, '\n', user_lname,'\n', E_mail)

print('successful !')