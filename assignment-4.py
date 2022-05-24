acc_bal= input ("enter account balance")


if (int(acc_bal) >100,000) and (int(acc_bal) <200,000):
    acc_bal = int (acc_bal) -250,000
    print("we have deducted ksh 25,000")

elif (int (acc_bal) > 5,000,000 and int(acc_bal) < 1,000,000):
    acc_bal = int(0.3 * acc_bal) 
    print ("we have deducte 30% percent from your account")

elif (int(acc_bal) > 1,000,000):
    acc_bal = int(acc_bal) - 15,000
    print ("sorry bro")

