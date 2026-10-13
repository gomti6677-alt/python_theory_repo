for letter in range(10):
    print(threshold=input("threshold:")
category=input("category:")
date=input("date:")
if unit<=100:
    if category=="commercial":
        if threshold=="yes":
            amount=(unit*10)+100
            print("the amount=",amount)
        else:
            amount=(unit*10)
            print("the amount=",amount)
    if category=="non commercial":
        if threshold=="yes":
            amount=(unit*5)+50
            print("the amount=",amount)
        else:
            amount=(unit*5)
            print("the amount=",amount)
elif unit>300:
    if category=="commercial":
        if threshold=="yes":
            amount=(100*10)+((unit-100)*15)+100
            print("the amount=",amount)
        else:
            amount=(100*10)+((unit-100)*15)
            print("the amount=",amount)
    if category=="non commercial":
        if threshold=="yes":
            amount=(100*10)+((unit-100)*8)+50
            print("the amount=",amount)
        else:
            amount=(100*10)((unit-100)*8)
            print("the amount=",amount)
else:
    if category=="commercial":
            if threshold=="yes":
                amount=(100*10)+((unit-100)*12)+100
                print("the amount=",amount)
            else:
                amount=(100*10)+((unit-100)*15)
                print("the amount=",amount)
    if category=="non commercial":
            if threshold=="yes":
                amount=(100*10)+((unit-100)*6)+50
                print("the amount=",amount)
            else:
                amount=(100*10)+((unit-100)*6)
                print("the amount=",amount)
age=int (input("age:"))
day=input("day:")
show=input("show timing:")
price=250
if day=="weekend":
    if show=="morning show":
        if age<=5:
            amount=price*(50/100)*(125/100)
            print("ticket price=",amount)
        elif age>=60:
            amount=price*(90/100)*(125/100)i+1,"good morning")