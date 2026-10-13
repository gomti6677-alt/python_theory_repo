
acc_name=input("account name")
acc_number=int(input("account number"))
while(True):
        if (acc_number!=1000):
            print("invalid number please try again")
        else:
            break
dob=int(input("date of birth"))
pan_number=int(input("pan number"))
return acc_name,acc_number,dob,pan_number
details=(acc_name,acc_number,dob,pan_number)
bankdetails=[acc_name,acc_number,dob,pan_number,(details)]



    