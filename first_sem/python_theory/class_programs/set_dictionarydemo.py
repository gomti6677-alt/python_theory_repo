name=input("enter the name")
number=int(input("enter the number"))
company=input("enter the company name")
salary=int(input("enter the salary"))
name2=input("enter the name")
number2=int(input("enter the number"))
company2=input("enter the company name")
salary2=int(input("enter the salary"))
employee1={name,number,company,salary}
print(employee1)


employee2={"name":name2,"phone_number":number2,"company_name":company2,"salary":salary2}
print(employee2)
age=int(input("enter the age"))
employee1.update([age])
print(employee1)
email=input("enter the email")
employee2["email"]=email
print(employee2["phone_number"])
print(employee2)









