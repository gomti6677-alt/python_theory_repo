customer_name=input("customers name")
recharge_amount=float(input("recharge plan amount"))
plan_type=input("plan type ('prepaid' or 'postpaid')")
members_sharing_plan=int(input("number of family members sharing the plan"))
festival=input("is it festival(yes/no)")
if festival=='yes':
    discount=recharge_amount*0.15
else:
    discount=0
processing_fee=recharge_amount*0.02
if plan_type=='postpaid': 
    flat_payment_charge=25
else:
    flat_payment_charge=0
final_amount= recharge_amount-discount+processing_fee+flat_payment_charge
cashback= int(final_amount*0.01)
if final_amount > 500:
    cashback=cashback+10
amount_per_member= round(final_amount /members_sharing_plan,2)
left_over=round(final_amount-(amount_per_person*members_sharing_plan),2
print("customer name:",customer_name)
print("recharge amount:",recharge_amount)
print("plan type:",plan_type)
print("family members sharing the plan",members_sharing_plan)
print("is it festival:",fesvial)
print("festival dicount :₹%.2f"% discount)
print("processing fee:%.2f"%processing_fee)
print("late payment charge:₹%.2f"%flat_payment_charge)

print("---------------------------------------------------")
p
             