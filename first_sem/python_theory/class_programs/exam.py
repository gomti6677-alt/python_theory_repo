customer_name=input("customers name")
bill_amount=float(input("food bill amount"))
people_sharing_bill=int(input("number of people sharing the bill"))
weekend=input("is it weekend(yes/no)")
type=input("customer typr('new'or'loyal')")
if weekend=='yes':
    weekend_surcharge=bill_amount*0.10
else:
    weekend_surcharge=0
if type=='loyal':
    discount=bill_amount*0.08
else:
    discount=0
subtotal=bill_amount+weekend_surcharge-discount
gst=subtotal* 0.05
final_bill=subtotal+gst
loyalty_points=int(bill_amount//100)
if final_bill>1000:
loyalty_points=loyalty_points+20

amount_per_person=round(final_bill/people_sharing_bill,2)
leftover_amount=round(final_amount-(amount_per_person*people),2)



