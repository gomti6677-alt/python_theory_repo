customer_name=input(" customer name")
food_bill=float(input("food bill amount"))
people=int(input("number of people sharing the bill"))
weekend=input("is it weekend? (yes/no):")
type=input(customer type('new' or 'loyal'))
if weekend=="yes":
    weekend_surcharge=food_bill*0.10
else:
    weekend_surcharge=0
if type=="loyal":
    discount=(food_bill + weekend_surcharge)*0.08
else:
    discount=0
    sub_total= food_bill + weekend_surcharge
gst= subtotal*0.05
final_bill=subtotal+gst
loyality_points=int(food_bill//100)

if final_bill>1000:
    loyality_points=loyality_points+20

    

