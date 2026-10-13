customer_name=input("customer name")
plan_amount=float(input("recharge plan amount"))
plan_type=input("plan type('prepaid'or'postpaid)")
members=int(input("number of family members sharintn the plan"))
festival=input("is it festival offer(yes/no)")
if festival=='yes':
    discount=plan_amount*0.15
else:
    discount=0
processing_fee=plan_amount*0.02
if type=='postpaid':
    late_payment_charge=25
else:
    late_payment_charge=0

    finam_amount=plan_amount-discount+processing_fee+late_payment_charge
    cashback=int(final_amount*0.01)
    if finamamount>500:
        cashbook=cashback+10






    